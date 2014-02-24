# -*- coding: utf-8 -*- #
""" #
Merge 2 objects with any depth (including contained dictionaries, lists, sets, strings, integers, floats). #
Type mismatches should yield a tuple with the two elements #
""" #

a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]} #
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"} #
x = {'x': [1,2,3,4,5,6], 'y': 5, 'z': set([1,2,3,4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3,2]}, 'm': ([1], "wer")} #

def merge(a, b): #
    if type(a) is type(b) is int: #
        return a + b #
    elif type(a) is type(b) is str: #
        return a + b #
    elif type(a) is type(b) is list: #
        return a + b #
    elif type(a) is type(b) is set: #
        return a | b #
    elif type(a) is type(b) is dict: #
        result = dict(a) #
        for k,v in b.iteritems(): #
            if k in result: #
                result[k] = merge(result[k],v) #
            else: #
                result[k] = v #
        return result #
    else: #
        return (a, b) #

print '#'*40 #
print a #
print '-'*40 #
print b #
print '-'*40 #
print merge(a,b) #
print '#'*40 #