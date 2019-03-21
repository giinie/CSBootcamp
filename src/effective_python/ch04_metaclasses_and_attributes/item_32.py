import logging


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = 'Value for %s' % item
        setattr(self, item, value)
        return value


data = LazyDB()
print('Before:', data.__dict__)
print('foo:   ', data.foo)
print('After  ', data.__dict__)
print('-' * 50)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, item):
        print('Called __getattr__(%s)' % item)
        return super(LoggingLazyDB, self).__getattr__(item)


data = LoggingLazyDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)
print('-' * 50)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print('Called __getattribute__(%s)' % item)
        try:
            return super(ValidatingDB, self).__getattribute__(item)
        except AttributeError:
            value = 'Value for %s' % item
            setattr(self, item, value)
            return value


data = ValidatingDB()
print('exists:', data.exists)
print('foo:   ', data.foo)
print('foo:   ', data.foo)
print('-' * 50)


class MissingPropertyDB(object):
    def __getattr__(self, item):
        if item == 'bad_name':
            raise AttributeError('%s is missing' % item)
        value = 'Value for %s' % item
        setattr(self, item, value)
        return value


# import logging
#
# try:
#     data = MissingPropertyDB()
#     data.foo  # Test this works
#     data.bad_name
# except:
#     logging.exception('Expected')

data = LoggingLazyDB()
print('Before:  ', data.__dict__)
print('foo exists:  ', hasattr(data, 'foo'))
print('After:   ', data.__dict__)
print('foo exists:  ', hasattr(data, 'foo'))
print('-' * 50)

data = ValidatingDB()
print('foo exists:', hasattr(data, 'foo'))
print('foo exists:', hasattr(data, 'foo'))
print('-' * 50)


class SavingDB(object):
    def __setattr__(self, key, value):
        # Save some data to the DB log
        super(SavingDB, self).__setattr__(key, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, key, value):
        print('Called __setattr__(%s, %r)' % (key, value))
        super(LoggingSavingDB, self).__setattr__(key, value)


data = LoggingSavingDB()
print('Before:', data.__dict__)
data.foo = 5
print('After :', data.__dict__)
data.foo = 7
print('Finally:', data.__dict__)
print('-' * 50)


class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = {}

    def __getattribute__(self, item):
        print('Called __getattribute__(%s)' % item)
        return self._data[item]


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        data_dict = super(DictionaryDB, self).__getattribute__('_data')
        return data_dict[item]


data = DictionaryDB({'foo': 3})
print(data.foo)
print('-' * 50)

