import logging
from PyQt5 import QtWidgets, QtGui, QtCore
    
    
def translate_elements(widget, language, translations_dict):
    logging.debug('utilities.py - translate_elements - language ' + language)
    for element, translation in translations_dict.items():
        if widget.objectName() == element:
            widget.setWindowTitle(translation[language])
        elif widget.findChildren(QtWidgets.QWidget, element):
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
                if 'info' in element:
                    pass
                else:
                    child_widget.setText(translation[language])
            elif isinstance(child_widget, QtWidgets.QComboBox):
                if child_widget.count() == 1:
                    child_widget.clear()
                    child_widget.addItem(translation[language])
            elif isinstance(child_widget, QtWidgets.QTextBrowser):
                child_widget.setHtml(translation[language])
            elif isinstance(child_widget, QtWidgets.QCheckBox):
                child_widget.setText(translation[language])
        elif widget.findChildren(QtWidgets.QAction, element):
            child_widget = widget.findChildren(QtWidgets.QAction, element)[0]
            child_widget.setToolTip(translation[language])


def set_size(bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while bytes >= 1024 and i < len(suffixes)-1:
            bytes /= 1024.
            i += 1
        f = ('%.2f' % bytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])


def clear_layout(layout):
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)