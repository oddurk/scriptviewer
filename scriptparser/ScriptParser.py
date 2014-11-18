# TODO: Refactor so it can be tested.
from configure import Configuration
from PySide import QtCore
from filetree import FileGraph
from filetree import FileContainer
from scriptparser import FileStore
import re
import os

## The Script Parser class
# Parses the given script
class ScriptParser(QtCore.QObject):

    fnf = QtCore.Signal((str,))

    ## The constructor
    #
    # @param self The object pointer.
    def __init__(self, rootfile):
        super(ScriptParser, self).__init__()
        self._extensions = []
        self._parsers = []
        self._parentDir = ""
        self._fileContainer = FileStore()
        self._graph = None
        self._rootfile = rootfile
        self._rootpath = self.rootpathfromfile(self._rootfile)


    ## Setter for the root file.
    #
    # @param self The object pointer.
    # @param rootfile The new root file to set the value to, as string.
    def setrootfile(self, rootfile):
        self._graph = FileGraph(rootfile)
        self._rootfile = rootfile
        self._rootpath = self.rootpathfromfile(self._rootfile)
        self.setup()

    ## Extracts the root path from a file folder name.
    #
    # @param self The object pointer.
    # @param filename The filename to extract the root folder from.
    # @return The root path.
    def rootpathfromfile(self, filename):
        return filename[::-1][0:filename[::-1].find("/")][::-1]

    ## Setup of the internal of the object.
    #
    # @param self The object pointer.
    def setup(self):
        self.readExtensions()
        self.setupParsers()

    ## Reads the file extensions from the config file.
    # This is a utility function used to setup the internal state of the object.
    #
    # @param self The object pointer.
    def readExtensions(self):
        config = Configuration()
        extensions = config.getValue("Extensions")
        for item in str(extensions).split(","):
            self._extensions.append(item.strip())

    ## Setups the parsers used by the object.
    #
    # @param self The object pointer.
    def setupParsers(self):
        for item in self._extensions:
            pattern = str(item).replace(".", "^\w.*\\.")
            parser = re.compile(pattern)
            self._parsers.append(parser)

        # add python parser
        pattern = "python (.*)"
        parser = re.compile(pattern)
        self._parsers.append(parser)

    ## Parses a file
    #
    # @param self The object pointer.
    # @param parsedFile The file to be parsed.
    def parseFile(self, parsedFile = ""):
        if parsedFile == "":
            parsedFile = self._rootfile
        self._fileContainer.addFile(os.path.abspath(parsedFile))
        self._parentDir = os.path.dirname(parsedFile)
        try:
            lineCount = 1
            for line in open(parsedFile).readlines():
                if len(line) > 2:
                    if line.strip()[0] != "#":
                        l = line.replace("./", "")
                        self.parseLine(l.strip(), os.path.abspath(parsedFile), lineCount)
                lineCount += 1
        except IOError:
            err = "File not found: "+ parsedFile
            self.fnf.emit(err)

    ## Parses a line
    #
    # @param self The object pointer.
    # @param line The line to be parsed
    def parseLine(self, line, callerFile, lineNumber):
        for parser in self._parsers:
            if parser.search(line):
                parsedFile = parser.search(line).group(0)
                if parsedFile.find(" ") == -1 or parsedFile.find("python") != -1:
                    pFile = parsedFile
                    if pFile.find("python") != -1:
                        pFile = pFile.replace("python", " ")
                        pFile = pFile.strip()
                        if pFile.find(" ") != -1:
                            pFile = pFile[0:pFile.find(" ")]
                    self._graph.add_edge(FileContainer(callerFile), FileContainer(os.path.abspath(self._parentDir + "/" + pFile).replace(self._rootpath, "")), lineNumber)
                    if not self._fileContainer.hasBeenParsed(os.path.abspath(self._parentDir + "/" + pFile)):
                        self.parseFile(self._parentDir + "/" + pFile)

    def getGraph(self):
        return self._graph