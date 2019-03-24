import __main__


class TestingDatabase(object):
    pass


class RealDatabase(object):
    pass


if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = RealDatabase
