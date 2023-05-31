from tkinter import *

class BaseWidget:
    _children = {} #子级
    ui = None, # TKinter 组件实例
    # value = '' # 用于存储组件值

    def __init__(self,ui=None) -> None:
        self.ui = ui

    def setChild(self,key,widget):
        self._children[key] = widget

    def removeChild(self,key):
        del self._children[key]

    def getChild(self,key):
        return self._children[key]

    def getChildren(self):
        return self._children
    
    def getVaule(self):
        return self.ui.get()
    
    def setValue(self,value):
        self.ui.delete("0","end")
        self.ui.insert(0,value)

class ListBoxtWidget:
    ui = None, # TKinter 组件实例
    # _max_len = 0

    def __init__(self,root,showCall) -> None:
        self._renderUi(root,showCall)
        
    def _renderUi(self,root,showCall):
        self.ui = Listbox(root,width=45,height=15,selectmode=MULTIPLE)
        showCall(self.ui)
        return

    def addItem(self,value):
        self.ui.insert(self.ui.size(), value)
        # self._max_len = self._max_len + 1
        
    def updateItem(self,index,value):
        self.ui.delete(index)
        self.ui.insert(index,value)
    
    def updateItemByValue(self,oldValue,newValue):
        index = self.getItemIndex(oldValue)
        if index == False:
            return False
        self.updateItem(index,newValue)
        return True

    def deleteItem(self,index):
        self.ui.delete(index)
        # self._max_len = self._max_len - 1

    def deleteItemByValue(self,value):
        index = self.getItemIndex(value)
        if index == False:
            return False
        self.deleteItem(index)
        return True

    def getSelectItems(self) -> list:
        return self.ui.curselection()
    
    def getSize(self) -> int:
        return self.ui.size() 
    
    def getAllItems(self) -> list:
        return self.ui.get(first=0,last=self.ui.size() - 1)

    def getItem(self,index):
        return self.ui.get(first=index,last=index)[0]
    
    def getItemIndex(self,value) -> int:
        lis = self.getAllItems()
        if value in lis:
           return lis.index(value)
        else:
            return False
    
    