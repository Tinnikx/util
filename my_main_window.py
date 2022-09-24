from generated.main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from my_generate_uuid import GenerateUuid
from my_url_encoder_decoder import UrlEncoderAndDecoder


class MyMainWindow(QMainWindow, Ui_MainWindow):

    WINDOWS = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionGenerate_UUID.triggered.connect(self.__create_generate_uuid_window)
        self.actionURL_Decoder_Encoder.triggered.connect(self.__create_url_encoder_decoder)
        self.show()

    def __create_generate_uuid_window(self):
        generate_uuid = GenerateUuid()
        self.WINDOWS.append(generate_uuid)
        self.mdiArea.addSubWindow(generate_uuid)
        generate_uuid.show()

    def __create_url_encoder_decoder(self):
        encoder_decoder = UrlEncoderAndDecoder()
        self.WINDOWS.append(encoder_decoder)
        self.mdiArea.addSubWindow(encoder_decoder)
        encoder_decoder.show()
