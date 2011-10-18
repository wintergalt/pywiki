'''
Created on Oct 18, 2011

@author: dromoli
'''
import unittest
from model.Page import Page

class TestPage(unittest.TestCase):
    
    def testSimple(self):
        page = Page(title='the page title', content='the page content') 
        self.assertEquals(page.title, 'the page title', 'Page titles fail')
        self.assertEquals(page.content, 'the page content', 'Page contents fail')
        