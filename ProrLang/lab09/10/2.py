def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

def multiply(a, b, c):
    return a * b * c

banana = toint(multiply)

a = input("a: ")
b = input("b: ")
c = input("c: ")

print("Произведение:", banana(a, b, c))