import os
from PyQt5 import QtCore, QtWidgets, QtGui
from functions.material_functions import tree_objects_init


class MyQFileIconProvider(QtWidgets.QFileIconProvider):
    def __init__(self, display_icons):
        super(QtWidgets.QFileIconProvider, self).__init__()
        super().__init__()
        self.display_icons = display_icons
        self.file_types, self.type_icons = tree_objects_init()
    
    def icon(self, file_info):
        if file_info.isFile():
            if self.display_icons:
                if os.path.splitext(file_info.fileName())[1][1:]:
                    try:
                        iconfile = self.type_icons[self.file_types[os.path.splitext(file_info.fileName())[1][1:]]]
                    except KeyError:
                        iconfile = 'file_icon.png'
                else:
                    iconfile = 'file_icon.png'
                if not iconfile:
                    iconfile = 'file_icon.png'
                return QtGui.QIcon('icons/' + iconfile)
            else:
                return QtGui.QIcon('icons/tree_none_icon.bmp')
        if file_info.isRoot():
            if self.display_icons:
                return QtGui.QIcon('icons/hdd_icon.png')
            else:
                return QtGui.QIcon('icons/tree_none_icon.bmp')
        if file_info.isDir():
            if self.display_icons:
                return QtGui.QIcon('icons/folder_icon.png')
            else:
                return QtGui.QIcon('icons/tree_none_icon.bmp')
            
        return QtWidgets.QFileIconProvider.icon(self, file_info)


class MyQFileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, first_column, second_column, third_column):
        super(QtWidgets.QFileSystemModel, self).__init__()
        super().__init__()
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
        if isinstance(text_list, list):
            self.first_column = text_list[0]
        else:
            self.first_column = text_list
        self.headerData(0, QtCore.Qt.Horizontal, QtCore.Qt.DisplayRole)


class MyQTreeWidgetItem(QtWidgets.QTreeWidgetItem):
    def __lt__(self, other):
        if not isinstance(other, MyQTreeWidgetItem):
            return super(MyQTreeWidgetItem, self).__lt__(other)
        tree = self.treeWidget()
        if not tree:
            column = 0
        else:
            column = tree.sortColumn()
        return self.sortData(column) < other.sortData(column)

    def __init__(self, *args):
        super(MyQTreeWidgetItem, self).__init__(*args)
        self._sortData = {}

    def sortData(self, column):
        return self._sortData.get(column, self.text(column))

    def setSortData(self, column, data):
        self._sortData[column] = data


class CustomTreeItem(QtWidgets.QTreeWidgetItem):
    def __init__(self, parent, status_object, file_object, size_object, speed_object, progress_object):
        super(CustomTreeItem, self).__init__(parent)
        parent.setItemWidget(self, 0, status_object)
        parent.setItemWidget(self, 1, file_object)
        parent.setItemWidget(self, 2, size_object)
        parent.setItemWidget(self, 3, speed_object)
        parent.setItemWidget(self, 4, progress_object)
