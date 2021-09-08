import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

from crypto_proxy.settings import settings

log_folder = os.path.realpath("../logs")
logs_format = (
    "[%(asctime)s - %(levelname)s - module:%(filename)s#%(lineno)d " '- func: "%(funcName)s"] message: "%(message)s"'
)


def configure_log_folder(file_name):
    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    logs_path_root = log_folder + "/crypto-proxy/"
    logs_path = logs_path_root + file_name

    if not os.path.exists(logs_path_root):
        os.mkdir(logs_path_root)

    if os.path.exists(logs_path):
        os.remove(logs_path)

    return logs_path


def conf_console_handler(log_level: str) -> logging.StreamHandler:
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(log_level)

    formatter = logging.Formatter(logs_format)
    consoleHandler.setFormatter(formatter)

    return consoleHandler


def configure_file_handler(log_level: str) -> logging.getLogger:
    filename = "crypto-proxy-server-{:%Y-%m-%d %H-%M-%S}.log".format(datetime.now())
    logs_path = configure_log_folder(filename)

    fileHandler = RotatingFileHandler(logs_path, maxBytes=5000000, backupCount=5)

    fileHandler.setLevel(log_level)
    fileHandler.setFormatter(logs_format)

    return fileHandler


def configure_loggers(log_level: str):
    logger = logging.getLogger("crypto_proxy")
    logger.setLevel(log_level)
    console_handler = conf_console_handler(log_level)

    file_handler = configure_file_handler(log_level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = configure_loggers(settings.log_level)
