#!/usr/bin/env python3

from os import listdir
from os import isfile, join

def filesInDirectory(mydir: str):
    onlyfiles = [ f for f in listdir(mydir) if isfile(join(mydir, f)) ]
    return onlyfiles

print(filesInDirectory('test_dir'))
