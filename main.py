# TODO: Handle python files better
from control import ControlMainWindow
from PySide import QtGui
import sys


# Main functionality goes here.
if __name__ == "__main__":
    # Setup the configuration

    app = QtGui.QApplication(sys.argv)
    mainWindowControler = ControlMainWindow()
    mainWindowControler.show()
    sys.exit(app.exec_())

