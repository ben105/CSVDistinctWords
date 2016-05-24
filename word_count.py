"""
Word Counting

This Python script will take a CSV file as input, and output all unique words
in a given column, as well as the number of occurences. The first argument to
this script must be the path to the CSV file. The second argument must be the
column name (case sensitive).

usage: 
C:\Python27\Python.exe word_count.py C:\users\eriknix\Desktop\sample.csv Column
"""

# The csv module implements classes to read and write tabular data in CSV 
# format.
import csv

# This module provides access to some variables used or maintained by the
# interpreter. This script will use it to read the arguments provided on the
# command line (CSV file path, and column name).
import sys

def enumerate_column(csv_data, column_name):
  """enumerate_column will iterate over each row, counting unique occurences.

  This will allow the caller to find all unique words, as well as the number
  of occurences of each word. To do this efficiently, a Python dictionary
  would be optimal. Each word will become a key in the dictionary, and the
  value will be the number of occurences.

  Args:
    csv_data - This is the list of dictionaries that was read into memory.
    column_name - This is the case sensitive column name

  Returns:
    A Python dictionary representing the unique words, and their occurence.

  Raises:
    KeyError - This will occur if the column name does not exist. Double check
               the column name!
  """
  # Start with an empty dictionary.
  unique_words = {}
  for row in csv_data:
    # Get the word that exists on this row, for the given column name.
    word = str(row[column_name])
    # This next line does the magic to increment the occurence.
    # The "get" function will try to get the value if it exists in the
    # dictionary. If it doesn't, it will return the default value, which in
    # this case is 0. So the first time the word appears, it will be set to
    # 0 + 1.
    unique_words[word] = unique_words.get(word, 0) + 1
  return unique_words

def extract_data(path_to_csv):
  """extract_data will read the contents of the CSV file into memory.

  Using the csv module that was imported at the beginning of this file, the
  DictReader method will read the contents and create a Python dictionary. The
  DictReader is preferred, because it allows us to reference a column
  specifically by name.

  Args:
    path_to_csv - this is the C:\... path to the CSV file

  Returns:
    A Python list of dictionaries, where the keys are the column names.
  """
  # Typically, one would try to catch exceptions, incase there is an IO error
  # or some other kind of problem. But because this entire script hinges on
  # the idea that we can open this file, I'd rather let the exception surface
  # to the command prompt.
  csvfile = open(path_to_csv)
  return csv.DictReader(csvfile)

def main():
  # Check if the number of arguments is correct.
  # argv is conventionally used in programming languages to represent the
  # variable list of arguments provided on the command line.
  # We would expect there to be 3 arguments, because the first argument is the
  # script name (i.e. word_count.py, C:\...\sample.csv, and ColumnName).
  if len(sys.argv) < 3:
    # There is an incorrect number of arguments, so print to the screen an
    # example on how to run the command.
    print('usage: C:\Python27\Python.exe '
          'C:\users\eriknix\Desktop\word_count.py <path to CSV> <Column Name>')
    # Use the sys module to exit now, with a status of 1 (1 means general
    # failure).
    sys.exit(1)

  # sys.argv[0] is the script name.
  csv_path = sys.argv[1]
  column_name = sys.argv[2]

  data = extract_data(csv_path)
  words = enumerate_column(data, column_name)

  for word, occurence in words.iteritems():
    print('%s:  %s' % (word, occurence))


# The following if condition will check if this module is running via the
# command line. Alternatively, this could be imported as a module in a separate
# script, and in that case, this condition would fail.
if __name__ == '__main__':
  main()
