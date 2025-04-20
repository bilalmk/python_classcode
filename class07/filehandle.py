# f = open("abc.txt", "r")
# f.seek(5)
# print(f.tell())
# content = f.read()
# print(f.tell())
# print(content)
# f.close()

# =============================================================

# f = open("ab.txt","w")
# f.write("Hello sir ratan  how are you...\n hello sir bilal")
# f.close()

# =============================================================

# f = open("a.txt","r+")
# f.seek(5)
# f.write("fareed")
# f.close()

# =============================================================

# f = open("abcd.txt","x")
# f.write("i am student...")
# f.close()

# =============================================================

# with open("a.txt","r") as f:
#     content = f.read()
#     print(content)

# =============================================================

with open("a.txt", "w") as f:
    f.write("hello sir bilal\ni am student of giaic...")
