'''
Created on Oct 19, 2011

@author: dromoli
'''

import sys
from ui.mainwindow import Ui_MainWindow
from PySide.QtGui import QMainWindow, QPushButton, QApplication, QStandardItem, QStandardItemModel

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mainwindow = Ui_MainWindow()
        self.mainwindow.setupUi(self)

        it1 = QStandardItem('it1')
        it2 = QStandardItem('it2')
        it1.setChild(0, it2)
        model = QStandardItemModel()
        model.appendRow(it1)
        model.appendRow(it2)
        self.mainwindow.treeView.setModel(model)
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
    