from abc import ABCMeta,abstractmethod
from PyQt5.QtWidgets import QFrame

class BaseController(QFrame):
    __metaclass__ = ABCMeta

    _model = None
    _view = None

    def __init__(self, parentUI=None):
        super().__init__(parent=parentUI)
        self._model = self._createModel()
        self._view = self._createView()
        self._view.setupUi(self)
    # 实例化model类
    @abstractmethod
    def _createModel(self):
        raise NotImplementedError
    # 实例化视图类
    @abstractmethod
    def _createView(self):
        raise NotImplementedError
    # 绑定控件信号与槽
    @abstractmethod
    def bindEvent(self):
        raise NotImplementedError

    def run(self):
        self.bindEvent()