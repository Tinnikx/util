import uuid

from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget

from generated.generate_uuid import Ui_Form
from worker_thread import WorkerThread


class GenerateUuid(Ui_Form, QWidget):

    generate_signal = Signal(list)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.num_edit.setValidator(QIntValidator())
        self.pushButton.clicked.connect(self.__generate_in_worker)
        self.generate_signal.connect(self.resolve_generate_process)

    @Slot(list)
    def resolve_generate_process(self, result):
        self.result_content.clear()
        for text in result:
            self.result_content.append(text)

    def __generate_in_worker(self):
        self.worker_thread = WorkerThread(self.__generate, self.generate_signal)
        self.worker_thread.start()

    def __generate(self):
        num = int(self.num_edit.text() or 0)
        if self.checkBox.isChecked():
            result = [str(uuid.uuid1()).upper() for _ in range(num)]
        else:
            result = [str(uuid.uuid1()) for _ in range(num)]
        return result
