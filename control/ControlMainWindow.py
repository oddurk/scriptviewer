from configure import Configuration
from scriptparser import ScriptParser
from PySide import QtGui, QtCore
from view import mainwindow

## Controller class for the Main window
class ControlMainWindow(QtGui.QMainWindow):

    ## The constructor.
    #
    # @param self The object pointer.
    # @param parent The parent window of the windows, default none.
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self._ui = mainwindow.Ui_MainWindow()
        self._ui.setupUi(self)
        Configuration("config.ini")
        self._scriptparser = ScriptParser("")

        self._ui.action_Quit.triggered.connect(self.quitprogram)
        self._ui.actionOpen_script.triggered.connect(self.openfile)
        self._scriptparser.fnf.connect(self.displayerror)



    def displayerror(self, string):
        text = self._ui.textEdit.toPlainText().strip()
        text = text + "\n" + string
        self._ui.textEdit.setText(text)

    def quitprogram(self):
        QtCore.QCoreApplication.instance().quit()

    def openfile(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                                                     ("Open script file"),
                                                     "",
                                                     ("Script file [.csh, .sh, .py] (*.csh *.py *.sh)"))

        if fileName[0] != "":
            self._ui.textEdit.clear()
            self._scriptparser.setrootfile(fileName[0])
            self._scriptparser.parseFile()