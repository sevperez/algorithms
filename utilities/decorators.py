import functools
import time

def timer(func):
    """
    - Prints the runtime of the decorated function.
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print(f"Runtime of {func.__name__!r} in {run_time:.4f} seconds!")
        return value
    return wrapper_timer
