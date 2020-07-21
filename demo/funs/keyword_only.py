# Keyword args only
def fun(*, a, b):
    pass


fun(a=10, b=20)
# fun(10, 20)
fun(b=10, a=50)
