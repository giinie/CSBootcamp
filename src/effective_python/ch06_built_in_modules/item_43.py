import logging
from contextlib import contextmanager
from threading import Lock

lock = Lock()
with lock:
    print('Lock is held')
print('-' * 50)

logging.getLogger().setLevel(logging.WARNING)


def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')


my_function()
print('-' * 50)


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


with debug_logging(logging.DEBUG):
    print('Inside:')
    my_function()
print('After:')
my_function()
print('-' * 50)

# with open('my_output.txt', 'w') as handle:
#     handle.write('This is some data!')


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)


with log_level(logging.DEBUG, 'my_log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')
print('-' * 50)

logger = logging.getLogger('my_log')
logger.debug('Debug will not print')
logger.error('Error will print')
