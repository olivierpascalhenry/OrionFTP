import os
import logging
from PyQt5 import QtCore, QtWidgets, QtGui
from functions.material_functions import tree_objects_init


class MyQFileIconProvider(QtWidgets.QFileIconProvider):
    def __init__(self, display_icons):
        logging.info('gui_elements.py - MyQFileIconProvider - __init__')
        super(QtWidgets.QFileIconProvider, self).__init__()
        self.display_icons = display_icons
        tree_objects_init(self)
    
    def icon(self, fileInfo):
        if fileInfo.isFile():
            if self.display_icons:
                if os.path.splitext(fileInfo.fileName())[1][1:]:
                    try:
                        iconfile = self.type_icons[self.file_types[os.path.splitext(fileInfo.fileName())[1][1:]]]
                    except KeyError:
                        iconfile = 'file_icon.png'
                else:
                    iconfile = 'file_icon.png'
                if not iconfile:
                    iconfile = 'file_icon.png'
                return QtGui.QIcon('icons/' + iconfile)
            else:
                return QtGui.QIcon('icons/tree_none_icon.bmp')
        if fileInfo.isRoot():
            if self.display_icons:
                return QtGui.QIcon('icons/hdd_icon.png')
            else:
                return QtGui.QIcon('icons/tree_none_icon.bmp')
        if fileInfo.isDir():
            if self.display_icons:
                return QtGui.QIcon('icons/folder_icon.png')
            else:
                return QtGui.QIcon('icons/tree_none_icon.bmp')
            
        return QtWidgets.QFileIconProvider.icon(self, fileInfo)


class MyQFileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, first_column, second_column, third_column):
        logging.info('gui_elements.py - MyQFileSystemModel - __init__')
        super(QtWidgets.QFileSystemModel, self).__init__()
        self.first_column = first_column
        self.second_column = second_column
        self.third_column = third_column
    
    def headerData(self, section, orientation, role):
        if section == 0 and role == QtCore.Qt.DisplayRole:
            return self.first_column
        elif section == 1 and role == QtCore.Qt.DisplayRole:
            return self.second_column
        elif section == 2 and role == QtCore.Qt.DisplayRole:
            return self.third_column
        else:
            return super(QtWidgets.QFileSystemModel, self).headerData(section, orientation, role)
    
    def setText(self, text_list):
        self.text = text_list[0]
        self.headerData(0, QtCore.Qt.Horizontal, QtCore.Qt.DisplayRole)


class MyQTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __lt__(self, other):
        if (not isinstance(other, MyQTreeWidgetItem)):
            return super(MyQTreeWidgetItem, self).__lt__(other)
        tree = self.treeWidget()
        if (not tree):
            column = 0
        else:
            column = tree.sortColumn()
        return self.sortData(column) < other.sortData(column)

    def __init__(self, *args):
        logging.info('gui_elements.py - MyQTreeWidgetItem - __init__')
        super(MyQTreeWidgetItem, self).__init__(*args)
        self._sortData = {}

    def sortData(self, column):
        return self._sortData.get(column, self.text(column))

    def setSortData(self, column, data):
        self._sortData[column] = data

