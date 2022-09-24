# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate_uuid.ui'
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
        Form.resize(552, 435)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.num_label = QLabel(Form)
        self.num_label.setObjectName(u"num_label")

        self.horizontalLayout.addWidget(self.num_label)

        self.num_edit = QLineEdit(Form)
        self.num_edit.setObjectName(u"num_edit")

        self.horizontalLayout.addWidget(self.num_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.result_label = QLabel(Form)
        self.result_label.setObjectName(u"result_label")

        self.verticalLayout.addWidget(self.result_label)

        self.result_content = QTextBrowser(Form)
        self.result_content.setObjectName(u"result_content")

        self.verticalLayout.addWidget(self.result_content)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Generate UUID", None))
        self.num_label.setText(QCoreApplication.translate("Form", u" Num", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Uppercase", None))
        self.result_label.setText(QCoreApplication.translate("Form", u"Result", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
    # retranslateUi

