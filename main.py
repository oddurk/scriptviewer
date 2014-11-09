# TODO: Handle python files better
from scriptparser import ScriptParser
from configure import Configuration
from PySide import QtCore, QtGui
from filetree import *

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

# Main functionality goes here.
if __name__ == "__main__":
    #import sys

    #app = QtGui.QApplication(sys.argv)
    #window = MainWindow()
    #window.show()
    #sys.exit(app.exec_())

    """
    f1 = FileContainer("/home/oddur/PycharmProjects/scriptviewer/config.ini")
    f2 = FileContainer("/home/oddur/PycharmProjects/scriptviewer/main.py")
    f3 = FileContainer("/home/oddur/PycharmProjects/scriptviewer/doxyconfig")
    f4 = FileContainer("/home/oddur/PycharmProjects/scriptviewer/LICENSE")
    f5 = FileContainer("/home/oddur/PycharmProjects/scriptviewer/SingletonType")

    ft = FileTree(f1)
    ft.addLink(f1, f2, 20)
    ft.addLink(f2, f3, 30)
    ft.addLink(f1, f4, 40)
    ft.addLink(f4, f5, 40)


    #ft.printTree()

    print ft
    """


    # Setup the configure object
    config = Configuration("config.ini")

    #sp = ScriptParser("/home/oddur/PycharmProjects/scriptviewer/resources/main_script.sh")
    #sp.parseFile()

    sp = ScriptParser("/home/oddur/tool/configure.csh")
    sp.parseFile()

    print sp.getGraph().getGraph()

    #sp.rootPath= "/home/oddur/bsc/TOOL_ORIGINAL/"
    #sp.parseFile("/home/oddur/bsc/TOOL_ORIGINAL/configure.csh")

    #Plotter.plotGraph(FileGraph().getGraph())
