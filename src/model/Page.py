'''
Created on Oct 18, 2011

@author: dromoli
'''

class Page():
    
    def __init__(self, parent=None, title=None, content=None):
        self.parent = parent
        self.title = title
        self.content = content
        
    