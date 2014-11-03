## Singleton type class to create singleton objects
# Classes which inherit from this class will be singleton.
# This code was taken from:\n
# http://blog.amir.rachum.com/blog/2012/04/26/implementing-the-singleton-pattern-in-python/
class SingletonType(type):
    ## Caller
    #
    # @param cls The class.
    # @param *args The arguments.
    # @param **kwargs The argument list.
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance
