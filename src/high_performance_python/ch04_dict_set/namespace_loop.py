from math import sin


def tight_loop_slow(iterations):
    result = 0
    for i in range(iterations):
        # this call to sin requires a global lookup
        result += sin(i)


def tight_loop_fast(iterations):
    result = 0
    local_sin = sin
    for i in range(iterations):
        # this call to local_sin requires a local lookup
        result += local_sin(i)

