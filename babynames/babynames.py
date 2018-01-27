#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from builtins import sorted

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  result = []
  names = {}
  # Open file
  f = open(filename, 'r')
  year = re.search(r'Popularity\s+in\s+(\d+)' , f.read())
  if year:
      result.append(year.group(1))
  f.seek(0)
  # Feed the file text into findall(); it returns a list of all the found strings
  #tuples = re.findall(r'<tr.+><td>\d+</td><td>(\w*)</td><td>(\w*)</td></tr>', f.read())
  tuples = re.findall(r'<tr.+><td>(\d+)</td><td>(\w*)</td><td>(\w*)</td>', f.read())
  f.close()
  for row in tuples:
      rank = row[0] 
      boy = row[1]
      girl = row[2]
      #print(name[0] + ' ' + name[1])
      names[boy] = rank
      names[girl] = rank
  #print(dict)
  #print(s.group())
  sorted_names = sorted(names.items(), key=lambda k: k[0])
  for sortedName in sorted_names: 
      result.append('%s %d' % (sortedName[0], int(sortedName[1]))) 
  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
#if __name__ == '__main__':
  #main()
result = extract_names('baby1994.html')
print(result)
#match = re.search(r'iii', 'piiig') #=>  found, match.group() == "iii"
'''text = r'<tr align="right"><td>118</td><td>Luke</td><td>Sabrina</td></tr>'
tuples = re.findall(r'<tr.+><td>\d+</td><td>(\w*)</td><td>(\w*)</td></tr>', text)
for n in tuples:
    print(n[0] + ' ' + n[1])'''
#if match:
#    print('found: %s' % match.group())  
