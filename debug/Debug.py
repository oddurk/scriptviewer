from SingletonType import SingletonType

## Debug class
# A naive way to print debug in the program, as it will affect the running speed.as
# Implemented as a Singleton class.
# This class is not unit-tested.
class Debug(object):
    __metaclass__ = SingletonType

    ## The constructor.
    #
    # @param self The object pointer.
    def __init__(self):
        self._show_debug = False
        self._show_dev = False

    ## The dev printer
    # Prints the dev_str, if _show_dev is True.
    #
    # @param self The object pointer.
    # @param dev_str The string to print.
    def dev(self, dev_str):
        if self._show_dev:
            print(dev_str)

    ## The debug printer
    # Prints the debug_str, if _show_debug is True.
    #
    # @param self The object pointer.
    # @param debug_str The debug string.
    def debug(self, debug_str):
        if self._show_debug:
            print(debug_str)

    ## Method to turn on debug output, void.
    #
    # @param self The object pointer.
    def showdebug(self):
        self._show_debug = True

    ## Methods to turn of debug output, void.
    #
    # @param self The object pointer.
    def hidedebug(self):
        self._show_debug = False

    ## Method to turn on the dev output, void.
    #
    # @param self The object pointer.
    def showdev(self):
        self._show_dev = True

    ## Method to hide the dev output, void.
    #
    # @param self The object pointer.
    def hidedev(self):
        self._show_dev = False
