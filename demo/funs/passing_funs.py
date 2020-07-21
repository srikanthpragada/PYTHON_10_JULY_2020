# func,value,value
def math_op(oper, n1, n2):
    return oper(n1, n2)


def multiply(n1, n2):
    return n1 * n2

def power(n1,n2):
    return n1 ** n2

print(math_op(multiply, 10, 20))
print(math_op(power, 10, 20))
