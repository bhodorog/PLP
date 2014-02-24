# -*- coding: utf-8 -*- #
""" #
Write a generator that returns all the subsets of a given set #
""" #

from itertools import combinations #

class SubsetGenerator(object): #

    def __init__(self, obj): #
        self.lst = self._build_combibations(obj) #
        self.pos = 0 #

    def __iter__(self): #
        return self #

    def next(self): #
        if(self.pos >= len(self.lst)): #
            raise StopIteration #
        elem = self.lst[self.pos] #
        self.pos+=1 #
        return elem #

    def _build_combibations(self, obj): #
        l = [] #
        for i in range(len(obj)): #
            c = combinations(obj,i) #
            for t in c: #
                l.append(set(list(t))) #
        l.append(obj) #
        return l #


val = set([1, 2, 3]) #
print '-'*40 #
print 'Input:', val #
print '-'*40 #
s = '' #
for val in SubsetGenerator(val): #
    s += val.__str__() + ', ' #
print 'Output: ', s #
print '-'*40 #