#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Calculate the number of user-passed arguments (excluding script name)
    count = len(sys.argv) - 1

    # Print the summary header line with dynamic punctuation and word forms
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    # Print each argument along with its 1-indexed positional marker
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
