import logging
import os
from PyQt5 import QtWidgets
    
    
def translate_elements(widget, language, translations_dict):
    logging.debug('utilities.py - translate_elements - language ' + language)
    for element, translation in translations_dict.items():
        if widget.objectName() == element:
            widget.setWindowTitle(translation[language])
        elif widget.findChildren(QtWidgets.QWidget, element):
            child_widget = None
            try:
                child_widget = widget.findChildren(QtWidgets.QWidget, element)[0]
                if isinstance(child_widget, QtWidgets.QLabel):
                    child_widget.setText(translation[language])
                elif isinstance(child_widget, QtWidgets.QTabWidget):
                    for i, item in enumerate(translation[language]):
                        child_widget.setTabText(i, item)
                elif isinstance(child_widget, QtWidgets.QTreeWidget):
                    for i, item in enumerate(translation[language]):
                        child_widget.headerItem().setText(i, item)
                elif isinstance(child_widget, QtWidgets.QToolButton):
                    if 'action' in element:
                        child_widget.setToolTip(translation[language])
                    else:
                        child_widget.setText(translation[language])
                elif isinstance(child_widget, QtWidgets.QComboBox):
                    if child_widget.count() == 1:
                        child_widget.clear()
                        child_widget.addItem(translation[language])
                    elif child_widget.count() > 1:
                        child_widget.clear()
                        child_widget.addItems(translation[language])
                elif isinstance(child_widget, QtWidgets.QTextBrowser):
                    child_widget.setHtml(translation[language])
                elif isinstance(child_widget, QtWidgets.QCheckBox):
                    child_widget.setText(translation[language])
                elif isinstance(child_widget, QtWidgets.QRadioButton):
                    child_widget.setText(translation[language])
            except KeyError:
                logging.exception('utilities.py - translate_elements - an element coudln\'t be found in the'
                                  + 'translations_dict - language ' + language + ' - element name '
                                  + child_widget.objectName())
        elif widget.findChildren(QtWidgets.QAction, element):
            child_widget = widget.findChildren(QtWidgets.QAction, element)[0]
            child_widget.setToolTip(translation[language])


def set_size(bytes_size):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while bytes_size >= 1024 and i < len(suffixes)-1:
        bytes_size /= 1024.
        i += 1
    f = ('%.2f' % bytes_size).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def clear_layout(layout):
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)


def get_file_name(self, action):
    logging.debug('utilities.py - get_file_name - action ' + str(action))
    file_dialog = QtWidgets.QFileDialog()
    filter_types = 'XML Files (*.xml)'
    out_file_name = None
    if action == 'save':
        # noinspection PyArgumentList
        out_file_name, _ = file_dialog.getSaveFileName(self, 'Save File', '', filter_types)
    elif action == 'open':
        # noinspection PyArgumentList
        out_file_name, _ = file_dialog.getOpenFileName(self, 'Open File', '', filter_types)
    return str(out_file_name)


def create_option_file(main_path, config_dict):
    ini_file = open(os.path.join(main_path, 'orion_ftp.ini'), 'w')
    config_dict.add_section('LOG')
    config_dict.add_section('OPTIONS')
    config_dict.add_section('INTERFACE')
    config_dict.add_section('CONNECTION')
    config_dict.add_section('TRANSFER')
    config_dict.set('LOG', 'level', 'DEBUG')
    config_dict.set('LOG', 'path', '')
    config_dict.set('OPTIONS', 'check_update', 'False')
    config_dict.set('OPTIONS', 'language', 'english')
    config_dict.set('OPTIONS', 'default_profile', '')
    config_dict.set('OPTIONS', 'local_home', '')
    config_dict.set('INTERFACE', 'local_tree_one_widget', 'False')
    config_dict.set('INTERFACE', 'remote_tree_one_widget', 'False')
    config_dict.set('INTERFACE', 'display_icons_local_tree', 'True')
    config_dict.set('INTERFACE', 'display_icons_remote_tree', 'True')
    config_dict.set('INTERFACE', 'display_path_local_tree', 'True')
    config_dict.set('INTERFACE', 'display_path_remote_tree', 'True')
    config_dict.set('CONNECTION', 'default_transfer_mode', '0')
    config_dict.set('CONNECTION', 'transfer_mode_fall_back', 'False')
    config_dict.set('CONNECTION', 'default_transfer_type', '0')
    config_dict.set('CONNECTION', 'timeout_connection', 'True')
    config_dict.set('TRANSFER', 'file_exist_download', '0')
    config_dict.write(ini_file)
    ini_file.close()


def copy_config_dict(config_dict):
    config_dict_copy = dict()
    config_dict_copy['level'] = config_dict['LOG'].get('level')
    config_dict_copy['path'] = config_dict['LOG'].get('path')
    config_dict_copy['check_update'] = config_dict['OPTIONS'].getboolean('check_update')
    config_dict_copy['language'] = config_dict['OPTIONS'].get('language')
    config_dict_copy['default_profile'] = config_dict['OPTIONS'].get('default_profile')
    config_dict_copy['local_home'] = config_dict['OPTIONS'].get('local_home')
    config_dict_copy['local_tree_one_widget'] = config_dict['INTERFACE'].getboolean('local_tree_one_widget')
    config_dict_copy['remote_tree_one_widget'] = config_dict['INTERFACE'].getboolean('remote_tree_one_widget')
    config_dict_copy['display_icons_local_tree'] = config_dict['INTERFACE'].getboolean('display_icons_local_tree')
    config_dict_copy['display_icons_remote_tree'] = config_dict['INTERFACE'].getboolean('display_icons_remote_tree')
    config_dict_copy['display_path_local_tree'] = config_dict['INTERFACE'].getboolean('display_path_local_tree')
    config_dict_copy['display_path_remote_tree'] = config_dict['INTERFACE'].getboolean('display_path_remote_tree')
    config_dict_copy['default_transfer_mode'] = config_dict['CONNECTION'].get('default_transfer_mode')
    config_dict_copy['transfer_mode_fall_back'] = config_dict['CONNECTION'].getboolean('transfer_mode_fall_back')
    config_dict_copy['default_transfer_type'] = config_dict['CONNECTION'].get('default_transfer_type')
    config_dict_copy['file_exist_download'] = config_dict['TRANSFER'].get('file_exist_download')
    return config_dict_copy


def read_translations():
    translations = {}
    file_list = os.listdir('translations/')
    logging.info('OrionFTP - read_translations - files: ' + str(len(file_list)))
    for file in file_list:
        name = file[:-4]
        f = open('translations/' + file, 'r', encoding='utf-8')
        for line in f:
            if line[:3] != '###':
                index = line.find('=')
                widget = line[:index]
                text = line[index + 1:].replace('\n', '')
                if '|' in text:
                    text = text.split('|')
                if text:
                    try:
                        existing_dict = translations[widget]
                    except KeyError:
                        existing_dict = {}
                    existing_dict[name] = text
                    translations[widget] = existing_dict
        f.close()
    return translations


def create_logging_handlers(config_dict, filename):
    log_filename = os.path.join(config_dict.get('LOG', 'path'), filename)
    logging.getLogger('').handlers = []
    logging.basicConfig(filename=log_filename,
                        level=getattr(logging, config_dict.get('LOG', 'level')),
                        filemode='w',
                        format='%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
