#!/usr/bin/env python2.7

# A script that checks whether files passed as arguments are the same

from hashlib import md5
from sys import argv, exit
from fileinput import input

# Omit script name which is the first argument
file_list = argv[1:]

def get_hash(filename):
    # Handle wrong filename exception
    try:
        # Automatically clean up after the job is done
        with open(filename,'r') as f:
                data = f.read()
                return md5(data).hexdigest()
    except IOError:
        print "Could not read the file."
        print "Is the filename correct?"
        exit(1)



file_hashes = [get_hash(filename) for filename in file_list]
unique_hashes = set(file_hashes)


if len(unique_hashes) == 1:
    if __name__ == '__main__':
        print "Matching!"
    exit(0)
else:
    if __name__ == '__main__':
        print "Different!"
    exit(1)
