#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    p = 1
    args = sys.argv[1:]
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print(len(sys.argv) - 1, "argument:")
    else:
        print(len(sys.argv) - 1, "arguments:")
    for i in range(len(args)):
        print("{}: {}".format(p, args[i]))
        p += 1
