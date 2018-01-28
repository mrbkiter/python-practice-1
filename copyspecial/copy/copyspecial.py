#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
# import commands
from builtins import dir
from sys import path
import zipfile

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(path_to_folder):
    specialPaths = []
    SPECIAL_PATH_PATTERN = '^.*__\w+__[^\\/]*$'
    paths = os.listdir(path_to_folder)
    for path in paths:
        absPath = os.path.abspath(os.path.join(path_to_folder, path))
        match = re.search(r'%s' % SPECIAL_PATH_PATTERN, absPath)
        if match: 
            print(match.group())
            specialPaths.append(absPath)


def copy_to(sourcePath, targetPath):
    #print('copy to folder %s' % targetPath)
    if os.path.exists(targetPath) == False: 
        os.mkdir(targetPath)
    #absSource = os.path.abspath(sourcePath)
    #absTarget = os.path.abspath(targetPath)
    paths = os.listdir(sourcePath)
    for filename in paths:
        path = os.path.join(sourcePath, filename)
        if os.path.isdir(path):
            #copy_to(path, os.path.join(targetPath, filename))
            print('we dont support copying folder in folder. Folder %s would be skipped' %filename)
        #absPath = os.path.abspath(os.path.join(path_to_folder, path))
        else:
            print('copying file %s to folder %s' % (filename, targetPath))
            copiedFile = shutil.copy(path, targetPath)

def zip(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print ('zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname))
            zf.write(absname, arcname)
    zf.close()
    
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)
  
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    
    sys.exit(1)
  for arg in args:
      get_special_paths(arg)
      if todir:
          copy_to(arg, todir)
      if tozip:
          zip(arg, tozip)
  # +++your code here+++
  # Call your functions

  
if __name__ == "__main__":
  main()
  '''str = '/aaa/bbb/ccc'
  match = re.search(r'.*', str)
  if match: 
      print(match.group())'''
