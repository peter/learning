import sys

def first_arg_or_stdin():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return sys.stdin.read().rstrip("\r\n")
