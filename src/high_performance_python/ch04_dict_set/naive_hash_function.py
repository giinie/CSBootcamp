class City(str):
    def __hash__(self):
        return ord(self[0])


if __name__ == '__main__':
    print('Adding Rome, San Francisco, New York and Barcelona to a set. ' \
          'New York and Barcelona will collide!')
    data = {
        City('Rome'): 4,
        City('San Francisco'): 3,
        City('New York'): 5,
        City('Barcelona'): 2,
    }
