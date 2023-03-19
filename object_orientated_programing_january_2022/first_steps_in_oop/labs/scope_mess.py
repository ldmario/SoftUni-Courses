x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)
        print("outer:", x)

    def change_global():
        x = print("global: changed!")

    print("outer:", x)
    inner()
    change_global()


print(x)
outer()
