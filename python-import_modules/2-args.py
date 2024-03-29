#!/use/bin/python3
if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print("1 argument:")
    elif num_args == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(num_args))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
