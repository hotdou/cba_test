import logging


def get_global_logger(name=''):
    formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                                  datefmt='%Y-%m-%d,%H:%M:%S')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logger.propagate = 0
        logger.addHandler(handler)

    return logger