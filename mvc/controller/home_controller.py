from core.base_controller import BaseController

from model.home_model import HomeModel
from view.home_view import HomeView

class HomeController(BaseController):

    def _createModel(self):
        return HomeModel()

    def _createView(self):
        return HomeView()

    def bindEvent(self):
        self._view.PushButton.clicked.connect(self.btn_click)

    def btn_click(self):
        print('btn clicked ...')