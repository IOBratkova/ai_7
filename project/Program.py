print('Hello, Im frame-program')

from Basic import frames

frames[0].print_frame()



"""
class A:
    def __init__(self, v):
        self.v = v

    def print_v(self):
        print(self.v)


a = A(10)
a.v = 55
a.print_v()

f = a.print_v
a.v = 199
f()


>>> a = A()
>>> a.v = 91
>>> a.print_me()
91
>>> f = a.print_me
>>> a.v = 155
>>> f()
155
>>>
"""