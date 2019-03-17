# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


def to_str(bytes_or_str: object) -> str:
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    elif isinstance(bytes_or_str, str):
        return bytes_or_str  # Instance of str


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')
    elif isinstance(bytes_or_str, bytes):
        return bytes_or_str  # Instance of bytes


print(repr(to_str(b'foo')))
print(repr(to_str('foo')))

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('foo')))


import os

try:
    with open('random.bin', 'w') as f:
        f.write(os.urandom(10))
except:
    logging.exception('Expected')
else:
    assert False


with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
