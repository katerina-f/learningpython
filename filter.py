"""
 Returns  iterator
"""

# filter(func, iterable)

def has_o(string):
    return "o" in string.lower()

l = ["one", "two", "three", "373773"]

n1 = filter(has_o, l)
print(n1)


newl = filter(lambda string: 'o' in string.lower(), l)
print(newl)


nl = [string for string in l if has_o(string)]
print(nl)
