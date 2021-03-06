import timeit

from binary_search import binary_search
from linear_search import linear_search


def time_and_log(function, needle, haystack):
    index = function(needle, haystack)
    t = timeit.timeit(
        stmt='{}(needle, haystack)'.format(function.__name__),
        setup=setup,
        number=iterations
    )
    print('[{}] Value {: <8} found in haystack of size {: <8} at index ' \
          '{: <8} in {:.2e} seconds'.format(function.__name__,
                                            needle,
                                            len(haystack),
                                            index,
                                            t / iterations))


if __name__ == '__main__':
    setup = 'from __main__ import ' \
            '(binary_search, linear_search, haystack, needle)'
    iterations = 1000

    for haystack_size in (10000, 100000, 1000000):
        haystack = list(range(haystack_size))
        for needle in (1, 6000, 9000, 1000000):
            time_and_log(linear_search, needle, haystack)
            time_and_log(binary_search, needle, haystack)
