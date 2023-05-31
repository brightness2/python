import sys
import time
from threading import Timer

from PyQt5 import QtCore, QtGui, QtWidgets
from qfluentwidgets import MessageBox
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QMessageBox

from demoui import Ui_MainWindow
from domain.autoWeb import AutoWeb
from module.test import Test

canRun = True # 利用线程共享变量的原理，来控制其他线程运行

class MyThread(QThread):
     # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal(str)
    def __init__(self,autoWeb):
        # 初始化函数
        super(MyThread,self).__init__()
        self.autoWeb = autoWeb
    def run(self):
        global canRun
        #重写线程执行的run函数
        self.autoWeb.openUrl('http://www.baidu.com')
        #触发自定义信号
        # 通过自定义信号把待显示的字符串传递给槽函数
        # for i in range(5):
        #     time.sleep(1)

        #     self.trigger.emit(str(i))
        test = Test(self.autoWeb.driver)
        test.doAction()
        # time.sleep(5)
        while canRun:
            pass
        self.autoWeb.quit()




class CloseEventWidget(QtWidgets.QMainWindow,Ui_MainWindow ):
    worker = None
    auto_web = None
    def __init__(self):
        super(CloseEventWidget, self).__init__()
        self.setupUi(self)
        self.bindevent()
        self.thread = QThread()
        
    def bindevent(self):
        self.PrimaryPushButton.clicked.connect(self.doAction)

    
    def doAction(self):
        t = Timer(5.0, self.stopRun )
        t.start()
        self.PrimaryPushButton.setEnabled(False)
        # 实例化 autoWeb
        webLocation = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        dataDir = r"C:\Users\Public\Chrome\UserData"
        self.auto_web =  AutoWeb(webLocation,dataDir)
        self.auto_web.set_chromedriver_version('113.0.5672.63')
        self.auto_web.init_driver()
        # 启动线程        
        self.worker = MyThread(self.auto_web)
        self.worker.start()
        # 线程自定义信号连接的槽函数
        self.worker.trigger.connect(self.display)
        # 线程完成信号连接的槽函数
        self.worker.finished.connect(lambda:self.PrimaryPushButton.setEnabled(True))
        # t=Thread(target=self.action,name='func_run')
        # t.start()
        # t.join()
        # self.PrimaryPushButton.setEnabled(True)

    def stopRun(self):
        print('ff')
        global canRun
        canRun = False

    def display(self,str):
        print(str)

    def closeEvent(self,event):
        # 若线程正在运行，进行提示
        if self.worker and self.worker.isRunning():
            # if self.auto_web is not None:
            #     try:
            #         # webdriver要求浏览器执行Javascript 来判断是否关闭了浏览器
            #         self.auto_web.driver.execute_script('javascript:void(0);')
            #     except:
            #         try:
            #             self.auto_web.quit()
            #             self.worker.quit()
            #         except:
            #             print('eee')
            #     finally:
            #         self.auto_web = None

            w = MessageBox('系统提示', '任务进行中,确认关闭吗', self)
            if w.exec():
                if self.auto_web:
                    self.auto_web.quit()
                event.accept()
            else:
                event.ignore()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = CloseEventWidget()
    w.show()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # ui.bindevent()
    # ui.action()
    # MainWindow.show()
    sys.exit(app.exec_())