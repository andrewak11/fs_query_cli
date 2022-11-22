#!/usr/bin/env python3
import os
import gzip
import mimetypes
import shutil

from os import listdir
from os.path import isfile, join

def filesInDirectory(mydir: str):
    onlyfiles = [ f for f in listdir(mydir) if isfile(join(mydir, f)) ]
    return onlyfiles

print(filesInDirectory('test_dir'))
print(mimetypes.guess_type('test_dir/sam3.gz'))

cur_path = os.path.dirname(__file__)

with open(os.path.join(os.getcwd(), 'test_dir/sam3.txt'), 'rb') as f:
    with gzip.open('test_dir/sam3.gz', 'wb') as zf:
        shutil.copyfileobj(f, zf)