dc = {"name": "Jamal", "age": 20, "email": "bilalmk@gmail.com"}

# try:
#     print(dc["role"])
# except Exception as e:
#     print(e)

# print("Hello world")

# =============================================================

# try:
#     print(dc["role"])
# except KeyError as e:
#     print(f"key {e} not found")
# except Exception as e:
#     print(e)

# =============================================================

# try:
#     print(dc["name"])
#     a = 10/0
#     print(a)
# except ZeroDivisionError as e:
#     print("can not divided by zero")
# except KeyError as e:
#     print(f"key {e} not found")

# print("hello world")

# =============================================================

# try:
#     print(dc["name1"])
#     a = 10/0
#     print(a)
# except Exception as e:
#     print(e)

# print("hello world")

# =============================================================

# try:
#     num1 = input("Enter first number : ")
#     num2 = input("Enter second number : ")
#     print(dc["name"])
#     a = int(num1) / int(num2)
#     print(a)
# except ValueError as e:
#     print("only numbers are allowed")
# except TypeError as e:
#     print("invalid input")
# except ZeroDivisionError as e:
#     print("can not divided by zero")
# except KeyError as e:
#     print(f"key {e} not found")

# print("hello world")

# =============================================================

# try:
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))
#     if num1 < 0 or num2 < 0:
#         raise ValueError("Negative numbers are not allowed")
#     a = int(num1) / int(num2)
#     print(a)
# except ValueError as e:
#     print(e)
# except TypeError as e:
#     print("invalid input")
# except ZeroDivisionError as e:
#     print("can not divided by zero")

# =============================================================

# class NegativeNumberException(Exception):
#    pass


# try:
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))
#     if num1 < 0 or num2 < 0:
#         raise NegativeNumberException("Negative numbers are not allowed")
#     if num1 == 10:
#         raise Exception("Testing")
#     a = int(num1) / int(num2)
#     print(a)
# except Exception as e:
#     print(e)
# except NegativeNumberException as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except TypeError as e:
#     print("invalid input")
# except ZeroDivisionError as e:
#     print("can not divided by zero")
# except Exception as e:
#     print(e)

# =============================================================

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    if num1 < 0 or num2 < 0:
        raise Exception("Negative numbers are not allowed")
    if num1 == 10:
        raise Exception("Testing")
    a = int(num1) / int(num2)
    print(a)
except Exception as e:
    print(e)
else:
    print("code executed successfully")
finally:
    print("code completed")
