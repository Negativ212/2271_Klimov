#1
# n = int(input())
# count = 0
# num = 1
#
# while count < n:
#     num += 1
#     prime = True
#     for d in range(2, num):
#         if num % d == 0:
#             prime = False
#             break
#     if prime:
#         count += 1
#
# print(num)

#2
# n = int(input())
# a = input().split()
#
# seen = []
# for i in range(n):
#     if a[i] not in seen:
#         seen.append(a[i])
#     if len(seen) == 3:
#         print(i + 1)
#         break
# else:
#     print(n)

#3
# s = input()
#
# best = "a"
# for c in "abcdefghijklmnopqrstuvwxyz":
#     if s.count(c) > s.count(best):
#         best = c
#
# print(s.replace(best, ""))

#4
# n = int(input())
#
# for _ in range(n):
#     p = input()
#     r1 = r2 = r3 = r4 = False
#     for c in p:
#         if c in "1234567890":
#             r1 = True
#         if c in "qwertyuiop":
#             r2 = True
#         if c in "asdfghjkl":
#             r3 = True
#         if c in "zxcvbnm":
#             r4 = True
#     if r1 and r2 and r3 and r4:
#         print("strong")
#     else:
#         print("weak")


