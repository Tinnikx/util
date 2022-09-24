from generated.main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from my_generate_uuid import GenerateUuid
from my_url_encoder_decoder import UrlEncoderAndDecoder
from my_timestamp import TimeStampTranslator


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionGenerate_UUID.triggered.connect(self.__create_generate_uuid_window)
        self.actionURL_Decoder_Encoder.triggered.connect(self.__create_url_encoder_decoder)
        self.actionTimeStamp_Translator.triggered.connect(self.__create_timestamp_translator)
        self.show()

    def __create_generate_uuid_window(self):
        generate_uuid = GenerateUuid()
        self.mdiArea.addSubWindow(generate_uuid)
        generate_uuid.show()

    def __create_url_encoder_decoder(self):
        encoder_decoder = UrlEncoderAndDecoder()
        self.mdiArea.addSubWindow(encoder_decoder)
        encoder_decoder.show()

    def __create_timestamp_translator(self):
        timestamp_translator = TimeStampTranslator()
        self.mdiArea.addSubWindow(timestamp_translator)
        timestamp_translator.show()
