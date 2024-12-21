import inspect
import logging


def project_logger(log_level=logging.DEBUG):
    loger_name = inspect.stack()[1][3]
    logger = logging.getLogger(loger_name)
    logger.setLevel(logging.DEBUG) # Sets the default log level (in this case, to log all messages)

    file_handler = logging.FileHandler("logs.log", mode="a", encoding="utf-8") # a for append, w for overwrite
    file_handler.setLevel(log_level)

    formatter = logging.Formatter("{levelname} - {asctime} - {name} - {message}", style="{",
                                  datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

