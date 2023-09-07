#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as args
    result = 0
    args_len = len(args) - 1
    for i in range(1, args_len + 1):
        result += int(args[i])
    print("{}".format(result))
