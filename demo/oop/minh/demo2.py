class A:
    def process(self):
        print("Process in A")


class B(A):
    def task(self):
        print("Task in B")


class C:
    def process(self):
        print("Process in C")


class D(B, C):
    pass


obj = D()
obj.process()
