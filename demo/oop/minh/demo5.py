class A:
    def __init__(self, n1):
        self.n1 = n1


class B:
    def __init__(self, n2):
        self.n2 = n2


class C(A, B):
    def __init__(self, n1, n2):
        A.__init__(self, n1)
        B.__init__(self, n2)


obj = C(10, 20)
print(obj.n1)
