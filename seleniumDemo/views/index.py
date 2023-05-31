from tkinter import *
from tkinter import ttk
import time
from domain.autoWeb import *
import module.test
from views.components.first_tab import *
from common.widget import *

class GUI:
    _tabs = None
    _ui_tabs_dict = {}
    def __init__(self,win) -> None:
        self.win = win
    
    def _init_window(self):
        self.win.title('demo') #标题
        self.win.geometry('1068x681+10+10') #窗口大小

        self._tabs = ttk.Notebook(self.win)
        self._tabs.pack(fill=BOTH, expand=TRUE)

        def creat_auto_web_ui(tab_widget):
            login_view(tab_widget)
            auto_web_config_view(tab_widget)
        self.addTab('auto_web','自动上传发票PDF',creat_auto_web_ui)
        
        Button(self.win,text="获取",command=self.login).pack()

        def showCall(ui):
            ui.pack()

        lis = ListBoxtWidget(self.win,showCall)
        lis.addItem('C')
        lis.addItem('C++')
        lis.addItem('JAVA')
        lis.updateItemByValue('C++','Python')
        lis.deleteItemByValue('C')
        print(lis.getItemIndex('JAVA'))
        print(list(lis.getAllItems()))
        print(lis.getItemIndex('C++'))


    def index(self):
        print('index')

    # 添加tabs页 widgetFun是创建TKinter 组件方法
    def addTab(self,name,text,widgetFun):
        #Tab Widget
        self._ui_tabs_dict[name] = BaseWidget(ui=ttk.Frame(self._tabs))
        self._tabs.add(self._ui_tabs_dict[name].ui, text=text)
        #adding widget to Tab
        widgetFun(self._ui_tabs_dict[name])


        


    def login(self):
        print('login')
        print('username:'+self._ui_tabs_dict['auto_web'].getChild('username_input').getVaule())
        print('password:'+self._ui_tabs_dict['auto_web'].getChild('password_input').getVaule())
        print('pdf dir:'+self._ui_tabs_dict['auto_web'].getChild('pdf_dir_input').getVaule())
        # print(self._ui_tabs_dict['auto_web'].children['username_input'].ui.get())
        # autoweb_obj = AutoWeb(chrome_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",data_dir = r'C:\Users\Public\Chrome\UserData')

        # autoweb_obj.set_chromedriver_version('113.0.5672.63')

        # autoweb_obj.init_driver()

        # autoweb_obj.openUrl('https://www.baidu.com')

    def search(self):
        print('search')
        # testObj = module.test.Test(auto.driver)
        # testObj.doAction()
#
def gui_start():
    win = Tk()
    guiObj = GUI(win)
    guiObj._init_window()
    win.mainloop()