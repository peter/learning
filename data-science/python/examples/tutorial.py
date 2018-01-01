#!/usr/bin/env python

import sys

def print_header(header):
    print("\n## " + header)

def read_stdin(number_of_lines = 5):
    return "\n".join(sys.stdin.readlines()[:number_of_lines])

def read_stdin_by_line():
    for line in sys.stdin:
        print(line)

def shelling_out():
    import subprocess
    cmd = "ls -l"
    return subprocess.check_output(cmd, shell = True)

# NOTE: alternative approach is to symlink a .py file to the file
def import_script_file(module_name, dir):
    import imp
    path = dir + '/' + module_name
    return imp.load_source(module_name, path)

def read_file(path):
    return open(path, "r").read()

def write_file(path, data):
    open(path, "w").write(data)

def read_json(json_str):
    import json
    return json.loads(json_str)

def write_json(data):
    import json
    return json.dumps(data)

def main():
    if not sys.stdin.isatty():
        print_header("Reading stdin")
        print(read_stdin())

    print_header("Shelling out")
    print(shelling_out())

    print_header("Import script file without .py extension")
    print(import_script_file('huuid', './bin').huuid())

    path = "/tmp/python-tutorial-file"
    data = {'message': 'some file data', 'foo': 123}
    print_header("Write json data to file with open().write()")
    print("Write: %s" % data)
    write_file(path, write_json(data))

    print_header("Read json data from file with open().read()")
    print("Read: %s" % read_json(read_file(path)))

if __name__ == "__main__":
    main()
