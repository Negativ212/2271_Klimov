#1
# n = int(input())
<<<<<<< HEAD
# count = 0     
# num = 1      

=======
# count = 0
# num = 1
#
>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
# while count < n:
#     num += 1
#     prime = True
#     for d in range(2, num):
<<<<<<< HEAD
#         if num % d == 0:  
=======
#         if num % d == 0:
>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
#             prime = False
#             break
#     if prime:
#         count += 1
<<<<<<< HEAD

=======
#
>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
# print(num)

#2
# n = int(input())
# a = input().split()
<<<<<<< HEAD

# seen = []                
=======
#
# seen = []
>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
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
<<<<<<< HEAD

=======
#
>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
# best = "a"
# for c in "abcdefghijklmnopqrstuvwxyz":
#     if s.count(c) > s.count(best):
#         best = c
<<<<<<< HEAD

=======
#
>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
# print(s.replace(best, ""))

#4
# n = int(input())
<<<<<<< HEAD

# for i in range(n):
#     p = input()
#     r1 = r2 = r3 = r4 = False  
=======
#
# for _ in range(n):
#     p = input()
#     r1 = r2 = r3 = r4 = False
>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
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

<<<<<<< HEAD
#5
# ranks = ["6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# trump = input()
# n = int(input())

# result = []
# for _ in range(n):
#     r1, s1 = input().split()    # карта, которой ходят: достоинство и масть
#     r2, s2 = input().split()    # карта, которой бьют
#     if s1 == s2 and ranks.index(r2) > ranks.index(r1):
#         result.append(1)        # одна масть, и вторая старше
#     elif s2 == trump and s1 != trump:
#         result.append(1)        # бьют козырем не козырную карту
#     else:
#         result.append(0)

# print(*result)
=======

>>>>>>> 3ff2f80249c368b31a7968c07d6a9fe5f942214f
