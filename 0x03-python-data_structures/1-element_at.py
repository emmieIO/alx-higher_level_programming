#!/usr/bin/python3
def element_at(my_list, idx):
    if int(idx) < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return int(my_list[idx])
