class A:
    def process(self):
        print("Process in A")


class B:
    def process(self):
        print("Process in B")


class C(A, B):  # Mutiple Inheritance
    # def process(self):
    #     print("Process in C")

    pass


obj = C()
obj.process()
