import copyreg
import pickle


# class GameState(object):
#     def __init__(self):
#         self.level = 0
#         self.lives = 4
#
#
# state = GameState()
# state.level += 1
# state.lives -= 1
#
#
# state_path = 'game_state.bin'
# with open(state_path, 'wb') as f:
#     pickle.dump(state, f)
#
# with open(state_path, 'rb') as f:
#     state_after = pickle.load(f)
# print(state_after.__dict__)
# print('-' * 50)
#
#
# class GameState(object):
#     def __init__(self):
#         self.level = 0
#         self.lives = 4
#         self.points = 0
#
#
# state = GameState()
# serialized = pickle.dumps(state)
# state_after = pickle.loads(serialized)
# print(state_after.__dict__)
# print('-' * 50)
#
# with open(state_path, 'rb') as f:
#     state_after = pickle.load(f)
# print(state_after.__dict__)
# print(isinstance(state_after, GameState))
# assert isinstance(state_after, GameState)
# print('-' * 50)


# class GameState(object):
#     def __init__(self, level=0, lives=4, points=0):
#         self.level = level
#         self.lives = lives
#         self.points = points
#
#
# def pickle_game_state(game_state):
#     kwargs = game_state.__dict__
#     return unpickle_game_state, (kwargs,)
#
#
# def unpickle_game_state(kwargs):
#     return GameState(**kwargs)
#
#
# copyreg.pickle(GameState, pickle_game_state)
# state = GameState()
# state.points += 1000
# serialized = pickle.dumps(state)
# state_after = pickle.loads(serialized)
# print(state_after.__dict__)
# print('-' * 50)
#
#
# class GameState(object):
#     def __init__(self, level=0, lives=4, points=0, magic=5):
#         self.level = level
#         self.lives = lives
#         self.points = points
#         self.magic = magic
#
#
# state_after = pickle.loads(serialized)
# print(state_after.__dict__)
# print('-' * 50)


class BetterGameState(object):
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic


# pickle.loads(serialized)


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs['version'] = 2
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    version = kwargs.pop('version', 1)
    if version == 1:
        kwargs.pop('lives')
    return BetterGameState(**kwargs)


copyreg.pickle(BetterGameState, pickle_game_state)

state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized[:35])
# state_after = pickle.loads(serialized)
# print(state_after.__dict__)
# print('-' * 50)

