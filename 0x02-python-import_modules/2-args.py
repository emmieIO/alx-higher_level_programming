#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args_len = len(argv) - 1
    if args_len == 0:
        print("{} arguments.".format(args_len))
    else:
        print("{} arguments:".format(args_len))
        for args in range(1, args_len + 1):
            print("{}: {}".format(args, argv[args]))
