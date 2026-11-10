a = list(range(10))
b = []
for x in a:
    b.append(a.pop() - x)
print(*b)