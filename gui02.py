import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class mouseDataGroup(QGroupBox):
    def __init__(self, tit: str):
        super().__init__(tit)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        folderButton = QPushButton("Select Folder")
        folderLabel = QLabel("Current folder:")
        selectMouse = QComboBox()
        addMouseBtn = QPushButton("Add Mouse")
        self.layout.addWidget(folderButton)
        self.layout.addWidget(folderLabel)
        self.layout.addWidget(selectMouse)
        self.layout.addWidget(addMouseBtn)
        


class experimentSettingsGroup(QGroupBox):
    def __init__(self, tit: str):
        super().__init__(tit)   
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.l1 = QLabel("Mode") 
        self.l2 = QLabel("Number of Trials")
        self.l3 = QLabel(f"% of FC")
        self.l4 = QLabel(f"% of NC")
        self.l5 = QLabel(f"% of QC")
        self.l6 = QLabel(f"% of Pavlovian trials")
        self.l7 = QLabel("Number of retrieval")

        self.c1 = QComboBox()
        self.e2 = QLineEdit()
        self.e3 = QLineEdit()
        self.e4 = QLineEdit()
        self.e5 = QLineEdit()
        self.e6 = QLineEdit()
        self.e7 = QLineEdit()
        self.p2 = QLabel("Predicted:")
        self.p3 = QLabel("Predicted: ")
        self.p4 = QLabel("Predicted: ")
        self.p5 = QLabel("Predicted: ")
        self.p6 = QLabel("Predicted: ")
        self.p7 = QLabel("Predicted: ")

        self.layout.addWidget(self.l1, 0,0,1,1)
        self.layout.addWidget(self.l2, 1,0,1,1)
        self.layout.addWidget(self.l3, 2,0,1,1)
        self.layout.addWidget(self.l4, 3,0,1,1)
        self.layout.addWidget(self.l5, 4,0,1,1)
        self.layout.addWidget(self.l6, 5,0,1,1)
        self.layout.addWidget(self.l7, 6,0,1,1)

        self.layout.addWidget(self.c1, 0,1,1,2)
        self.layout.addWidget(self.e2, 1,1,1,1)
        self.layout.addWidget(self.e3, 2,1,1,1)
        self.layout.addWidget(self.e4, 3,1,1,1)
        self.layout.addWidget(self.e5, 4,1,1,1)
        self.layout.addWidget(self.e6, 5,1,1,1)
        self.layout.addWidget(self.e7, 6,1,1,1)

        self.layout.addWidget(self.p2, 1,2,1,1)
        self.layout.addWidget(self.p3, 2,2,1,1)
        self.layout.addWidget(self.p4, 3,2,1,1)
        self.layout.addWidget(self.p5, 4,2,1,1)
        self.layout.addWidget(self.p6, 5,2,1,1)
        self.layout.addWidget(self.p7, 6,2,1,1)

        

class fileSavingGroup(QGroupBox):
    def __init__(self, tit: str):
        super().__init__(tit)
        self.layout = QVBoxLayout() 
        self.setLayout(self.layout)
        folderButton = QPushButton("Select Folder")
        folderLabel = QLabel("Current folder:")
        self.layout.addWidget(folderButton)
        self.layout.addWidget(folderLabel)

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        grid = QGridLayout()
        
        self.l1 = fileSavingGroup('Saving File informations')
        l2 = mouseDataGroup("Mouse Data")
        l3 = experimentSettingsGroup("Experiment Settings")
        runButton = QPushButton("Run")

        grid.addWidget(self.l1, 0,0,2,1)
        grid.addWidget(l2, 2,0,4,1)
        grid.addWidget(runButton, 6,0,1,1)
        grid.addWidget(l3, 0,1,7,1)

        widget.setLayout(grid)
        self.setCentralWidget(widget)           # Cannot set QxxLayout directly on the QMainWindow
                                                # Need to create a QWidget and set it as the central widget
        self.setGeometry(100,100,900,400)
        self.setWindowTitle("Food cue conditioning")
        self.show()

        
    class fileSavingGroup(QGroupBox):
        def __init__(self, tit: str):
            super().__init__(tit)
            self.layout = QVBoxLayout() 
            self.ciao = 'ciao'


if __name__ == '__main__':
    app = QApplication(sys.argv)


    # app.setStyle("Fusion")

    # # Now use a palette to switch to dark colors:
    # palette = QPalette()
    # palette.setColor(QPalette.Window, QColor(53, 53, 53))
    # palette.setColor(QPalette.WindowText, Qt.white)
    # palette.setColor(QPalette.Base, QColor(25, 25, 25))
    # palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    # palette.setColor(QPalette.ToolTipBase, Qt.black)
    # palette.setColor(QPalette.ToolTipText, Qt.white)
    # palette.setColor(QPalette.Text, Qt.white)
    # palette.setColor(QPalette.Button, QColor(53, 53, 53))
    # palette.setColor(QPalette.ButtonText, Qt.white)
    # palette.setColor(QPalette.BrightText, Qt.red)
    # palette.setColor(QPalette.Link, QColor(42, 130, 218))
    # palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # palette.setColor(QPalette.HighlightedText, Qt.black)
    # app.setPalette(palette)



    ex = window()
    ex.show()
    sys.exit(app.exec_())