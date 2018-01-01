# -*- coding: UTF-8 -*-

import os
import sys
import re

# TODO: is this needed?
reload(sys)
sys.setdefaultencoding('utf-8')

def env(name):
    return os.environ.get(name)

def script_dir(file):
    return os.path.dirname(os.path.realpath(file))

def flatten(list):
    return [item for sublist in list for item in sublist]

def extract(pattern, string):
    match = re.match(pattern, string)
    return match.groups() if match else ()
