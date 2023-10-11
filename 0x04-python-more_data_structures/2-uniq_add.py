#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_intergers = set()
    sum = 0
    for num in my_list:
        if num not in uniq_intergers:
            sum += num
            uniq_intergers.add(num)
    return sum
