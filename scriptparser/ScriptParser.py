# TODO: Refactor so it can be tested.

from configure import Configuration
from scriptparser import FileContainer
from filegraph import FileGraph
import re
import os

## The Script Parser class
# Parses the given script
class ScriptParser(object):
    ## The constructor
    #
    # @param self The object pointer.
    def __init__(self):
        self._extensions = []
        self._parsers = []
        self._parentDir = ""
        self._fileContainer = FileContainer()
        self._graph = FileGraph()
        self.setup()
        self.rootPath = ""

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
    def parseFile(self, parsedFile):
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
            print "File not found: ", parsedFile

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

                    #print "addingEdge:", callerFile.replace(self.rootPath, ""), "->", os.path.abspath(self._parentDir + "/" + pFile).replace(self.rootPath, "")
                    self._graph.add_edge(callerFile.replace(self.rootPath, ""), os.path.abspath(self._parentDir + "/" + pFile).replace(self.rootPath, ""))
                    if not self._fileContainer.hasBeenParsed(os.path.abspath(self._parentDir + "/" + pFile)):
                        self.parseFile(self._parentDir + "/" + pFile)