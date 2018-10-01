from PyQt5 import QtCore, QtWidgets, QtGui

class MyQFileIconProvider(QtWidgets.QFileIconProvider):
    def icon(self, fileInfo):

        if fileInfo.isRoot():
            return QtGui.QIcon('icons/hdd_icon.png') 
        
        if fileInfo.isDir():
            return QtGui.QIcon('icons/folder_icon.png')
        
        return QtWidgets.QFileIconProvider.icon(self, fileInfo)


class MyQFileSystemModel(QtWidgets.QFileSystemModel):
    def __init__(self, text):
        super(QtWidgets.QFileSystemModel, self).__init__()
        self.text = text
    
    def headerData(self, section, orientation, role):
        if section == 0 and role == QtCore.Qt.DisplayRole:
            return self.text
        else:
            return super(QtWidgets.QFileSystemModel, self).headerData(section, orientation, role)
