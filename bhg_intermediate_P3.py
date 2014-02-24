# -*- coding: utf-8 -*-
"""
Write a function decorator that tracks how long the execution of the wrapped function took.
The decorator will log slow function calls including details about the execution time and function name.
The decorator should take an optional threshold argument
"""
import time

def time_slow(threshold=-1):
    def real_decorator(f):
        def wrapper_decorator(*args, **kwargs):
            print 'Threshold: ', threshold
            start = time.time() * 1000
            result = f(*args, **kwargs)
            stop = time.time() * 1000
            print 'Execution: {0} ms'.format(stop - start)
            return result
        return wrapper_decorator
    return real_decorator

@time_slow()
def f1():
    print 'f1() is to sleep for 1 sec'
    time.sleep(1)

@time_slow(threshold=1)
def f2():
    print 'f2() is to sleep for 2 sec'
    time.sleep(2)

print '-'*40
f1()
print '-'*40
f2()
print '-'*40