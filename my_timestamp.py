from PySide6.QtCore import QTimer, Qt, QDateTime, QTimeZone, QByteArray
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
    DEFAULT_FORMAT = 'yyyy-MM-ddThh:mm:ssZ'
    DEFAULT_TIMEZONE = bytearray(QTimeZone.systemTimeZoneId()).decode('utf8')

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timezone.setAlignment(Qt.AlignRight)
        self.currentTime.setAlignment(Qt.AlignRight)
        self.currentTimeStamp.setAlignment(Qt.AlignRight)
        self.inputZone.setAlignment(Qt.AlignRight)
        self.timeFormat.setAlignment(Qt.AlignRight)

        self.timezone.setPlaceholderText(self.DEFAULT_TIMEZONE)
        self.timezone.setText(self.DEFAULT_TIMEZONE)
        self.timezone.editingFinished.connect(self.__check_timezone)
        self.timezone_check_status = True
        self.inputTimezone = QTimeZone(QByteArray(self.DEFAULT_TIMEZONE.encode('utf8')))

        self.currentTimeTimer = QTimer()
        self.currentTimeTimer.timeout.connect(self.__timer_timeout)
        self.currentTimeTimer.start(1000)
        self.currentTime.textChanged.connect(self.__current_time_changed)
        self.currentTime.setAlignment(Qt.AlignRight)
        self.timeFormat.setPlaceholderText(self.DEFAULT_FORMAT)
        self.timeFormat.setText(self.DEFAULT_FORMAT)
        self.pushButton.clicked.connect(self.__translate)

    def __check_timezone(self):
        if self.timezone.text() in QTimeZone.availableTimeZoneIds():
            self.timezone_check_status = True
            self.inputTimezone = QTimeZone(QByteArray(self.timezone.text().encode('utf8')))
        else:
            self.timezone_check_status = False
            dialog = InputErrorDialog(self, text='Invalid timezone')
            dialog.exec_()

    def __timer_timeout(self):
        if self.timezone_check_status:
            time = QDateTime.currentDateTime().toTimeZone(self.inputTimezone)
            self.currentTime.setText(time.toString('yyyy-MM-ddThh:mm:ssZ'))

    def __current_time_changed(self):
        time = QDateTime.fromString(self.currentTime.text(), 'yyyy-MM-ddThh:mm:ssZ')
        self.currentTimeStamp.setText(str(time.toMSecsSinceEpoch()))

    def __translate(self):
        if not self.timezone_check_status:
            self.resultZone.setText("Please input a valid timezone")
            return
        custom_format = self.timeFormat.text() or self.DEFAULT_FORMAT
        input_value = self.inputZone.text()
        if not input_value:
            return
        try:
            value = int(input_value)
            self.resultZone.setText(QDateTime.fromMSecsSinceEpoch(value).toTimeZone(self.inputTimezone).toString(custom_format))
        except ValueError:
            timestamp = QDateTime.fromString(input_value, custom_format).toTimeZone(self.inputTimezone).toMSecsSinceEpoch()
            if timestamp < 0:
                self.resultZone.setText("Error while Translate, Please check the input and the format")
            else:
                self.resultZone.setText(str(QDateTime.fromString(input_value, custom_format).toMSecsSinceEpoch()))
