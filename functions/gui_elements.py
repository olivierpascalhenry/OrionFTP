import os
import math
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


class QtWaitingSpinner(QtWidgets.QWidget):
    """
    The MIT License (MIT)

    Copyright (c) 2012-2014 Alexander Turkin
    Copyright (c) 2014 William Hallatt
    Copyright (c) 2015 Jacob Dawid
    Copyright (c) 2016 Luca Weiss

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    def __init__(self, parent, centerOnParent=True, disableParentWhenSpinning=False, modality=QtCore.Qt.NonModal):
        super().__init__(parent)

        self._centerOnParent = centerOnParent
        self._disableParentWhenSpinning = disableParentWhenSpinning

        # WAS IN initialize()
        self._color = QtGui.QColor(QtCore.Qt.black)
        self._roundness = 100.0
        self._minimumTrailOpacity = 3.14159265358979323846
        self._trailFadePercentage = 80.0
        self._revolutionsPerSecond = 1.57079632679489661923
        self._numberOfLines = 20
        self._lineLength = 10
        self._lineWidth = 2
        self._innerRadius = 10
        self._currentCounter = 0
        self._isSpinning = False

        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.rotate)
        self.updateSize()
        self.updateTimer()
        self.hide()
        # END initialize()

        self.setWindowModality(modality)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def paintEvent(self, QPaintEvent):
        self.updatePosition()
        painter = QtGui.QPainter(self)
        painter.fillRect(self.rect(), QtCore.Qt.transparent)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        if self._currentCounter >= self._numberOfLines:
            self._currentCounter = 0

        painter.setPen(QtCore.Qt.NoPen)
        for i in range(0, self._numberOfLines):
            painter.save()
            painter.translate(self._innerRadius + self._lineLength, self._innerRadius + self._lineLength)
            rotateAngle = float(360 * i) / float(self._numberOfLines)
            painter.rotate(rotateAngle)
            painter.translate(self._innerRadius, 0)
            distance = self.lineCountDistanceFromPrimary(i, self._currentCounter, self._numberOfLines)
            color = self.currentLineColor(distance, self._numberOfLines, self._trailFadePercentage,
                                          self._minimumTrailOpacity, self._color)
            painter.setBrush(color)
            painter.drawRoundedRect(QtCore.QRect(0, -self._lineWidth / 2, self._lineLength, self._lineWidth), self._roundness,
                                    self._roundness, QtCore.Qt.RelativeSize)
            painter.restore()

    def start(self):
        self.updatePosition()
        self._isSpinning = True
        self.show()

        if self.parentWidget and self._disableParentWhenSpinning:
            self.parentWidget().setEnabled(False)

        if not self._timer.isActive():
            self._timer.start()
            self._currentCounter = 0

    def stop(self):
        self._isSpinning = False
        self.hide()

        if self.parentWidget() and self._disableParentWhenSpinning:
            self.parentWidget().setEnabled(True)

        if self._timer.isActive():
            self._timer.stop()
            self._currentCounter = 0

    def setNumberOfLines(self, lines):
        self._numberOfLines = lines
        self._currentCounter = 0
        self.updateTimer()

    def setLineLength(self, length):
        self._lineLength = length
        self.updateSize()

    def setLineWidth(self, width):
        self._lineWidth = width
        self.updateSize()

    def setInnerRadius(self, radius):
        self._innerRadius = radius
        self.updateSize()

    def color(self):
        return self._color

    def roundness(self):
        return self._roundness

    def minimumTrailOpacity(self):
        return self._minimumTrailOpacity

    def trailFadePercentage(self):
        return self._trailFadePercentage

    def revolutionsPersSecond(self):
        return self._revolutionsPerSecond

    def numberOfLines(self):
        return self._numberOfLines

    def lineLength(self):
        return self._lineLength

    def lineWidth(self):
        return self._lineWidth

    def innerRadius(self):
        return self._innerRadius

    def isSpinning(self):
        return self._isSpinning

    def setRoundness(self, roundness):
        self._roundness = max(0.0, min(100.0, roundness))

    def setColor(self, color=QtCore.Qt.black):
        self._color = QtGui.QColor(color)

    def setRevolutionsPerSecond(self, revolutionsPerSecond):
        self._revolutionsPerSecond = revolutionsPerSecond
        self.updateTimer()

    def setTrailFadePercentage(self, trail):
        self._trailFadePercentage = trail

    def setMinimumTrailOpacity(self, minimumTrailOpacity):
        self._minimumTrailOpacity = minimumTrailOpacity

    def rotate(self):
        self._currentCounter += 1
        if self._currentCounter >= self._numberOfLines:
            self._currentCounter = 0
        self.update()

    def updateSize(self):
        size = (self._innerRadius + self._lineLength) * 2
        self.setFixedSize(size, size)

    def updateTimer(self):
        self._timer.setInterval(1000 / (self._numberOfLines * self._revolutionsPerSecond))

    def updatePosition(self):
        if self.parentWidget() and self._centerOnParent:
            self.move(self.parentWidget().width() / 2 - self.width() / 2,
                      self.parentWidget().height() / 2 - self.height() / 2)

    def lineCountDistanceFromPrimary(self, current, primary, totalNrOfLines):
        distance = primary - current
        if distance < 0:
            distance += totalNrOfLines
        return distance

    def currentLineColor(self, countDistance, totalNrOfLines, trailFadePerc, minOpacity, colorinput):
        color = QtGui.QColor(colorinput)
        if countDistance == 0:
            return color
        minAlphaF = minOpacity / 100.0
        distanceThreshold = int(math.ceil((totalNrOfLines - 1) * trailFadePerc / 100.0))
        if countDistance > distanceThreshold:
            color.setAlphaF(minAlphaF)
        else:
            alphaDiff = color.alphaF() - minAlphaF
            gradient = alphaDiff / float(distanceThreshold + 1)
            resultAlpha = color.alphaF() - gradient * countDistance
            # If alpha is out of bounds, clip it.
            resultAlpha = min(1.0, max(0.0, resultAlpha))
            color.setAlphaF(resultAlpha)
        return color