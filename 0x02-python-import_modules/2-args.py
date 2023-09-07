#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_len = len(argv) - 1
    print("{} arguments:".format(args_len))
    for args in range(1, args_len):
        print("{}: {}".format(args, argv[args]))
