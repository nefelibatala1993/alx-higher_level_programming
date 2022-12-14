#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    except TypeError as err:
        print("Exception: {}".format(err), file=sys.stderr)
    else:
        return True
    return False
