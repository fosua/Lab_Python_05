#a
def do(thing):
    return str(thing) + str(1)
print do(5)
print ''
# b
def do(one, two= 5):
    return one + two
print do (5)
print ''
#c
def do (a,b):
    a = 5
    b = 5
    return a * b
inp = 8
do (inp, 5)
print inp
def try_to_change_list_contents(the_list):
    the_list.append('four')
outer_list = ['one', 'two', 'three']
try_to_change_list_contents(outer_list)
print outer_list
print ''
def do (a, f):
    return a*f(a)
def inp (a):
    return a*2
print do (6, inp)
"""51

10

8
['one', 'two', 'three', 'four']

72
"""
