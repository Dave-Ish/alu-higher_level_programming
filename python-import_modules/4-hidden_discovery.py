#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in the compiled module
    module_names = dir(hidden_4)

    # Sort names alphabetically
    module_names.sort()

    # Print only names that do not start with '__'
    for name in module_names:
        if not name.startswith("__"):
            print("{}".format(name))
