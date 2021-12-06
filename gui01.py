import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QMainWindow):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        widget = QWidget()
        grid = QGridLayout()
        
        l1 = fileSavingGroup("Saving Directory")
        l2 = mouseDataGroup("Mouse Data")
        l3 = experimentSettingsGroup("Experiment Settings")
        runButton = QPushButton("Run")

        grid.addWidget(l1, 0,0,2,1)
        grid.addWidget(l2, 2,0,4,1)
        grid.addWidget(runButton, 6,0,1,1)
        grid.addWidget(l3, 0,1,7,1)

        widget.setLayout(grid)
        self.setCentralWidget(widget)           # Cannot set QxxLayout directly on the QMainWindow
                                                # Need to create a QWidget and set it as the central widget
        self.setGeometry(100,100,900,400)
        self.setWindowTitle("Food cue conditioning")
        self.show()



def fileSavingGroup(title):
    group = QGroupBox(title)
    vBox = QVBoxLayout()
    group.setLayout(vBox)
    folderButton = QPushButton("Select Folder")
    folderLabel = QLabel("Current folder:")
    vBox.addWidget(folderButton)
    vBox.addWidget(folderLabel)
    return group

def mouseDataGroup(title):
    group = QGroupBox(title)
    vBox = QVBoxLayout()
    group.setLayout(vBox)
    folderButton = QPushButton("Select Folder")
    folderLabel = QLabel("Current folder:")
    selectMouse = QComboBox()
    addMouseBtn = QPushButton("Add Mouse")
    vBox.addWidget(folderButton)
    vBox.addWidget(folderLabel)
    vBox.addWidget(selectMouse)
    vBox.addWidget(addMouseBtn)
    return group

    



def experimentSettingsGroup(title):
    group = QGroupBox(title)
    layout = QGridLayout()
    l1 = QLabel("Mode") 
    l2 = QLabel("Number of Trials")
    l3 = QLabel(f"% of FC")
    l4 = QLabel(f"% of NC")
    l5 = QLabel(f"% of QC")
    l6 = QLabel(f"% of Pavlovian trials")
    l7 = QLabel("Number of retrieval")

    c1 = QComboBox()
    e2 = QLineEdit()
    e3 = QLineEdit()
    e4 = QLineEdit()
    e5 = QLineEdit()
    e6 = QLineEdit()
    e7 = QLineEdit()
    p2 = QLabel("Predicted:")
    p3 = QLabel("Predicted: ")
    p4 = QLabel("Predicted: ")
    p5 = QLabel("Predicted: ")
    p6 = QLabel("Predicted: ")
    p7 = QLabel("Predicted: ")

    layout.addWidget(l1, 0,0,1,1)
    layout.addWidget(l2, 1,0,1,1)
    layout.addWidget(l3, 2,0,1,1)
    layout.addWidget(l4, 3,0,1,1)
    layout.addWidget(l5, 4,0,1,1)
    layout.addWidget(l6, 5,0,1,1)
    layout.addWidget(l7, 6,0,1,1)

    layout.addWidget(c1, 0,1,1,2)
    layout.addWidget(e2, 1,1,1,1)
    layout.addWidget(e3, 2,1,1,1)
    layout.addWidget(e4, 3,1,1,1)
    layout.addWidget(e5, 4,1,1,1)
    layout.addWidget(e6, 5,1,1,1)
    layout.addWidget(e7, 6,1,1,1)

    layout.addWidget(p2, 1,2,1,1)
    layout.addWidget(p3, 2,2,1,1)
    layout.addWidget(p4, 3,2,1,1)
    layout.addWidget(p5, 4,2,1,1)
    layout.addWidget(p6, 5,2,1,1)
    layout.addWidget(p7, 6,2,1,1)

    group.setLayout(layout)
    return group






if __name__ == '__main__':
    app = QApplication(sys.argv)


    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)



    ex = window()
    ex.show()
    sys.exit(app.exec_())