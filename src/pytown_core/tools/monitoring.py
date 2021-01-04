import logging
import functools
import time


def timeit(method):
    @functools.wraps(method)
    def wrapper_timeit(*args, **kwargs):
        start_time = time.perf_counter()
        value = method(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        logging.debug("TIMED : {} run in {}".format(method.__name__, run_time))
        return value

    return wrapper_timeit
