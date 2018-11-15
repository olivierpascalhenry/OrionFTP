import os
import logging
import requests
import sys
import platform
import urllib
import time
import ftplib
import paramiko
import socket
from functions.material_functions import tree_objects_init
from functions.utilities import set_size
from PyQt5 import QtCore
from ui.version import gui_version
from distutils.version import LooseVersion
        

class FindFilesAndPopulate(QtCore.QThread):
    finished = QtCore.pyqtSignal(list)
    
    def __init__(self, path):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - FindFilesAndPopulate - __init__')
        self.path = path
        self.file_types, self.type_icons = tree_objects_init()
        
    def run(self):
        logging.debug('thread_functions.py - FindFilesAndPopulate - run')
        file_list = []
        for filename in next(os.walk(self.path))[2]: 
            filepath = self.path + '/' + filename
            filesize = os.path.getsize(filepath)
            filesize_str = set_size(os.path.getsize(filepath))
            if os.path.splitext(filepath)[1][1:]:
                try:
                    filetype = self.file_types[os.path.splitext(filepath)[1][1:]]
                    iconfile = self.type_icons[filetype]
                except KeyError:
                    filetype = os.path.splitext(filepath)[1][1:].upper() + ' File'
                    iconfile = 'file_icon.png'
            else:
                filetype = 'File'
                iconfile = 'file_icon.png'
            if not iconfile:
                iconfile = 'file_icon.png'
            file_list.append([filename, filesize, filesize_str, filetype, 'icons/' + iconfile])
        self.finished.emit(file_list)
    
    def stop(self):
        logging.debug('thread_functions.py - FindFilesAndPopulate - stop')
        self.terminate()


class CheckOrionFTPOnline(QtCore.QThread):
    finished = QtCore.pyqtSignal(str)
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - CheckOrionFTPOnline - __init__')
    
    def run(self):
        logging.debug('thread_functions.py - CheckOrionFTPOnline - run')
        url = 'https://api.github.com/repos/olivierpascalhenry/OrionFTP/releases/latest'
        # noinspection PyBroadException
        try:
            json_object = requests.get(url=url).json()
            file_format = ''
            if getattr(sys, 'frozen', False):
                if platform.system() == 'Windows':
                    file_format = '.msi'
                elif platform.system() == 'Linux':
                    file_format = '.tar.gz'
            else:
                file_format = 'sources.zip'
            if LooseVersion(gui_version) < LooseVersion(json_object['tag_name']):
                assets = json_object['assets']
                download_url = 'no new version'
                for asset in assets:
                    link = asset['browser_download_url']
                    if file_format in link:
                        download_url = link  
                self.finished.emit(download_url)
            else:
                self.finished.emit('no new version')
        except Exception:
            logging.exception('thread_functions.py - CheckOrionFTPOnline - run - internet connection error - url '
                              + url)

    def stop(self):
        logging.debug('thread_functions.py - CheckOrionFTPOnline - stop')
        self.terminate()


class DownloadFile(QtCore.QThread):
    download_update = QtCore.pyqtSignal(list)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal()
    
    def __init__(self, url_name, update_file, config_dict, translations_dict):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - DownloadFile - __init__ - url_name ' + str(url_name))
        self.url_name = url_name
        self.update_file = update_file
        self.filename = self.url_name[self.url_name.rfind("/")+1:]
        self.cancel = False
        self.config_dict = config_dict
        self.translations_dict = translations_dict
        
    def run(self):
        logging.debug('thread_functions.py - DownloadFile - run')
        download_text = self.translations_dict['downloadingat'][self.config_dict['OPTIONS'].get('language')]
        pre_download_text = self.translations_dict['downloading'][self.config_dict['OPTIONS'].get('language')]
        self.download_update.emit([0, pre_download_text % self.filename])
        opened_file = open(self.update_file, 'wb')
        # noinspection PyBroadException
        try:
            opened_url = urllib.request.urlopen(self.url_name, timeout=10)
            total_file_size = int(opened_url.info()['Content-Length'])
            buffer_size = 9192
            file_size = 0
            start = time.time()
            while True:
                if self.cancel:
                    opened_file.close()
                    break
                buffer = opened_url.read(buffer_size)
                if not buffer:
                    break
                file_size += len(buffer)
                opened_file.write(buffer)
                download_speed = set_size(file_size/(time.time() - start)) + '/s'
                self.download_update.emit([round(file_size * 100 / total_file_size),
                                           download_text % (self.filename, download_speed)])
            opened_file.close()
            if not self.cancel:
                logging.debug('thread_functions.py - DownloadFile - run - download finished')
                self.download_done.emit()
            else:
                logging.debug('thread_functions.py - DownloadFile - run - download canceled')
        except Exception:
            logging.exception('thread_functions.py - DownloadFile - run - connexion issue ; self.url_name '
                              + self.url_name)
            opened_file.close()
            self.download_failed.emit()
    
    def cancel_download(self):
        logging.debug('thread_functions.py - DownloadFile - cancel_download')
        self.cancel = True
    
    def stop(self):
        logging.debug('thread_functions.py - DownloadFile - stop')
        self.terminate()


class DownloadFTPFile(QtCore.QThread):
    download_update = QtCore.pyqtSignal(list)
    update_status = QtCore.pyqtSignal(list)
    update_down_widget = QtCore.pyqtSignal()
    download_done = QtCore.pyqtSignal(list)
    download_failed = QtCore.pyqtSignal()
    download_canceled = QtCore.pyqtSignal(int)
    all_download_canceled = QtCore.pyqtSignal()

    def __init__(self, ftp, file_list, folder, translations_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - DownloadFTPFile - __init__')
        self.translations_dict = translations_dict
        self.config_dict = config_dict
        self.ftp = ftp
        self.file_list = file_list
        self.folder = folder
        self.cancel = False
        self.cancel_all = False
        self.connected = True
        self.downloading = False
        self.file_path = None
        self.local_file_path = None

    def run(self):
        logging.debug('thread_functions.py - DownloadFTPFile - run - download started')
        text_1 = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][0]
        text_2 = ''
        self.f = None
        self.downloading = True
        try:
            for i, file in enumerate(self.file_list):
                logging.debug('thread_functions.py - DownloadFTPFile - run - file: ' + file['file'])
                if i > 0:
                    if self.cancel:
                        text_2 = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][
                                3]
                        self.cancel = False
                    else:
                        text_2 = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][
                                1]
                self.file_path = file['path'] + file['file']
                self.local_file_path = self.folder + '/' + file['local_name']
                self._update_status([0, 'Downloading ' + self.file_path])
                self.download_update.emit([i, text_1, text_2, '', 0])
                self._update_status([1, 'TYPE i'])
                message = self.ftp.sendcmd('TYPE i')
                self._update_status([2, message])
                self._update_status([1, ' SIZE ' + self.file_path])
                self.total_size = self.ftp.size(self.file_path)
                self._update_status([2, self.total_size])
                self._update_status([1, 'TYPE A'])
                message = self.ftp.sendcmd('TYPE A')
                self._update_status([2, message])
                self.file_size = 0
                self.f = open(self.local_file_path, 'wb')
                start = time.time()

                def callback(data):
                    if self.cancel or self.cancel_all:
                        self.f.close()
                    else:
                        self.file_size += len(data)
                        try:
                            download_speed = set_size(self.file_size / (time.time() - start)) + '/s'
                        except ZeroDivisionError:
                            download_speed = '0 B/s'
                        self.download_update.emit([i, text_1, text_2, download_speed,
                                                   round(self.file_size * 100 / self.total_size)])
                        try:
                            self.f.write(data)
                        except ValueError:
                            pass

                try:
                    self._update_status([1, 'RETR ' + self.file_path])
                    message = self.ftp.retrbinary('RETR ' + self.file_path, callback)
                    self._update_status([2, message])
                    self.f.close()
                except (AttributeError, ftplib.error_reply, OSError) as e:
                    if self.cancel:
                        self._update_status([0, 'Download of file ' + self.file_path
                                             + ' has been canceled.'])
                        self.connected = False
                    elif self.cancel_all:
                        self._update_status([0, 'All downloads have been canceled.'])
                        self.connected = False
                    elif "'NoneType' object has no attribute 'readline'" in str(e):
                        self.downloading = False
                        try:
                            self.f.close()
                            os.remove(self.local_file_path)
                        except PermissionError:
                            logging.exception('thread_functions.py - DownloadFTPFile - run - PermissionError - The '
                                              + 'file couldn\'t be removed.')
                        return

                if self.cancel_all or self.cancel:
                    while True:
                        if self.connected:
                            break
                    try:
                        self.f.close()
                        self.f = None
                        os.remove(self.local_file_path)
                    except PermissionError:
                        logging.exception('thread_functions.py - DownloadFTPFile - run - PermissionError - The file '
                                          + 'couldn\'t be removed.')
                    if self.cancel_all:
                        break
                    if self.cancel:
                        continue

            if self.cancel_all:
                logging.debug('thread_functions.py - DownloadFTPFile - run - all download canceled')
                self.all_download_canceled.emit()
                self.downloading = False
            elif self.cancel:
                logging.debug('thread_functions.py - DownloadFTPFile - run - download canceled')
                self.download_canceled.emit(i)
                self.downloading = False
            else:
                logging.debug('thread_functions.py - DownloadFTPFile - run - download finished')
                text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][1]
                self.download_done.emit([len(self.file_list) - 1, text, '', '', 100])
                self.downloading = False

        except Exception:
            logging.exception('thread_functions.py - DownloadFTPFile - run - connexion issue')
            try:
                self.f.close()
            except Exception:
                pass
            self.download_failed.emit()
            self.downloading = False

    def cancel_download(self):
        logging.debug('thread_functions.py - DownloadFTPFile - cancel_download')
        self.cancel = True

    def cancel_all_download(self):
        logging.debug('thread_functions.py - DownloadFTPFile - cancel_all_download')
        self.cancel_all = True

    def _update_status(self, status_list):
        logging.debug('thread_functions.py - DownloadFTPFile - _update_status')
        self.update_status.emit(status_list)

    def close_file(self):
        logging.debug('thread_functions.py - DownloadFTPFile - close_file')
        try:
            self.f.close()
            self.f = None
            os.remove(self.local_file_path)
        except PermissionError:
            logging.exception('thread_functions.py - DownloadFTPFile - run - PermissionError - The file '
                              + 'couldn\'t be removed.')

    def stop(self):
        logging.debug('thread_functions.py - DownloadFTPFile - stop')
        self.terminate()


class SetDefaultLocalPath(QtCore.QThread):
    finished = QtCore.pyqtSignal()

    def __init__(self, path, local_tree_up):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - SetDefaultLocalPath - __init__')
        self.path = path
        self.local_tree_up = local_tree_up

    def run(self):
        logging.info('thread_functions.py - SetDefaultLocalPath - run')
        folder_list = list()
        if platform.system() == 'Windows':
            folder_list = self.path.split('\\')
        elif platform.system() == 'Linux':
            folder_list = self.path.split('/')
        path = ''
        index = None
        try:
            for i, folder in enumerate(folder_list):
                if i == 0:
                    path += folder
                else:
                    if platform.system() == 'Windows':
                        path += '\\' + folder
                    elif platform.system() == 'Linux':
                        path += '/' + folder
                index = self.local_tree_up.model().index(path)
                self.local_tree_up.expand(index)
        except AttributeError:
            logging.exception('thread_functions.py - SetDefaultLocalPath - run - error')
            index = None
        if index is not None:
            self.local_tree_up.setCurrentIndex(index)
        self.finished.emit()

    def stop(self):
        logging.debug('thread_functions.py - SetDefaultLocalPath - stop')
        self.terminate()


class ConnectFTP(QtCore.QThread):
    connection_start = QtCore.pyqtSignal()
    connection_update = QtCore.pyqtSignal(list)
    connected = QtCore.pyqtSignal(list)
    connection_error = QtCore.pyqtSignal()

    def __init__(self, host, port, transfer_mode, encryption, username, password, action):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - ConnectFTP - __init__')
        self.host = host
        self.port = port
        self.transfer_mode = transfer_mode
        self.encryption = encryption
        self.username = username
        self.password = password
        self.action = action

    def run(self):
        logging.info('thread_functions.py - ConnectFTP - run')
        self.connection_start.emit()
        try:
            self._update_status([0, 'Connecting to ' + self.host + ':' + self.port + '...'])
            if self.encryption == 'plain':
                ftp_protocol = ftplib.FTP(timeout=5)
            else:
                ftp_protocol = MyFTP_TLS(timeout=5)
            if self.transfer_mode == 0:
                ftp_protocol.set_pasv(True)
            else:
                ftp_protocol.set_pasv(False)
            message = ftp_protocol.connect(self.host, int(self.port))
            self._update_status([2, message])
            if self.encryption != 'plain':
                self._update_status([1, 'AUTH TLS'])
                message = ftp_protocol.auth()
                self._update_status([2, message])
                self._update_status([1, 'PROT P'])
                message = ftp_protocol.prot_p()
                self._update_status([2, message])
            self._update_status([1, 'USER ' + self.username + ' ; PASS **************'])
            message = ftp_protocol.login(self.username, self.password)
            self._update_status([2, message])
            self._update_status([1, 'OPTS UTF8 ON'])
            message = ftp_protocol.sendcmd("OPTS UTF8 ON")
            self._update_status([2, message])
            ftp_protocol.encoding = 'utf-8'
            self.connected.emit([self.action, ftp_protocol])
        except ftplib.error_perm as e:
            logging.exception('thread_functions.py - ConnectFTP - connection - error')
            if '550' in str(e):
                self._update_status([3, 'SSL/TLS required on the control channel'])
            elif '500' in str(e):
                self._update_status([3, 'AUTH not understood'])
            else:
                self._update_status([3, 'Login incorrect'])
            self.connection_error.emit()
        except socket.timeout:
            logging.exception('thread_functions.py - ConnectFTP - connection - error')
            self._update_status([3, 'The connection was refused by ' + self.host])
            self.connection_error.emit()
        except ConnectionRefusedError:
            logging.exception('thread_functions.py - ConnectFTP - connection - error')
            self._update_status([3, 'Timed out, no response from ' + self.host])
            self.connection_error.emit()

    def _update_status(self, status_list):
        self.connection_update.emit(status_list)

    def stop(self):
        logging.debug('thread_functions.py - ConnectFTP - stop')
        self.terminate()


class ConnectSFTP(QtCore.QThread):
    connection_start = QtCore.pyqtSignal()
    connection_update = QtCore.pyqtSignal(list)
    connected = QtCore.pyqtSignal(list)
    connection_error = QtCore.pyqtSignal()

    def __init__(self, host, port, username, password, action):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - ConnectSFTP - __init__')
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.action = action

    def run(self):
        logging.info('thread_functions.py - ConnectSFTP - run')
        self.connection_start.emit()
        try:
            self._update_status([0, 'Connecting to ' + self.host + ':' + self.port + '...'])
            self._update_status([1, 'Transport object init...'])
            transport = paramiko.Transport((self.host, int(self.port)))
            self._update_status([2, 'Transport object available'])
            self._update_status([1, 'Authentication pending for ' + self.username + '...'])
            transport.connect(username=self.username, password=self.password)
            self._update_status([2, 'Connection established for ' + self.username])
            self._update_status([2, 'Password ************* accepted for ' + self.username])
            self._update_status([1, 'Opening sftp connection...'])
            sftp_protocol = paramiko.sftp_client.SFTPClient.from_transport(transport)
            self._update_status([2, 'sftp connection opened'])
            self.connected.emit([self.action, sftp_protocol, transport])
        except paramiko.ssh_exception.SSHException as e:
            logging.exception('thread_functions.py - ConnectSFTP - connection - error')
            message = str(e).replace('paramiko.ssh_exception.SSHException: ', '')
            self._update_status([3, message])
            self.connection_error.emit()

    def _update_status(self, status_list):
        self.connection_update.emit(status_list)

    def stop(self):
        logging.debug('thread_functions.py - ConnectSFTP - stop')
        self.terminate()


class DownloadSFTPFile(QtCore.QThread):
    download_update = QtCore.pyqtSignal(list)
    update_status = QtCore.pyqtSignal(list)
    update_down_widget = QtCore.pyqtSignal()
    download_done = QtCore.pyqtSignal(list)
    download_failed = QtCore.pyqtSignal()
    download_canceled = QtCore.pyqtSignal(int)
    all_download_canceled = QtCore.pyqtSignal()

    def __init__(self, ftp, file_list, folder, translations_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('thread_functions.py - DownloadSFTPFile - __init__')
        self.translations_dict = translations_dict
        self.config_dict = config_dict
        self.ftp = ftp
        self.file_list = file_list
        self.folder = folder
        self.cancel = False
        self.cancel_all = False
        self.connected = True
        self.downloading = False
        self.file_path = None
        self.local_file_path = None

    def run(self):
        logging.debug('thread_functions.py - DownloadSFTPFile - run - download started')
        text_1 = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][0]
        text_2 = ''
        self.f = None
        self.downloading = True
        try:
            for i, file in enumerate(self.file_list):
                logging.debug('thread_functions.py - DownloadSFTPFile - run - file: ' + file['file'])
                if i > 0:
                    if self.cancel:
                        text_2 = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][
                                3]
                        self.cancel = False
                    else:
                        text_2 = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][
                                1]
                self.file_path = file['path'] + file['file']
                self.local_file_path = self.folder + '/' + file['local_name']
                self._update_status([0, 'Downloading ' + self.file_path])
                self.download_update.emit([i, text_1, text_2, '', 0])
                self._update_status([1, 'querying file size...'])
                self._update_status([2, str(self.ftp.stat(self.file_path).st_size)])
                self.file_size = 0
                self.f = open(self.local_file_path, 'wb')
                start = time.time()

                def callback(bytes_transfered, total_bytes):
                    try:
                        download_speed = set_size(bytes_transfered / (time.time() - start)) + '/s'
                    except ZeroDivisionError:
                        download_speed = '0 B/s'
                    value = round(bytes_transfered * 100 / total_bytes)
                    self.download_update.emit([i, text_1, text_2, download_speed, value])

                try:
                    self._update_status([1, 'get ' + self.file_path])
                    self.ftp.getfo(self.file_path, self.f, callback)
                    self.f.close()
                    self._update_status([2, self.local_file_path + ' has been downloaded'])
                except (paramiko.ssh_exception.SSHException, EOFError):
                    self._close_file()
                    if self.cancel:
                        self._update_status([0, 'Download of file ' + self.file_path + ' has been canceled.'])
                        self.connected = False
                    elif self.cancel_all:
                        self._update_status([0, 'All downloads have been canceled.'])
                        self.connected = False

                if self.cancel_all or self.cancel:
                    while True:
                        if self.connected:
                            break
                    if self.cancel_all:
                        break
                    if self.cancel:
                        continue

            if self.cancel_all:
                logging.debug('thread_functions.py - DownloadSFTPFile - run - all download canceled')
                self.all_download_canceled.emit()
                self.downloading = False
            elif self.cancel:
                logging.debug('thread_functions.py - DownloadSFTPFile - run - download canceled')
                self.download_canceled.emit(i)
                self.downloading = False
            else:
                logging.debug('thread_functions.py - DownloadSFTPFile - run - download finished')
                text = self.translations_dict['transferstatus'][self.config_dict['OPTIONS'].get('language')][1]
                self.download_done.emit([len(self.file_list) - 1, text, '', '', 100])
                self.downloading = False

        except Exception:
            logging.exception('thread_functions.py - DownloadSFTPFile - run - connexion issue')
            self._close_file()
            self.download_failed.emit()
            self.downloading = False

    def cancel_download(self):
        logging.debug('thread_functions.py - DownloadSFTPFile - cancel_download')
        self.cancel = True

    def cancel_all_download(self):
        logging.debug('thread_functions.py - DownloadSFTPFile - cancel_all_download')
        self.cancel_all = True

    def _update_status(self, status_list):
        logging.debug('thread_functions.py - DownloadSFTPFile - _update_status')
        self.update_status.emit(status_list)

    def _close_file(self):
        logging.debug('thread_functions.py - DownloadSFTPFile - _close_file')
        try:
            self.f.close()
            self.f = None
            os.remove(self.local_file_path)
        except PermissionError:
            logging.exception('thread_functions.py - DownloadSFTPFile - run - PermissionError - the file '
                              + 'couldn\'t be removed.')

    def stop(self):
        logging.debug('thread_functions.py - DownloadSFTPFile - stop')
        self.terminate()


class MyFTP_TLS(ftplib.FTP_TLS):
    def ntransfercmd(self, cmd, rest=None):
        conn, size = ftplib.FTP.ntransfercmd(self, cmd, rest)
        if self._prot_p:
            conn = self.context.wrap_socket(conn, server_hostname=self.host, session=self.sock.session)
        return conn, size
