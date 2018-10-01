import logging
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_managerwindow import Ui_managerWindow
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_optionwindow import Ui_optionWindow
from functions.utilities import translate_elements
from functions.material_functions import profile_window_objects_initialization


class MyManager(QtWidgets.QDialog, Ui_managerWindow):
    def __init__(self, config_dict, translations_dict, ftp_profiles):
        logging.info('window_functions.py - MyManager - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        self.translations_dict = translations_dict
        self.ftp_profiles = ftp_profiles
        self.current_name = ''
        self.save = False
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.mw_combobox.setItemDelegate(itemDelegate)
        profile_window_objects_initialization(self)
        self.resize(900, 360)
        translate_elements(self, config_dict['OPTIONS'].get('language'), translations_dict)
        self.parse_ftp_profiles()
        self.mw_cancel_button.clicked.connect(self.close_window)
        self.mw_ok_button.clicked.connect(self.save_profiles)
        self.mw_add_button.clicked.connect(self.add_profile_item)
        self.mw_del_button.clicked.connect(self.del_profile_item)
        self.mw_profile_list.currentTextChanged.connect(self.display_profile_data)
        self.mw_profile_list.itemChanged.connect(self.change_profile_name)
        
        
    def change_profile_name(self, val):
        try:
            self.ftp_profiles[str(val.text())] = self.ftp_profiles.pop(self.current_name)
            self.current_name = str(val.text())
        except KeyError:
            self.current_name = str(val.text())
        
    def set_data_in_dict(self, val):
        try:
            self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]
        except KeyError:
            profile = {'protocol': 'ftp', 'host':'', 'port':'', 'username':'', 'password':''}
            self.ftp_profiles[str(self.mw_profile_list.currentItem().text())] = profile
        if isinstance(self.sender(), QtWidgets.QComboBox):
            self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['protocol'] = self.ftp_protocols_dict[str(self.sender().currentText())]
        elif isinstance(self.sender(), QtWidgets.QLineEdit):
            if '1' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['host'] = str(self.sender().text())
            elif '2' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['port'] = str(self.sender().text())
            elif '3' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['username'] = str(self.sender().text())
            elif '4' in self.sender().objectName():
                self.ftp_profiles[str(self.mw_profile_list.currentItem().text())]['password'] = base64.b64encode(str.encode(self.sender().text()))
    
    def parse_ftp_profiles(self):
        for key in self.ftp_profiles:
            item = QtWidgets.QListWidgetItem()
            item.setText(key)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
            self.mw_profile_list.addItem(item)
        if self.mw_profile_list.count() > 0:
            self.mw_ok_button.setEnabled(True)
    
    def add_profile_item(self):
        i = self.mw_profile_list.count() + 1
        item = QtWidgets.QListWidgetItem()
        item.setText('new_server_' + str(i))
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        self.mw_profile_list.addItem(item)
        self.mw_profile_list.setCurrentItem(item)
        self.mw_profile_list.editItem(item)
        self.mw_ok_button.setEnabled(True)
    
    def del_profile_item(self):
        profile = str(self.mw_profile_list.currentItem().text())
        try:
            self.ftp_profiles.pop(profile)
        except KeyError:
            pass
        item = self.mw_profile_list.takeItem(self.mw_profile_list.currentRow())
        item = None
        self.deactivate_profile_fields()
            
    def display_profile_data(self, val):
        self.current_name = str(val)
        try:
            self.mw_combobox.currentIndexChanged.disconnect(self.set_data_in_dict)
            self.mw_line_1.textChanged.disconnect(self.set_data_in_dict)
            self.mw_line_2.textChanged.disconnect(self.set_data_in_dict)
            self.mw_line_3.textChanged.disconnect(self.set_data_in_dict)
            self.mw_line_4.textChanged.disconnect(self.set_data_in_dict)
        except:
            pass
        self.activate_profile_fields()
        try:
            profile = self.ftp_profiles[val]
            try:
                self.mw_combobox.setCurrentIndex(self.mw_combobox.findText(self.inv_ftp_protocols_dict[profile['protocol']]))
            except:
                pass
            try:
                self.mw_line_1.setText(profile['host'])
            except:
                pass
            try:
                self.mw_line_2.setText(profile['port'])
            except:
                pass
            try:
                self.mw_line_3.setText(profile['username'])
            except:
                pass
            try:
                self.mw_line_4.setText(base64.b64decode(profile['password']).decode('utf-8'))
            except:
                pass
            
        except KeyError:
            pass
        self.mw_combobox.currentIndexChanged.connect(self.set_data_in_dict)
        self.mw_line_1.textChanged.connect(self.set_data_in_dict)
        self.mw_line_2.textChanged.connect(self.set_data_in_dict)
        self.mw_line_3.textChanged.connect(self.set_data_in_dict)
        self.mw_line_4.textChanged.connect(self.set_data_in_dict)
        
    def activate_profile_fields(self):
        self.mw_combobox.setEnabled(True)
        self.mw_line_1.setEnabled(True)
        self.mw_line_2.setEnabled(True)
        self.mw_line_3.setEnabled(True)
        self.mw_line_4.setEnabled(True)
        self.mw_del_button.setEnabled(True)
        self.mw_combobox.setCurrentIndex(0)
        self.mw_line_1.setText('')
        self.mw_line_2.setText('')
        self.mw_line_3.setText('')
        self.mw_line_4.setText('')
    
    def deactivate_profile_fields(self):
        if self.mw_profile_list.count() == 0:
            self.mw_combobox.setEnabled(False)
            self.mw_line_1.setEnabled(False)
            self.mw_line_2.setEnabled(False)
            self.mw_line_3.setEnabled(False)
            self.mw_line_4.setEnabled(False)
            self.mw_del_button.setEnabled(False)
            self.mw_combobox.setCurrentIndex(0)
            self.mw_line_1.setText('')
            self.mw_line_2.setText('')
            self.mw_line_3.setText('')
            self.mw_line_4.setText('')
    
    def save_profiles(self):
        self.save = True
        self.close_window()
    
    def close_window(self):
        logging.debug('window_functions.py - MyManager - close_window')
        self.close()
    
    def closeEvent(self, event):
        if not self.save:
            self.ftp_profiles = None

        
class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, config_dict, translations_dict):
        logging.info('window_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        translate_elements(self, config_dict['OPTIONS'].get('language'), translations_dict)
        self.aw_browser_2.setPlainText(open("documentation/changelog.txt").read())
        self.aw_button.clicked.connect(self.close_window)

    def close_window(self):
        logging.debug('window_functions.py - MyAbout - close_window')
        self.close()





class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict, translations_dict, ftp_profile_list):
        logging.info('window_functions.py - MyOptions - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        self.translations_dict = translations_dict
        self.ftp_profile_list = ftp_profile_list
        translate_elements(self, config_dict['OPTIONS'].get('language'), translations_dict)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.ow_combobox_1.setItemDelegate(itemDelegate)
        self.ow_combobox_2.setItemDelegate(itemDelegate)
        self.ow_combobox_3.setItemDelegate(itemDelegate)
        self.ow_ok_button.clicked.connect(self.save_and_close)
        self.ow_cancel_button.clicked.connect(self.close_window)
        self.ow_openButton_1.clicked.connect(self.get_directory)
        self.ow_openButton_2.clicked.connect(self.get_directory)
        '''all_info_boxes = self.findChildren(QtWidgets.QToolButton)
        for widget in all_info_boxes:
            if 'infoButton' in widget.objectName():
                widget.clicked.connect(lambda: self.info_button())'''
        self.cancel = True
        self.setTabOrder(self.ow_line_1,self.ow_line_2)
        self.ow_line_1.setFocus()
        self.set_ftp_profile_list()
        self.read_config_dict()
    
    def set_ftp_profile_list(self):
        if self.ftp_profile_list:
            self.ow_combobox_3.clear()
            self.ow_combobox_3.addItem(self.translations_dict['makeachoice'][self.config_dict['OPTIONS'].get('language')])
            self.ow_combobox_3.addItems(self.ftp_profile_list)
    
    def read_config_dict(self):
        logging.debug('window_functions.py - MyOptions - read_config_dict')
        log_level = self.config_dict.get('LOG', 'level')
        log_path = self.config_dict.get('LOG', 'path')
        check_update = self.config_dict['OPTIONS'].getboolean('check_update')
        language = self.config_dict.get('OPTIONS', 'language')
        default_profile = self.config_dict.get('OPTIONS', 'default_profile')
        local_home = self.config_dict.get('OPTIONS', 'local_home')
        self.ow_combobox_1.setCurrentIndex(self.ow_combobox_1.findText(log_level))
        self.ow_combobox_2.setCurrentIndex(self.ow_combobox_2.findText(language.title()))
        self.ow_line_1.setText(log_path)
        self.ow_line_2.setText(local_home)
        self.ow_checkbox_1.setChecked(check_update)
        if default_profile:
            self.ow_combobox_3.setCurrentIndex(self.ow_combobox_3.findText(default_profile))
    
    def get_directory(self):
        logging.debug('window_functions.py - MyOptions - get_directory')
        file_dialog = QtWidgets.QFileDialog()
        out_dir = file_dialog.getExistingDirectory(self, "Select Directory")
        if self.sender().objectName() == 'ow_openButton_1':
            self.ow_line_1.setText(str(out_dir.replace('/','\\')))
        elif self.sender().objectName() == 'ow_openButton_2':
            self.ow_line_2.setText(str(out_dir.replace('/','\\')))
    
    def save_and_close(self):
        logging.debug('window_functions.py - MyOptions - save_and_close')
        self.cancel = False
        self.config_dict.set('LOG', 'level', str(self.ow_combobox_1.currentText()))
        self.config_dict.set('LOG', 'path', str(self.ow_line_1.text()))
        self.config_dict.set('OPTIONS', 'check_update', str(self.ow_checkbox_1.isChecked()))
        self.config_dict.set('OPTIONS', 'language', str(self.ow_combobox_2.currentText()).lower())
        if '...' not in self.ow_combobox_3.currentText():
            default_profile = str(self.ow_combobox_3.currentText())
        else:
            default_profile = ''
        self.config_dict.set('OPTIONS', 'default_profile', default_profile)
        self.config_dict.set('OPTIONS', 'local_home', str(self.ow_line_2.text()))
        self.close_window()
    
    '''def info_button(self):
        logging.debug('window_functions.py - MyOptions - info_button - self.sender().objectName() ' + self.sender().objectName())
        if 'infoButton' in self.sender().objectName():
            self.infoWindow = MyInfo(self.info_text[self.sender().objectName()])
            self.infoWindow.move(QtGui.QCursor.pos().x() - 275, QtGui.QCursor.pos().y() + 20)
            self.infoWindow.exec_()'''
    
    def close_window(self):
        logging.info('window_functions.py - MyOptions - close_window')
        self.close()


'''class MyUpdate(QtWidgets.QDialog, Ui_storeWindow):
    def __init__(self, url, folder):
        logging.info('window_functions.py - MyUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.temp_folder = folder
        self.url = url
        if platform.system() == 'Windows':
            self.update_file = self.temp_folder + '\\' + self.url[self.url.rfind('/')+1:]
        elif platform.system() == 'Linux':
            self.update_file = self.temp_folder + '/' + self.url[self.url.rfind('/')+1:]
        self.sw_button.clicked.connect(self.cancel_download)
        self.cancel = False
        self.download_update()
    
    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.progressBar.setValue(val[0])
            self.sw_label.setText(val[1])
        else:
            self.progressBar.setValue(val)
    
    def download_update(self):
        logging.debug('window_functions.py - MyUpdate - download_update')
        self.thread = DownloadFile(self.url, self.update_file)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.close)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()
    
    def cancel_download(self):
        logging.debug('window_functions.py - MyUpdate - cancel_download')
        self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close()
        
    def download_failed(self):
        logging.debug('window_functions.py - MyUpdate - download_failed')
        self.update_progress_bar(0)
        self.sw_label.setText('Download failed')
        self.cancel_download()
        
    def closeEvent(self, event):
        logging.info('window_functions.py - MyUpdate - closeEvent')
        self.thread.download_update.disconnect(self.update_progress_bar)
        if self.cancel:
            os.remove(self.update_file)'''



        
        
'''class MyCredentials(QtWidgets.QDialog, Ui_credentialsWindow):
    def __init__(self, user, password):
        QtWidgets.QWidget.__init__(self)
        logging.info('mainwindow.py - MyCredentials - __init__')
        self.setupUi(self)
        if user:
            self.edit_1.setText(user)
        if password:
            self.edit_2.setText(password)
        self.username = ''
        self.password = ''
        self.submit.clicked.connect(self.set_username_password)
        self.cancel.clicked.connect(self.closeWindow)

    def set_username_password(self):
        logging.debug('window_functions.py - MyCredentials - set_username_password')
        self.username = str(self.edit_1.text())
        self.password = str(self.edit_2.text())
        self.closeWindow()

    def closeWindow(self):
        logging.info('window_functions.py - MyCredentials - closeWindow')
        self.close()'''
        
        



'''class CustomTreeItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent, status_object, file_object, progress_object):
        super(CustomTreeItem, self).__init__(parent)
        parent.setItemWidget(self, 0, status_object)
        parent.setItemWidget(self, 1, file_object)
        parent.setItemWidget(self, 2, progress_object)'''
        