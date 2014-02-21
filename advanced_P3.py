# -*- coding: utf-8 -*-
"""
Implement a singleton pattern using meta classes
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(object):
    __metaclass__ = Singleton

    def __init__(self, name):
        self.name = name
        print 'Constructor ', self.name, ' @', id(self)

    def say_hello(self):
        print 'Instance: ', self.name, ' says hello'

c = MyClass('A')
c.say_hello()
d = MyClass('B')
d.say_hello()