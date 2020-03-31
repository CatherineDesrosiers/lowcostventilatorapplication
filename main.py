from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mainapp.mainappwindow import MainAppWindow

def main() :
    app = QApplication(sys.argv)
    m = MainAppWindow()
    m.showFullScreen()

    # Start the event loop...
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

