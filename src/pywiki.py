'''
Created on Oct 19, 2011

@author: dromoli
'''

from PySide.QtGui import QMainWindow, QApplication, QStandardItemModel, \
    QAbstractItemView
from model.Category import Category
from model.Page import Page
from ui.mainwindow import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)

        it1 = Category(title='it1')
        it2 = Page('it2', 'This is it2\'s content')
        it3 = Page('it3', 'This is it3\'s content')
        it1.setChild(it1.rowCount(), it2)
        it1.setChild(it1.rowCount(), it3)
        model = QStandardItemModel()
        model.appendRow(it1)
        tv = self.mainwindow.treeView
        tv.setModel(model)
        tv.setRootIsDecorated(True)
        tv.setSelectionMode(QAbstractItemView.SingleSelection)
        tv.setSelectionBehavior(QAbstractItemView.SelectItems)
        tv.clicked.connect(self.printData)

        
    def printData(self):
        it = self.mainwindow.treeView.model().itemFromIndex(self.mainwindow.treeView.currentIndex())
        print('Item: {0}'.format(type(it)))
        self.mainwindow.textEdit.setText(it.content)
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
    