#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            if isinstance(item, int):
                print("{:d}".format(item), end=' ')
                count += 1
        print()
    except (IndexError, TypeError, ValueError):
        print("Error: Index out of range")
    return(count)
