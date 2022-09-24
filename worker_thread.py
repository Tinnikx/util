from PySide6.QtCore import QThread


class WorkerThread(QThread):

    def __init__(self, func, signal, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.signal = signal
        self.kwargs = kwargs

    def run(self) -> None:
        result = self.func(*self.args, **self.kwargs)
        self.signal.emit(result)
