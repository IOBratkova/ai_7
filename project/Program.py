from DataBase import frames

print('Hello, Im frame-program')

j = 0
for frame in frames:
    s = frame.frameToString()
    print(j, ' ', s)
    j += 1

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