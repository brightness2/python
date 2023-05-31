from abc import ABC,abstractmethod
class BaseView(ABC):
    @abstractmethod
    def setupUi(self):
        pass

    @abstractmethod
    def retranslateUi(self):
        pass