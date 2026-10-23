#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    # Loop through each argument starting from the first user input
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
