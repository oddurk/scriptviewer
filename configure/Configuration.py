from SingletonType import SingletonType


## Configuration
# Container for all configuration used in the program.
# This is a singleton class, which is accessible everywhere in the program.
# The loader expects a file containing:\n
# key1=value1 \n
# key2=value2 \n
# ... \n
# keyn=valuen \n
# The configuration class keeps a copy of the original file in memory, so that it can be written back
# in the same order as it was read.
class Configuration(object):
    __metaclass__ = SingletonType
    ## @var configParameters
    # Contains all the configuration parameters used.
    ## @var configKeys
    # Container for all keys.
    ## @var dataLoaded
    # Indicator if data has been loaded.
    ## @var originalFile
    # The orignal file is kept in memory, so that it can be written back.
    #

    ## The constructor
    #
    # @param self The object pointer.
    # @param configFile A configuration file to load.
    def __init__(self, configFile=""):
        self.configParameters = dict()
        self.configKeys = set()
        self.dataLoaded = False
        self.originalFile = []
        if configFile != "":
            self.loadData(configFile)

    ## Loads the data from a given source
    # Comments are ignored
    # @param self The object pointer.
    # @param source The location of the file to read
    def loadData(self, source):
        if self.dataLoaded == True:
            self.configParameters.clear()
            self.configKeys.clear()
            del self.originalFile[:]
        for item in open(source, 'r'):
            self.originalFile.append(item)
            if not (item[0] == "#" or item[0] == "\n"):
                key, value = str(item.split('=')[0]).strip(), str(item.split('=')[1]).strip()
                self.setValue(key, value)
                self.dataLoaded = True

    ## Saves the configuration data to file
    #
    # @param self The object pointer.
    # @param file The file to save the configuration to.
    def saveData(self, file):
        f = open(file, 'w')
        writtenKeys = set()

        # Loop through the original file to save.
        # This is done in order to keep comments, and order
        for line in self.originalFile:
            if line[0] == '#' or line[0] == '\n':
                f.write(line)
                continue
            key = str(line.split('=')[0]).strip()
            if key in self.configKeys:
                f.write(str(key) + '=' + str(self.configParameters[key]) + '\n')
                writtenKeys.add(key)
        # Add all values which have been added to the end of the file
        unwrittenKeys = set(self.configParameters.keys()).difference(writtenKeys)
        for key in unwrittenKeys:
            f.write(str(key) + '=' + str(self.configParameters[key]) + '\n')


    ## Returns a value for a given key
    #
    # @param self The object pointer
    # @param key The key of the parameter
    # @param default The default value, returned if the key is not found.
    def getValue(self, key, default=''):
        if key in self.configKeys:
            return self.configParameters[key]
        else:
            return None

    ## Sets a value of a parameter
    #
    # @param self The object pointer
    # @param key The key to be updated.
    # @param value The value to be set.
    def setValue(self, key, value):
        if key not in self.configKeys:
            self.configParameters[key] = value
            self.configKeys.add(key)

    ## Removes a key from the collection along with the value.
    #
    # @param self The object pointer
    # @param key The key to remove
    def removeKey(self, key):
        if key in self.configKeys:
            del self.configParameters[key]
            self.configKeys.remove(key)