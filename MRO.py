class A:
    def rk(self):
        print("In Class A")

class B(A):
    def rk(self):
        print("In Class B")

class C(A):
    def rk(self):
        print("In Class C")

class D(B, C):
    pass

r = D()
r.rk()