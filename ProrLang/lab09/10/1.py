def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

def add(a, b):
    return a + b

banana = toint(add)

x = input("Первое число: ")
y = input("Второе число: ")

print(banana(x, y))