'''
Created on Oct 18, 2011

@author: dromoli
'''

from PySide.QtGui import QStandardItem, QIcon

class Page(QStandardItem):
    
    def __init__(self, title=None, content=None):
        super(Page, self).__init__(title)
        self.title = title
        self.content = content
        self.setIcon(QIcon('images/document-16.png'))
        
    
