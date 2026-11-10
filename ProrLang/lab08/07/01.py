a = list(map(int, input().split()))
for x in a:
    if x < 0:
        print("Нашли отрицательное:", x)
        break
else:
    print("Отрицательных нет")