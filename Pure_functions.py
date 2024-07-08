#Map function

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))

#filter
my_list = [4,5,6]

def only_odd(item):
    return item %2 != 0

print(list(filter(only_odd, my_list)))

#zip
your_list = [7,8,9]

print(list(zip(my_list, your_list)))

#reduce
from functools import reduce
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, my_list, 10))