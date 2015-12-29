from PySide.QtCore import *
from PySide.QtGui import *
import sys
import UI

class MainWindow(QDialog,UI.Ui_Form):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()