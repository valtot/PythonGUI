import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QMainWindow):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        widget = QWidget()
        grid = QGridLayout()
        
        b1 = QPushButton() # class inheritance once again
        b1.setText("Button1")
        b1.clicked.connect(b1_clicked)
        b2 = QPushButton() # class inheritance once again
        b2.setText("Button2")
        
        b2.clicked.connect(b2_clicked)

        b3 = QPushButton() # class inheritance once again
        b3.setText("Button3")
        b3.clicked.connect(b3_clicked)

        b4 = QLineEdit("ciao")
        # grid.addRow("integer validator", b4)
        b4.setDisabled(True)

        grid.addWidget(b1, 0,0,1,1)
        grid.addWidget(b2, 0,1,1,1)
        grid.addWidget(b3, 1,1,1,1)
        grid.addWidget(b4, 1,0,1,1)

        widget.setLayout(grid)
        self.setCentralWidget(widget)           # Cannot set QxxLayout directly on the QMainWindow
                                                # Need to create a QWidget and set it as the central widget
        self.setGeometry(100,100,200,100)
        self.setWindowTitle("My application")
        self.show()
def b1_clicked():
    print ("Button 1 clicked")
def b2_clicked():
    print ("Button 2 clicked")
def b3_clicked():
    Fn = QFileDialog()
    Fn.exec_()
    print(Fn)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())
