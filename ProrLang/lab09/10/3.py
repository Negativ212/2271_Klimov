def toint(fun):
    def wrapper(*args):
        return fun(*map(int, args))
    return wrapper

def max_of_three(a, b, c):
    return max(a, b, c)

banana = toint(max_of_three)

a = input("a: ")
b = input("b: ")
c = input("c: ")

print("Максимум:", banana(a, b, c))