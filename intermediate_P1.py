# -*- coding: utf-8 -*-
"""
Given a dictionary, swap keys <-­‐> values.
The program should use some custom logic to check if the swap is possible,
but without using try..except constructs or the __hash__() function
"""

def swap_dict(d):
    #return dict(zip(d.values(), d.keys()))
    #return dict((value, key) for key, value in d.iteritems())
    result = {}
    for k,v in d.iteritems():
        if type(v) in [list, set, dict, tuple]:
            return 'Swap is not posible'
        else:
            result[v] = k
    return result

print '-'*40
d =  {'a': 123, 'b': 456}
print 'Input: ', d
print 'Output: ', swap_dict(d)
print '-'*40

d =  {'a': (1, 2, [3])}
print 'Input: ', d
print 'Output: ', swap_dict(d)
print '-'*40