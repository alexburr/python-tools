import logging
import sys
import inspect

class logUtil():
    def __init__(self, level: logging):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    
    def add_file_hander(self, filename: str, level: logging):
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(level)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)
        self.logger.info(f'...')
        self.logger.info(f'Added file handler {filename} to logger')

    def add_stdout_hander(self, level: logging):
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(self.formatter)
        self.logger.addHandler(stdout_handler)
        self.logger.info(f'...')
        self.logger.info(f'Added stdout handler to logger')

    def get_calling_function_name(self):
        return inspect.stack()[2][3]

    def method_start_debug(self):
        self.logger.debug(f'Begin {self.get_calling_function_name()}() >>')

    def method_end_debug(self):
        self.logger.debug(f'<< End {self.get_calling_function_name()}()')

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)
