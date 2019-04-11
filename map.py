
"""
map() returns iterator, which need to be iterated
"""

# map(func, *iterable)

def upper(str):
    return str.upper()

l = ["one", "two", "three"]

new_list = list(map(upper, l))
print(new_list)

new_l = list(map(lambda string: string.upper(), l))

print(new_l)
