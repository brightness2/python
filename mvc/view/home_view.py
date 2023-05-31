from PyQt5 import QtCore
from qfluentwidgets import PushButton

from core.base_view import BaseView

class HomeView(BaseView):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.PushButton = PushButton(Form)
        self.PushButton.setGeometry(QtCore.QRect(110, 120, 102, 32))
        self.PushButton.setObjectName("PushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.PushButton.setText(_translate("Form", "按钮"))