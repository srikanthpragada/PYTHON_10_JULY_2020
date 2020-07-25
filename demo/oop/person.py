# Private attributes demo

class Person:
    def __init__(self,name, email):
        # Private attributes
        self.__name = name
        self.__email = email

    def print_details(self):
        print('Name   :', self.__name)
        print('Email  :', self.__email)


p = Person("Bill", "bill@microsoft.com")
# p._Person__name = "Bill Gates"
print(p.__dict__)
p.print_details()
