# -*- coding: utf-8 -*-
"""
Given a binary tree encoded as a tuple (node_label, left_node_tuple, right_node_tuple),
write an iterator / generator that returns the nodes of the tree in pre-order
"""

class BTreeTupleIterator(object):

    def __init__(self, obj):
        self.lst = self._flatten(obj)
        self.pos = 0

    def __iter__(self):
        return self

    def next(self):
        if(self.pos >= len(self.lst)):
            raise StopIteration
        elem = self.lst[self.pos]
        self.pos+=1
        return elem

    def _flatten(self, lst):
        result = []
        for item in lst:
            if item is not None:
                if type(item) is tuple:
                    result.extend(self._flatten(item))
                else:
                    result.append(item)
        return result

node = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
print '-'*40
print 'Input:', node
print '-'*40
s = ''
for val in BTreeTupleIterator(node):
    s += val + ' '
print 'Output: ', s
print '-'*40