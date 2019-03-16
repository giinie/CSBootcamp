class OpenHello:
    def __enter__(self):
        self.file = open('hello.txt', 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenHello() as hello:
    hello.write('Hello, world!')
