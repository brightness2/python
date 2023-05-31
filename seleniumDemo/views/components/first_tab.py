import tkinter
from tkinter import *
from common.widget import BaseWidget
import common.utils as Utils
# 账号密码控件
def login_view(tab_widget):
    tab_frame = tab_widget.ui
    # username label
    username_label_widget = BaseWidget()
    username_label_widget.ui = Label(tab_frame,text="用户名:")
    username_label_widget.ui.grid(row=0,column=0,padx='4px',pady='4px',sticky='w')
    tab_widget.setChild('username_label',username_label_widget)
    # username input
    username_input_widget = BaseWidget()
    username_input_widget.ui = Entry(tab_frame)
    username_input_widget.ui.grid(row=0,column=1,padx=1,pady=1)
    tab_widget.setChild('username_input',username_input_widget)
    # password label
    password_label_widget = BaseWidget()
    password_label_widget.ui = Label(tab_frame,text="密码:")
    password_label_widget.ui.grid(row=1,column=0,padx='4px',pady='4px',sticky='w')
    tab_widget.setChild('password_label',password_label_widget)
    # password input
    password_input_widget = BaseWidget()
    password_input_widget.ui = Entry(tab_frame)
    password_input_widget.ui.grid(row=1,column=1)
    tab_widget.setChild('password_input',password_input_widget)

# auto_web 配置相关控件
def auto_web_config_view(tab_widget):
    tab_frame = tab_widget.ui
    # chrome_driver label
    chrome_driver_label_widget = BaseWidget()
    chrome_driver_label_widget.ui = Label(tab_frame,text="chrome driver版本:")
    chrome_driver_label_widget.ui.grid(row=0,column=3,padx='20px',pady='4px',sticky='w')
    tab_widget.setChild('chrome_driver_label',chrome_driver_label_widget)
    # chrome_driver input
    chrome_driver_input_widget = BaseWidget()
    chrome_driver_input_widget.ui = Entry(tab_frame)
    chrome_driver_input_widget.ui.insert(0,'113.0.5672.63') #默认值
    chrome_driver_input_widget.ui.grid(row=0,column=4)
    tab_widget.setChild('chrome_driver_input',chrome_driver_input_widget)
    # pdf_dir label
    paf_dir_label_widget = BaseWidget()
    paf_dir_label_widget.ui = Label(tab_frame,text="PDF所在文件夹:")
    paf_dir_label_widget.ui.grid(row=0,column=6,padx='20px',pady='4px',sticky='w')
    tab_widget.setChild('paf_dir_label',paf_dir_label_widget)
    # pdf_dir_input 
    pdf_dir_input_widget = BaseWidget()
    pdf_dir_input_widget.ui = Entry(tab_frame,width=40)
    pdf_dir_input_widget.ui.grid(row=0,column=7)
    tab_widget.setChild('pdf_dir_input',pdf_dir_input_widget)
    # open_pdf_dir_btn
    open_pdf_dir_btn_widget = BaseWidget()

    def openDir():
        pdf_dir_input_widget.setValue(Utils.openDir())

    open_pdf_dir_btn_widget.ui = Button(tab_frame,text="选择文件夹",command=openDir)
    open_pdf_dir_btn_widget.ui.grid(row=0,column=8,padx='2px')

