# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'url_encoder_decoder.ui'
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
        Form.resize(579, 480)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.encode_zone = QTextEdit(Form)
        self.encode_zone.setObjectName(u"encode_zone")

        self.verticalLayout.addWidget(self.encode_zone)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_encode = QPushButton(Form)
        self.bt_encode.setObjectName(u"bt_encode")

        self.horizontalLayout.addWidget(self.bt_encode)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.bt_decode = QPushButton(Form)
        self.bt_decode.setObjectName(u"bt_decode")

        self.horizontalLayout.addWidget(self.bt_decode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.decode_zone = QTextEdit(Form)
        self.decode_zone.setObjectName(u"decode_zone")

        self.verticalLayout.addWidget(self.decode_zone)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"URL Encoder/Decoder", None))
        self.bt_encode.setText(QCoreApplication.translate("Form", u"Encode", None))
        self.bt_decode.setText(QCoreApplication.translate("Form", u"Decode", None))
    # retranslateUi

