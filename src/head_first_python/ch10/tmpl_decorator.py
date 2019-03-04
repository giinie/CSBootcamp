from functools import wraps


def decorator_name(func: object) -> object:
    @wraps(func)
    def wrapper(*args, **kwargs):
        ##############################################################
        # if 'logged_in' in session:
        #     return func(*args, **kwargs)
        # return 'You are NOT logged in.'
        ##############################################################
        # 1. Code to execute BEFORE calling the decorator function.
        #
        # 2. Call the decorated function as required, returning its
        #    results if needed.
        return func(*args, **kwargs)
        #
        # 3. Code to execute INSTEAD of calling the decorated function.
    return wrapper
