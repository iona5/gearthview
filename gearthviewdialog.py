# -*- coding: utf-8 -*-
"""
/***************************************************************************
 gearthviewDialog
                                 A QGIS plugin
 GEarth View
                             -------------------
        begin                : 2012-12-14
        copyright            : (C) 2012 by geodrinx
        email                : geodrinx@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt5 import QtCore, QtGui
#from ui_gearthview import Ui_gearthview
# create the dialog for zoom to point


class gearthviewDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
#        self.ui = Ui_gearthview()
#        self.ui.setupUi(self)
