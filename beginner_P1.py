# -*- coding: utf-8 -*-
"""
Implement a function that will flatten two lists up to a maximum given depth
"""

def _flatten(lst, depth_limit = -1):
    result = []
    if type(lst) is list:
        for item in lst:
            if depth_limit <= 0:
                result.append(item)
            elif type(item) is list:
                depth_limit-=1
                result.extend(_flatten(item, depth_limit))
            else:
                result.append(item)
    return result;

def flatten(list_a, list_b, max_depth):
    l1 = _flatten(list_a, max_depth)
    l2 = _flatten(list_b, max_depth)
    l1.extend(l2)
    return l1

a_list = [1,[2,3,[4,5,[6,7,[8]],9],10,11],12,13,14]
b_list = [3,6,9,[12,15,17,[22,24,26]]]
print '#'*40
print a_list
print '-'*40
print b_list
print '-'*40
print flatten(a_list, b_list, 2)
print '#'*40