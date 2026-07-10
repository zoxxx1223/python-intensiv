"""
Logging Modul in Python

debug
info
warning <<< das ist die
error
critical

Logger -> Handler (Stream, File, RotatingFileHandler) -> Formatter

"""

import logging

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("dev.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def search():
    logger.info("Not found")
    logger.warning("Not found waring")
    logger.error("Not found")


search()
