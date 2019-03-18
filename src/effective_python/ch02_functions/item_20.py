import json
from time import sleep
from datetime import datetime


def log(message, when=datetime.now()):
    print('{}: {}'.format(when, message))


log('Hi there!')
sleep(1)
log('Hi again!')

print('-' * 50)


def log(message: str, when: datetime = None) -> None:
    """Log a message with a timestamp.

    :param message: Message to print.
    :type message: str
    :param when: datetime of when the message occurred. Defaults to the present time.
    :type when: datetime
    """
    when = datetime.now() if when is None else when
    print('{}: {}'.format(when, message))


log('Hi there!')
sleep(1)
log('Hi again!')
help(log)

print('-' * 50)


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
print('foo is bar:', foo is bar)

print('-' * 50)


def decode(data: str, default: dict = None) -> dict:
    """Load JSON data from a string.

    :param data: JSON data to decode.
    :type data: str
    :param default: Value to return if decoding fails. Defaults to an empty dictionary.
    :type default: dict
    :return:
    :rtype:
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
print('foo is bar:', foo is bar)

print('-' * 50)

