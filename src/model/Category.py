'''
Created on Oct 18, 2011

@author: dromoli
'''

from PySide.QtGui import QStandardItem, QIcon

class Category(QStandardItem):
    
    def __init__(self, title=None):
        super(Category, self).__init__(title)
        self.title = title 
        self.content = None
        self.setIcon(QIcon('images/folder-16.png'))
        
    def add_page(self, page):
        self.pages.append(page)
        
    def remove_page(self, page):
        self.pages.remove(page)