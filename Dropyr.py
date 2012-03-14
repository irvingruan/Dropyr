#!/usr/bin/env python

# Author: Irving Ruan
# Contact: irvingruan@gmail.com

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Dropyr examines and displays the top-down view of your Dropbox directory in friendly ASCII art.
# To run, simply type: ./Dropyr.py

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
	
	
		
	
	
		
	
	
	