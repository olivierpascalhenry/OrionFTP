import logging
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
