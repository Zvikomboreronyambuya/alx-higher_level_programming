#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    rem = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            rem += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (rem)
