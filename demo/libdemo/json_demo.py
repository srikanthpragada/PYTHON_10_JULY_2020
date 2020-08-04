import json


class Contact:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile


c = Contact("Abc", "39393944")
cl = [Contact("Abc", "39393944"), Contact("Xyz", "494949444")]

s = json.dumps(c.__dict__)
print(s)

s = json.dumps([c.__dict__ for c in cl])
print(s)
