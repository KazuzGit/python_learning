from itertools import count
from itertools import cycle

def count_func(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)
def cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1

count_func(start_num = 3, stop_num = 10)
cycle_func(my_list = [3, 10, 11], iteration = int(input("enter iteration: ")))