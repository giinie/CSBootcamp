from collections import namedtuple


def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


it = my_coroutine()
next(it)
it.send('First')
it.send('Second')
print('-' * 50)


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)


it = minimize()
next(it)
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))
print('-' * 50)

ALIVE = '*'
EMPTY = '-'

Query = namedtuple('Query', ('y', 'x'))


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)
    ne = yield Query(y + 1, x + 1)
    e_ = yield Query(y + 0, x + 1)
    se = yield Query(y - 1, x + 1)
    s_ = yield Query(y - 1, x + 0)
    sw = yield Query(y - 1, x - 1)
    w_ = yield Query(y + 0, x - 1)
    nw = yield Query(y + 1, x - 1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


it = count_neighbors(10, 5)
q1 = next(it)
print('First yield:', q1)
q2 = it.send(ALIVE)
print('Second yield:', q2)
q3 = it.send(ALIVE)
print('...')
q4 = it.send(EMPTY)
q5 = it.send(EMPTY)
q6 = it.send(EMPTY)
q7 = it.send(EMPTY)
q8 = it.send(EMPTY)
try:
    count = it.send(EMPTY)
except StopIteration as e:
    print('Count:', e.value)
print('-' * 50)

Transition = namedtuple('Transition', ('y', 'x', 'state'))


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors > 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
        return state


def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


it = step_cell(10, 5)
q0 = next(it)
print('Me:', q0)
q1 = it.send(ALIVE)
print('Q1:', q1)
print('...')
q2 = it.send(ALIVE)
q3 = it.send(ALIVE)
q4 = it.send(ALIVE)
q5 = it.send(ALIVE)
q6 = it.send(EMPTY)
q7 = it.send(EMPTY)
q8 = it.send(EMPTY)
t1 = it.send(EMPTY)
print('Outcome:', t1)
print('-' * 50)

