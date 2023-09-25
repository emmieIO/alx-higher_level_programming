#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for value in my_list:
            if count >= x:
                break
            
            try:
                integer_value = int(value)
                print("{:d}".format(integer_value), end=' ')
                count += 1
            except (ValueError, TypeError):
                continue  # Ignore non-integer values
            
        print()  # Print a newline to end the line
        return count
    except TypeError:
        raise TypeError("Input list must be iterable")

