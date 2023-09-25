#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        index = 0
        while count < x:
            value = my_list[index]
            if isinstance(value, int):
                formatted_value = "{:d}".format(value)
                print(formatted_value, end='')
                count += 1
            index += 1
        print()

        return count
    except IndexError:
        return count
