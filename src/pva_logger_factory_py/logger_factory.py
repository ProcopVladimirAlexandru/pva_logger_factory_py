import logging


class LoggerFactory(object):
    """Very basic class which wraps logging module to shorten
    code needed by other classes to instantiate a logger to one line.
    """
    # TODO add proper docs
    LEVEL_MAP = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }
    LOGGER_DICT = dict()

    def __init__(self):
        return

    @staticmethod
    def init_logger(name: str, level: str,
                    _format: str = "[%(levelname)s] [%(asctime)s] %(message)s"):
        logger = LoggerFactory.get_logger(name)
        if logger:
            return logger

        formatter = logging.Formatter(_format)

        logger = logging.getLogger(name)
        logger.setLevel(LoggerFactory.LEVEL_MAP.get(level))

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        LoggerFactory.LOGGER_DICT[name] = logger
        return logger

    @staticmethod
    def get_logger(name):
        return LoggerFactory.LOGGER_DICT.get(name, None)

    @staticmethod
    def get_levels():
        return list(LoggerFactory.LEVEL_MAP.keys())
