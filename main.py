# TODO: Handle python files better
from scriptparser import ScriptParser
from configure import Configuration
from plotter import Plotter
from filegraph import FileGraph

# Main functionality goes here.
if __name__ == "__main__":
    # Setup the configure object
    config = Configuration("config.ini")

    sp = ScriptParser()
    #sp.rootPath = "/home/oddur/PycharmProjects/ScriptPlotter/resources/"
    #sp.parseFile("resources/main_script.sh")

    sp.rootPath = ("/home/oddur/tool/")
    sp.parseFile("/home/oddur/tool/configure.csh")

    #sp.rootPath= "/home/oddur/bsc/TOOL_ORIGINAL/"
    #sp.parseFile("/home/oddur/bsc/TOOL_ORIGINAL/configure.csh")

    Plotter.plotGraph(FileGraph().getGraph())
