from configure import Configuration
from scriptparser import FileContainer
import re
import os

class ScriptParser(object):
    def __init__(self):
        self._extensions = []
        self._parsers = []
        self.readExtensions()
        self.setupParsers()
        self._parentDir = ""
        self._fileContainer = FileContainer()

    def readExtensions(self):
        config = Configuration()
        extensions = config.getValue("Extensions")
        for item in str(extensions).split(","):
            self._extensions.append(item.strip())

    def setupParsers(self):
        for item in self._extensions:
            pattern = str(item).replace(".", ".*\\.")
            parser = re.compile(pattern)
            self._parsers.append(parser)

    def parseFile(self, parseFile):
        self._fileContainer.addFile(os.path.abspath(parseFile))
        print "Parsing file"
        print os.path.abspath(parseFile)
        print
        self._parentDir = parseFile.split("/")[0]
        for line in open(parseFile).readlines():
            self.parseLine(line.strip())

    def parseLine(self, line):
        for parser in self._parsers:
            if parser.search(line):
                parsedFile = parser.search(line).group(0)
                if not self._fileContainer.hasBeenParsed(os.path.abspath(self._parentDir + "/" + parsedFile)):
                    self.parseFile(self._parentDir + "/" + parsedFile)
