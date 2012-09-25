# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
# Profile
# Copyright (C) 2012  Patrice Verchere
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, print to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from profiletool import Ui_ProfileTool
from ..tools.plottingtool import *
#from ..profileplugin import ProfilePlugin

try:
	from PyQt4.Qwt5 import *
	Qwt5_loaded = True
except ImportError:
	Qwt5_loaded = False 
try:
	from matplotlib import *
	import matplotlib
	matplotlib_loaded = True
except ImportError:
	matplotlib_loaded = False 

import platform


class Ui_PTDockWidget(QDockWidget,Ui_ProfileTool):



	TITLE = "MirrorMap"

	def __init__(self, parent, iface1, mdl1):
		QDockWidget.__init__(self, parent)
		self.setAttribute(Qt.WA_DeleteOnClose)

		#self.mainWidget = MirrorMap(self, iface)
		self.location = Qt.RightDockWidgetArea
		self.iface = iface1

		self.setupUi(self)
		#self.connect(self, SIGNAL("dockLocationChanged(Qt::DockWidgetArea)"), self.setLocation)
		self.mdl = mdl1
		#self.showed = False

	def showIt(self):
		#self.setLocation( Qt.BottomDockWidgetArea )
		self.location = Qt.BottomDockWidgetArea
		minsize = self.minimumSize()
		maxsize = self.maximumSize()
		self.setMinimumSize(minsize)
		self.setMaximumSize(maxsize)
		self.iface.mapCanvas().setRenderFlag(False)

		#TableWiew thing
		self.tableView.setModel(self.mdl)
		self.tableView.setColumnWidth(0, 20)
		self.tableView.setColumnWidth(1, 20)
		self.tableView.setColumnWidth(2, 150)
		hh = self.tableView.horizontalHeader()
		hh.setStretchLastSection(True)
		self.tableView.setColumnHidden(4 , True)
		self.mdl.setHorizontalHeaderLabels(["","","Layer","Band"])
		#self.checkBox.setEnabled(False)
		
		#The ploting area
		self.plotWdg = None
		#Draw the widget
		self.iface.addDockWidget(self.location, self)
		self.iface.mapCanvas().setRenderFlag(True)
		
		
	def addOptionComboboxItems(self):
		self.comboBox.addItem("Temporary polyline")
		self.comboBox.addItem("Selected polyline")
		if Qwt5_loaded:
			self.comboBox_2.addItem("Qwt5")
		if matplotlib_loaded:
			self.comboBox_2.addItem("Matplotlib")						



	def closeEvent(self, event):
		self.emit( SIGNAL( "closed(PyQt_PyObject)" ), self )
                QObject.disconnect(self.butPrint, SIGNAL("clicked()"), self.outPrint)
                QObject.disconnect(self.butPDF, SIGNAL("clicked()"), self.outPDF)
                QObject.disconnect(self.butSVG, SIGNAL("clicked()"), self.outSVG)
		return QDockWidget.closeEvent(self, event)


	def addPlotWidget(self, library):
		layout = self.frame_for_plot.layout()
		while layout.count():
                        child = layout.takeAt(0)
                        child.widget().deleteLater()
		if library == "Qwt5":
                        self.widget_save_buttons.setVisible( True )
			self.plotWdg = PlottingTool().changePlotWidget("Qwt5", self.frame_for_plot)
			layout.addWidget(self.plotWdg)
						
			if QT_VERSION >= 0X040100:
				self.butPDF.setEnabled(True)
			if QT_VERSION >= 0X040300:
				self.butSVG.setEnabled(True)

			QObject.connect(self.butPrint, SIGNAL("clicked()"), self.outPrint)
                        QObject.connect(self.butPDF, SIGNAL("clicked()"), self.outPDF)
                        QObject.connect(self.butSVG, SIGNAL("clicked()"), self.outSVG)
                                
		elif library == "Matplotlib":
                        self.widget_save_buttons.setVisible( False )
			self.plotWdg = PlottingTool().changePlotWidget("Matplotlib", self.frame_for_plot)
			layout.addWidget(self.plotWdg)
			mpltoolbar = matplotlib.backends.backend_qt4agg.NavigationToolbar2QTAgg(self.plotWdg, self.frame_for_plot)
			layout.addWidget( mpltoolbar )
			lstActions = mpltoolbar.actions()
			mpltoolbar.removeAction( lstActions[ 7 ] )
			mpltoolbar.removeAction( lstActions[ 8 ] )


	def outPrint(self): # Postscript file rendering doesn't work properly yet.
		PlottingTool().outPrint(self.iface, self, self.mdl, self.comboBox_2.currentText ())
		
	def outPDF(self):
		PlottingTool().outPDF(self.iface, self, self.mdl, self.comboBox_2.currentText ())

	def outSVG(self):
		PlottingTool().outSVG(self.iface, self, self.mdl, self.comboBox_2.currentText ())		

	def outPNG(self):
		PlottingTool().outPNG(self.iface, self, self.mdl, self.comboBox_2.currentText ())		

