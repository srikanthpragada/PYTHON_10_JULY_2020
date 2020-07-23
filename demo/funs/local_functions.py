v1 = 100  # Global
def fun1():
    global v1
    v2 = 200  # Enclosing
    v1 = 10000
    # Local function
    def fun2():
        nonlocal v2
        v3 = 300  # Local
        v2 = v2 + 100
        print(v1, v2, v3)

    fun2()
    print(v1)

fun1()
print(v1)