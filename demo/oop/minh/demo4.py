class A:
    def process(self):
        print("Process in A")


class B(A):
    def process(self):
        print("Process in B")


class C(B, A):
    pass


print(C.mro())
