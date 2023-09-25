#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            numerator = my_list_1[i]
            denominator = my_list_2[i]
            if not isinstance(numerator, (int, float)) or not
            isinstance(denominator, (int, float)):
                raise TypeError("wrong type")
            if denominator == 0:
                raise ZeroDivisionError("division by 0")
            division_result = numerator / denominator
            result.append(division_result)
        except (ZeroDivisionError, TypeError, IndexError) as e:
            print(e)
            result.append(0)
    return result
