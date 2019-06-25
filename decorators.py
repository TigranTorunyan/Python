import functools
import time

def repeat(num_times):  
    def do_twice(func):
        @functools.wraps(func)
        def wrapper_do_twice(*args, **kwargs):
            for _ in range(num_times):
                val = func(*args, **kwargs)
            return val
        return wrapper_do_twice
    return do_twice

''' Model for more complex decorators'''
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # DO something before
        value = func(*args, **kwargs)
        # DO something after
        return value
    return wrapper_decorator


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print("Finished {0!r} in {1:.4f} secs".format(func.__name__, run_time))
        return value
    return wrapper_timer


