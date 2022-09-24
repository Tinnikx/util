from generated.url_encoder_decoder import Ui_Form
from PySide6.QtWidgets import QWidget
from urllib import request, parse


class UrlEncoderAndDecoder(Ui_Form, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bt_encode.clicked.connect(self.__encode)
        self.bt_decode.clicked.connect(self.__decode)

    def __encode(self):
        # TODO 编码有问题
        content = self.encode_zone.toPlainText()
        if content:
            self.decode_zone.clear()
            self.decode_zone.setText(parse.quote(content, safe='/:;=?&'.encode('utf8'), encoding='utf8'))

    def __decode(self):
        content = self.decode_zone.toPlainText()
        if content:
            self.encode_zone.clear()
            self.encode_zone.setText(parse.unquote(content, encoding='utf8'))
