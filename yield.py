"""
yield returns one element per call.
We need to call func (as next(g)) if we want to get element or get loop
for this object.
func with construction yield is a generator object, as well iterable object.
"""

def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -=1

g = gen_countdown(5)  # it is a generator object

list = [i for i in g]  # we can make list from generator object

print(list)
