# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/profiletool.ui'
#
# Created: Tue Sep 25 13:06:16 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProfileTool(object):
    def setupUi(self, ProfileTool):
        ProfileTool.setObjectName(_fromUtf8("ProfileTool"))
        ProfileTool.resize(973, 332)
        ProfileTool.setWindowTitle(QtGui.QApplication.translate("ProfileTool", "Profile Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1.sizePolicy().hasHeightForWidth())
        self.tab_1.setSizePolicy(sizePolicy)
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.gridlayout = QtGui.QGridLayout(self.tab_1)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self._2 = QtGui.QHBoxLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_for_plot = QtGui.QFrame(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_for_plot.sizePolicy().hasHeightForWidth())
        self.frame_for_plot.setSizePolicy(sizePolicy)
        self.frame_for_plot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_for_plot.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_for_plot.setObjectName(_fromUtf8("frame_for_plot"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.frame_for_plot)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.gridLayout.addWidget(self.frame_for_plot, 0, 1, 1, 1)
        self.widget_save_buttons = QtGui.QWidget(self.tab_1)
        self.widget_save_buttons.setObjectName(_fromUtf8("widget_save_buttons"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_save_buttons)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.stackedWidget = QtGui.QStackedWidget(self.widget_save_buttons)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.page)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.butPrint = QtGui.QPushButton(self.page)
        self.butPrint.setText(QtGui.QApplication.translate("ProfileTool", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.butPrint.setObjectName(_fromUtf8("butPrint"))
        self.horizontalLayout_4.addWidget(self.butPrint)
        self.butPDF = QtGui.QPushButton(self.page)
        self.butPDF.setEnabled(False)
        self.butPDF.setText(QtGui.QApplication.translate("ProfileTool", "Save as PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.butPDF.setObjectName(_fromUtf8("butPDF"))
        self.horizontalLayout_4.addWidget(self.butPDF)
        self.butSVG = QtGui.QPushButton(self.page)
        self.butSVG.setEnabled(False)
        self.butSVG.setText(QtGui.QApplication.translate("ProfileTool", "Save as SVG", None, QtGui.QApplication.UnicodeUTF8))
        self.butSVG.setObjectName(_fromUtf8("butSVG"))
        self.horizontalLayout_4.addWidget(self.butSVG)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        spacerItem = QtGui.QSpacerItem(1, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtGui.QLabel(self.widget_save_buttons)
        self.label.setText(QtGui.QApplication.translate("ProfileTool", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.widget_save_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("ProfileTool", "Temp. polyline", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("ProfileTool", "Selected polyline", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_2 = QtGui.QLabel(self.widget_save_buttons)
        self.label_2.setText(QtGui.QApplication.translate("ProfileTool", "Plot library", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtGui.QComboBox(self.widget_save_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.checkBox = QtGui.QCheckBox(self.widget_save_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setText(QtGui.QApplication.translate("ProfileTool", "Full resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.gridLayout.addWidget(self.widget_save_buttons, 1, 1, 1, 1)
        self.scaleSlider = QtGui.QSlider(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleSlider.sizePolicy().hasHeightForWidth())
        self.scaleSlider.setSizePolicy(sizePolicy)
        self.scaleSlider.setOrientation(QtCore.Qt.Vertical)
        self.scaleSlider.setObjectName(_fromUtf8("scaleSlider"))
        self.gridLayout.addWidget(self.scaleSlider, 0, 0, 2, 1)
        self._2.addLayout(self.gridLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableView = QtGui.QTableView(self.tab_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(10, 10))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(10, 20))
        self.pushButton_2.setText(QtGui.QApplication.translate("ProfileTool", "Add Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.tab_1)
        self.pushButton.setMinimumSize(QtCore.QSize(10, 20))
        self.pushButton.setText(QtGui.QApplication.translate("ProfileTool", "Remove Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self._2.addLayout(self.verticalLayout)
        self.gridlayout.addLayout(self._2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1155, 255))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        ProfileTool.setWidget(self.dockWidgetContents)

        self.retranslateUi(ProfileTool)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProfileTool)

    def retranslateUi(self, ProfileTool):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("ProfileTool", "&Profile", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("ProfileTool", "Table", None, QtGui.QApplication.UnicodeUTF8))

