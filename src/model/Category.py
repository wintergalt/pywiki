'''
Created on Oct 18, 2011

@author: dromoli
'''

class Category():
    
    def __init__(self, parent=None, title=None, pages=[]):
        self.parent = parent
        self.pages = pages
        self.title = title 
        
    def add_page(self, page):
        self.pages.append(page)
        
    def remove_page(self, page):
        self.pages.remove(page)