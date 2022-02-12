import logging, os
from file_handling.file_handling import *

log_fmt = logging.Formatter("%(pathname)s s%(funcName)s %(lineno)d %(levelname)s %(message)s")

def stream_handler(format_string):
    handler = logging.StreamHandler
    handler.setFormatter()
    return handler

def create_logger(name, level, dir, stream=False):
    log = logging.getLogger(name)
    log.setLevel(level)
    file_handler = logging.FileHandler(dir + os.sep + name + ".txt", mode="w")
    file_handler.setFormatter(log_fmt)
    log.addHandler(file_handler)

    if stream:
        stream_handle = logging.StreamHandler()
        stream_handle.setFormatter(log_fmt)
        log.addHandler(stream_handle)

    return log

class Root_log():
    def __init__(self, master_level=logging.ERROR, master_terminal=False, max_log_age=10):


        self.format_string = "%(pathname)s s%(funcName)s %(lineno)d %(levelname)s %(message)s"
        self.root = logging.getLogger("")

        self.log_dir = os.path.dirname(__file__)+os.sep+ "logs"
        log_name = "master_log.txt"
        if not file_exist(self.log_dir, log_name):
            create_file(self.log_dir, log_name)

        self.rootHandler = logging.FileHandler(self.log_dir + os.sep + log_name)
        self.rootHandler.setFormatter(self.format_string)
        self.root.addHandler(self.rootHandler)

        if master_terminal:
            stream = logging.StreamHandler
            self.root.addHandler(stream)







#class SQL_log():
#    def __init__(self, level=logging.ERROR, terminal_output=False):
#        super(SQL_log, self).__init__(self)
#        log_name = __name__+".txt"
#        self.logger = logging.getLogger(log_name)
#
#        if not file_exist(self.log_dir, log_name):
#            create_file(self.log_dir, log_name)
#
#        fileHandler = logging.FileHandler(self.log_dir + os.sep + log_name)
#        fileHandler.setFormatter(self.format_string)
#        self.logger.addHandler(fileHandler)
#        self.logger.addHandler(self.rootHandler)
#
#        if terminal_output:
#            stream = logging.StreamHandler
#            self.logger.addHandler(stream)
#    def get_logger(self):
#        return self.logger