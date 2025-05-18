# x = int(input("enter a number : "))
# #   statement if-condition else-condition statement
# a = x + 2 if x >= 10 else x - 2
# print(a)

# if x >= 10:
#     print("number is greater then 10")
# else:
#     print("number is less then 10")


# percentage = int(input("Enter your percentage : "))

# if percentage >= 70:
#     print("A+")
# elif percentage >= 60 and percentage < 70:
#     print("B grade")
# elif percentage >= 50 and percentage < 60:
#     print("C grade")
# elif percentage >= 40 and percentage < 60:
#     print("D grade")
# else:
#     print("fail")\


# ==================================================

# a = [x for x in range(1,6) if x>=3]
# print(a)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def main(x):
#     return x + 10

# a = list(map(main, lst))
# print(a)
# for x in lst:
#     print(x,end="-")

# ============================================

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #main = lambda x: x + 100

# a = list(map(lambda x: x + 200, lst))
# print(a)


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in enumerate(lst, start=4):
#     print(i)

# x = 20
# def myfunc():
#     x = 10
#     print(x)

# print(x)
# myfunc()
# print(x)

# def hello():
#     """hyeh sik function hsi

#     jo dring retun kerta hai"""
#     return "hello"

# hello.__doc__()


def a():
    a1 = 1
    b1 = b()
    c1 = b1 + a1
    return c1


def b():
    a1 = 1 + 2
    return b()


print(a())

"""
    Heap
    - Persistent (stored for long period) : It used for long-lived data. Memory allocated on the heap stays there until it's explicitly freed or it is garbage collected
    - Large area compared to the stack : The operating system can allocate a large block of memory on the heap and it is generally slower than stack memory
    - Dynamic memory allocation : Memory on the heap is allocated dynamically during program execution
    - Stored randomly : data can be scattered in the memory space. It is not contiguous like stack memory
    - Garbage collection : is used to freed the occupied memory else it leads to memory leaks
    - Stores objects (int, list, dictionary, class, functions) : Dynamic memory is allocated during the program's execution

    Stack
    - Temporary or Short-lived storage : stack memory is used for short-lived data. It stores temporary data
    - Smaller area as compared to heap : The size of the stack is usually limited and can result in a stack overflow if you use too much memory 
    - Static memory allocation : The size and structure are determined at compile time. The operating system manages it.
    - LIFO (last in fist out) : last item pushed onto the stack is the first one to be popped off when the function exits
    - Automatic cleanup : When a function exits, the memory used by its local variables is automatically freed
    - Store function calls : Stack stores data related to functions calls like Function parameters,Return addresses, Local variables, Control flow data 


    A memory leak occurs when a programmer allocates memory but fails to release it back to the system after its use is complete. Over time, memory leaks can cause an application to consume more and more memory, potentially leading to performance problems and crashes
"""
