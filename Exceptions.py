"""
Custom exceptions
"""
import time

from Utils import log


class SystemFailureException(Exception):
    def __init_(self, threshold, delta):
        self.message = f"{time.time()} : System failure detected\tDELTA : {delta}\tTHRESHOLD : {threshold}"
        super().__init__(self.message)


class InvalidConfigException(Exception):
    def __init_(self):
        self.message = f"Config is missing a required key"
        super().__init__(self.message)
