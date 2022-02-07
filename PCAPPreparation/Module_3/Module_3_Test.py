"""Question 6"""
class Ex(Exception):
    def __init__(self, msg):
        super().__init__(msg +  msg)
        #self.args = (msg,)


"""try:
    raise Ex("Ex")
except Ex as e:
    print(e)
except Exception as e:
    print(e)"""

#Item 9
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B,A):
    def c(self):
        self.a()

o = C()
print(o.c())
