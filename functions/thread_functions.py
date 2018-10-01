import os
import logging
from functions.material_functions import tree_objects_init
from functions.utilities import set_size
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
        

class FindFilesAndPopulate(Qt.QThread):
    def __init__(self, path, widget):
        Qt.QThread.__init__(self)
        self.path = path
        self.widget = widget
        tree_objects_init(self)
        
    def run(self):
        for filename in next(os.walk(self.path))[2]: 
            filepath = self.path + '/' + filename
            filesize = set_size(os.path.getsize(filepath))
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
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('icons/' + iconfile), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = QtWidgets.QTreeWidgetItem()
            item.setText(0, filename)
            item.setText(1, filesize)
            item.setText(2, filetype)
            item.setIcon(0, icon)
            self.widget.addTopLevelItem(item)
    
    def stop(self):
        self.terminate()

