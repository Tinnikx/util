from datetime import datetime

import pytz
from PySide6.QtCore import QTimer, Qt, QTimeZone, Slot
from PySide6.QtWidgets import QWidget, QDialog, QVBoxLayout, QPushButton, QLabel

from generated.timestamp import Ui_Form


class InputErrorDialog(QDialog):

    def __init__(self, parent: QWidget = None, text=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel(text)
        button2 = QPushButton('Got it!')
        layout.addWidget(label)
        layout.addWidget(button2)
        button2.clicked.connect(self.close)
        self.setLayout(layout)


class TimeStampTranslator(Ui_Form, QWidget):
    DEFAULT_FORMAT = '%Y-%m-%d %H:%M:%S'
    DEFAULT_TIMEZONE = bytearray(QTimeZone.systemTimeZoneId()).decode('utf8')

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timezone.setAlignment(Qt.AlignRight)
        self.currentTime.setAlignment(Qt.AlignRight)
        self.currentTimeStamp.setAlignment(Qt.AlignRight)
        self.inputZone.setAlignment(Qt.AlignRight)
        self.timeFormat.setAlignment(Qt.AlignRight)
        self.timeFormat.setReadOnly(True)
        self.timeFormat.setText("yyyy-MM-dd hh:mm:ss")

        self.timezone.setPlaceholderText(self.DEFAULT_TIMEZONE)
        self.timezone.setText(self.DEFAULT_TIMEZONE)
        self.timezone.editingFinished.connect(self.__check_timezone)
        self.timezone_check_status = True
        self.currentTimeZone = pytz.timezone(self.timezone.text())

        self.currentTimeTimer = QTimer()
        self.currentTimeTimer.timeout.connect(self.__timer_timeout)
        self.currentTimeTimer.start(1000)
        self.currentTime.textChanged.connect(self.__current_time_changed)
        self.currentTime.setAlignment(Qt.AlignRight)
        self.pushButton.clicked.connect(self.__translate)

        self.lineEdit.setPlaceholderText("Please input Time")
        self.comboBox.addItems(pytz.all_timezones)
        self.lineEdit_2.setPlaceholderText("Result")
        self.comboBox_2.addItems(pytz.all_timezones)
        self.translate2.clicked.connect(self.__translate_to_another_locale)

    def __translate_to_another_locale(self):
        source_timezone = self.comboBox.currentText()
        target_timezone = self.comboBox_2.currentText()
        result_time_str = pytz.timezone(source_timezone)\
            .localize(datetime.strptime(self.lineEdit.text(), self.DEFAULT_FORMAT))\
            .astimezone(pytz.timezone(target_timezone)).strftime(self.DEFAULT_FORMAT)
        self.lineEdit_2.setText(result_time_str)

    @Slot()
    def __check_timezone(self):
        current_timezone_str = self.timezone.text()
        if current_timezone_str in pytz.all_timezones:
            self.timezone_check_status = True
            self.currentTimeZone = pytz.timezone(current_timezone_str)
        else:
            self.timezone_check_status = False
            dialog = InputErrorDialog(self, text='Invalid timezone')
            dialog.exec_()

    @Slot()
    def __timer_timeout(self):
        if self.timezone_check_status:
            datetime.now(tz=self.currentTimeZone).strftime(self.DEFAULT_FORMAT)
            self.currentTime.setText(datetime.now(tz=self.currentTimeZone).strftime(self.DEFAULT_FORMAT))

    @Slot()
    def __current_time_changed(self):
        self.currentTimeStamp.setText(self.__generate_timestamp(self.currentTime.text()))

    @Slot()
    def __translate(self):
        if not self.timezone_check_status:
            self.resultZone.setText("Please input a valid timezone")
            return
        input_value = self.inputZone.text()
        if not input_value:
            return
        try:
            self.resultZone.setText(datetime.fromtimestamp(float(int(input_value) / 1000),
                                                           tz=self.currentTimeZone).strftime(self.DEFAULT_FORMAT))
        except ValueError:
            try:
                self.resultZone.setText(self.__generate_timestamp(input_value))
            except ValueError:
                self.resultZone.setText("Error while Translate, Please check the input")
        except BaseException:
            self.resultZone.setText("Error while Translate, Please check the input")

    def __generate_timestamp(self, date_str: str):
        return str(int(self.currentTimeZone
                       .localize(datetime.strptime(date_str, self.DEFAULT_FORMAT)).timestamp() * 1000))
