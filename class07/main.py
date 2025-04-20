# def mysum(a:int, b:int=1):
#     return a+b

# print(mysum(10,3))

# =============================================================

# mysum = lambda x, y: x + y
# print(mysum(10, 2))

# =============================================================

# lst1 = [("Bilal", 4), ("Jahanzab", 1), ("ali", 3)]
# lst1.sort(key=lambda x: x[1])
# print(lst1)

# =============================================================

# lst1 = [("Bilal", 4), ("Jahanzab", 1), ("ali", 3)]
# lst1.sort(key=lambda x: len(x[0]))
# print(lst1)

# =============================================================

# def counter(x):
#     print(x)
#     if x <= 0:
#         return True
#     counter(x - 2)
# # x = 3
# # counter(2)
# # counter(1)
# # counter(0)
# counter(10)

# =============================================================

# def counter(x):
#     for i in range(x,0,-1):
#         print(i)
# counter(10)
