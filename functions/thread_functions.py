import os
import logging
import requests
import sys
import platform
import time
import urllib
from functions.material_functions import tree_objects_init
from functions.utilities import set_size
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from ui._version import _gui_version
from distutils.version import LooseVersion
        

class FindFilesAndPopulate(Qt.QThread):
    finished = QtCore.pyqtSignal(list)
    
    def __init__(self, path):
        Qt.QThread.__init__(self)
        logging.info('thread_functions.py - FindFilesAndPopulate - __init__')
        self.path = path
        tree_objects_init(self)
        
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
            file_list.append([filename, filesize, filesize_str, filetype,'icons/' + iconfile])
        self.finished.emit(file_list)
    
    def stop(self):
        logging.debug('thread_functions.py - FindFilesAndPopulate - stop')
        self.terminate()


class CheckOrionFTPOnline(Qt.QThread):
    finished = QtCore.pyqtSignal(str)
    
    def __init__(self):
        Qt.QThread.__init__(self)
        logging.info('thread_functions.py - CheckOrionFTPOnline - __init__')
    
    def run(self):
        logging.debug('thread_functions.py - CheckOrionFTPOnline - run')
        url = 'https://api.github.com/repos/olivierpascalhenry/OrionFTP/releases/latest'
        try:
            json_object = requests.get(url=url).json()
            format = ''
            if getattr(sys, 'frozen', False) :
                if platform.system() == 'Windows':
                    format = '.msi'
                elif platform.system() == 'Linux':
                    format = '.tar.gz'
            else:
                format = 'sources.zip'
            if LooseVersion(_gui_version) < LooseVersion(json_object['tag_name']):
                assets = json_object['assets']
                download_url = 'no new version'
                for asset in assets:
                    link = asset['browser_download_url']
                    if format in link:
                        download_url = link  
                self.finished.emit(download_url)
            else:
                self.finished.emit('no new version')
        except Exception:
            logging.exception('thread_functions.py - CheckOrionFTPOnline - run - internet connection error - url ' + url)

    def stop(self):
        logging.debug('thread_functions.py - CheckOrionFTPOnline - stop')
        self.terminate()


class DownloadFile(Qt.QThread):
    download_update = QtCore.pyqtSignal(list)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal()
    
    def __init__(self, url_name, update_file, config_dict, translations_dict):
        Qt.QThread.__init__(self)
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
        try:
            opened_url = urllib.request.urlopen(self.url_name, timeout=10)
            totalFileSize = int(opened_url.info()['Content-Length'])
            bufferSize = 9192
            fileSize = 0
            start = time.time()
            while True:
                if self.cancel:
                    opened_file.close()
                    break
                buffer = opened_url.read(bufferSize)
                if not buffer:
                    break
                fileSize += len(buffer)
                opened_file.write(buffer)
                download_speed = set_size(fileSize/(time.time() - start)) + '/s'
                self.download_update.emit([round(fileSize * 100 / totalFileSize), download_text % (self.filename, download_speed)])
            opened_file.close()
            if not self.cancel:
                logging.debug('thread_functions.py - DownloadFile - run - download finished')
                self.download_done.emit()
            else:
                logging.debug('thread_functions.py - DownloadFile - run - download canceled')
        except Exception:
            logging.exception('thread_functions.py - DownloadFile - run - connexion issue ; self.url_name ' + self.url_name)
            opened_file.close()
            self.download_failed.emit()
    
    def cancel_download(self):
        logging.debug('thread_functions.py - DownloadFile - cancel_download')
        self.cancel = True
    
    def stop(self):
        logging.debug('thread_functions.py - DownloadFile - stop')
        self.terminate()
