# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timestamp.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(840, 502)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(200, 0))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_2)

        self.timezone = QLineEdit(Form)
        self.timezone.setObjectName(u"timezone")

        self.horizontalLayout_6.addWidget(self.timezone)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.currentTime = QLineEdit(Form)
        self.currentTime.setObjectName(u"currentTime")
        self.currentTime.setMinimumSize(QSize(300, 0))
        self.currentTime.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.currentTime)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.currentTimeStamp = QLineEdit(Form)
        self.currentTimeStamp.setObjectName(u"currentTimeStamp")
        self.currentTimeStamp.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.currentTimeStamp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(110, 0))

        self.horizontalLayout.addWidget(self.label)

        self.inputZone = QLineEdit(Form)
        self.inputZone.setObjectName(u"inputZone")

        self.horizontalLayout.addWidget(self.inputZone)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.timeFormat = QLineEdit(Form)
        self.timeFormat.setObjectName(u"timeFormat")

        self.horizontalLayout_3.addWidget(self.timeFormat)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.resultZone = QTextEdit(Form)
        self.resultZone.setObjectName(u"resultZone")
        self.resultZone.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.resultZone)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.comboBox)

        self.translate2 = QPushButton(Form)
        self.translate2.setObjectName(u"translate2")

        self.horizontalLayout_7.addWidget(self.translate2)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.comboBox_2)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Timestamp", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"timezone", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"current time", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"currentTimestamp", None))
        self.label.setText(QCoreApplication.translate("Form", u"TimeOrTimeStamp", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"format", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Translate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"result", None))
        self.translate2.setText(QCoreApplication.translate("Form", u"Translate", None))
    # retranslateUi

