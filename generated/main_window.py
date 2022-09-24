# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 597)
        self.actionGenerate_UUID = QAction(MainWindow)
        self.actionGenerate_UUID.setObjectName(u"actionGenerate_UUID")
        self.actionURL_Decoder_Encoder = QAction(MainWindow)
        self.actionURL_Decoder_Encoder.setObjectName(u"actionURL_Decoder_Encoder")
        self.actionTimeStamp_Translator = QAction(MainWindow)
        self.actionTimeStamp_Translator.setObjectName(u"actionTimeStamp_Translator")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.horizontalLayout.addWidget(self.mdiArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 23))
        self.menuWindows = QMenu(self.menubar)
        self.menuWindows.setObjectName(u"menuWindows")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuWindows.menuAction())
        self.menuWindows.addAction(self.actionGenerate_UUID)
        self.menuWindows.addAction(self.actionURL_Decoder_Encoder)
        self.menuWindows.addAction(self.actionTimeStamp_Translator)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Utils", None))
        self.actionGenerate_UUID.setText(QCoreApplication.translate("MainWindow", u"Generate UUID", None))
        self.actionURL_Decoder_Encoder.setText(QCoreApplication.translate("MainWindow", u"URL Decoder/Encoder", None))
        self.actionTimeStamp_Translator.setText(QCoreApplication.translate("MainWindow", u"TimeStamp Translator", None))
        self.menuWindows.setTitle(QCoreApplication.translate("MainWindow", u"Windows", None))
    # retranslateUi

