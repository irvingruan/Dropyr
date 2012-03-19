#!/usr/bin/env python

# Author: Irving Ruan <irvingruan@gmail.com>

# Dropyr examines and displays the top-down view of your Dropbox directory in       # friendly ASCII art.

# See README for instructions on how to use Dropyr

import os
import sys

def find_dropbox_directory():
	homePath = os.path.expanduser("~/")

	for root, subFolders, files in os.walk(homePath):
	    for sf in subFolders:
			if sf.lower() == "dropbox":
				return os.path.join(root, sf)
				
	sys.stdout.write("Cannot find Dropbox directory!\n")
			
def usage():
	sys.stderr.write("Usage: ./Dropyr.py\n")

def generate_dropbox_tree(dir, padding, displayFilesFlag):
    sys.stdout.write(padding[:-1] + '+-' + os.path.basename(os.path.abspath(dir)) + '/\n')
    padding = padding + '\t'
    files = []
    if displayFilesFlag:
        files = os.listdir(dir)
    else:
        files = [x for x in os.listdir(dir) if os.path.isdir(dir + sep + x)]
    count = 0
    for file in files:
        count += 1
        sys.stdout.write(padding + '|\n')
        path = dir + os.sep + file
        if os.path.isdir(path):
            if count == len(files):
                generate_dropbox_tree(path, padding + ' ', displayFilesFlag)
            else:
                generate_dropbox_tree(path, padding + '|', displayFilesFlag)
        else:
            sys.stdout.write(padding + '+-' + file + '\n')

def main():
	if len(sys.argv) != 1:
		usage()

	dropboxRootDir = find_dropbox_directory()
	generate_dropbox_tree(dropboxRootDir, "\t", True)	

if __name__ == "__main__":
	main()
	
	
		
	
	
		
	
	
	