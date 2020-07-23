import functools
from ansibleawx.exceptions import LoginRequiredError

def require_auth(function):
    """
    A decorator that wraps the passed in function and raises exception
    if headers with token is missing
    """
    @functools.wraps(function)
    def wrapper(self, *args, **kwargs):
        if not self.headers:
            raise LoginRequiredError
        return function(self, *args, **kwargs)
    return wrapper