#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
from urllib.error import HTTPError

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  FILE_NAME_PATTERN = '^\w+_(.*)$'
  LOG_PATTERN = '(\d+\.\d+\.\d+\.\d+).* "GET\s+([^\s]+)\s+([^/]+)/.*\n'
  match = re.search(FILE_NAME_PATTERN, filename)
  host = ''
  if match:
      host = match.group(1)
  else:
      print('Filename doesnt comply pattern')
      exit(1)
  f = open(file=filename, mode='r')
  tuples = re.findall(r'%s' % LOG_PATTERN, f.read())
  urlDict = {}
  for tuple in tuples:
      
      extractedUrl  = tuple[2].lower() + '://www.' + host + tuple[1]
      count = urlDict.get(extractedUrl, 0)
      if count > 0: 
          print('fromip=%s url=%s' %(tuple[0], extractedUrl))
      urlDict[extractedUrl] = count + 1;
  return sorted(urlDict.keys())
  
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if os.path.exists(dest_dir) == False:
      os.mkdir(dest_dir)
  indexHtml = '''<verbatim>
                <html>
                <body>
                %s
                </body>
                </html>''';
  pathToImages = []
  for idx in range(len(img_urls)):
    urlToFile = img_urls[idx]
    try:
        filename = 'img%d' % idx
        pathToFile = os.path.abspath(os.path.join(dest_dir, filename))
        urllib.request.urlretrieve(url=urlToFile, filename=pathToFile);
        pathToImages.append('<img src="%s">' % pathToFile)
    except HTTPError:
        print('url %s 404 not found' % urlToFile)
  htmlForImages = ''.join(pathToImages)
  indexHtml = indexHtml % htmlForImages
  indexFile = os.path.join(dest_dir, 'index.html')
  
  f = open(indexFile, 'w')
  #os.write(indexFile, indexHtml)
  print(indexHtml, file=f)  
  f.close()
  
def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  print(img_urls)
  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()
