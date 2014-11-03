from scriptparser import ScriptParser
from configure import Configuration
from plotter import Plotter

# Main functionality goes here.
if __name__ == "__main__":
    # Setup the configure object
    config = Configuration("config.ini")

    sp = ScriptParser()
    #sp.parseFile("resources/main_script.sh")
    sp.rootPath = ("/home/oddur/tool/")
    sp.parseFile("/home/oddur/tool/configure.csh")
    plotter = Plotter()

    plotter.plotGraph()