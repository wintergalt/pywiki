'''
Created on Oct 18, 2011

@author: dromoli
'''


from model.Category import Category
from model.Page import Page
import unittest

class TestCategory(unittest.TestCase):
    
    def testSimple(self):
        cat = Category('The Title')
        self.assertEquals('The Title', cat.title, 'The titles fail')
        
    def testAddRemovePages(self):
        cat = Category('Test category')
        pageOne = Page(cat, 'Page One Title', 'Page One Content')
        pageTwo = Page(cat, 'Page Two Title', 'Page Two Content')
        cat.add_page(pageOne)
        cat.add_page(pageTwo)
        
        self.assertEquals(len(cat.pages), 2, 'Pages len fail')
        
        cat.remove_page(pageOne)
        self.assertEquals(len(cat.pages), 1, 'Pages len fail')
        
        cat.remove_page(pageTwo)
        self.assertEquals(len(cat.pages), 0, 'Pages len fail')
    
    
if __name__ == '__main__':
    unittest.main()