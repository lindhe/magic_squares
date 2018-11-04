#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

""" Hunting for the magic square! """

import argparse
import io
import sys
import time
from itertools import repeat
from typing import List

version = "0.1.2"


##############################     NotASquare     ##############################
class NotASquare(Exception):
  def __init__(self, message):
    super().__init__(message)

################################     Square     ################################
class Square:
  """ Defines an n by n square. """

  def __init__(self, *rows):
    """ Create a from n lists of length n """
    # Check that it is a square
    for row in rows:
      if len(row) != len(rows):
        raise NotASquare("A square must be n by n!")
    self.rows = [*rows]
    self.columns = [list(col) for col in list(zip(*rows))]
    self.n = len(rows)

  def __repr__(self):
    """ How to be unambiguous """
    return str(self.rows)

  def __str__(self):
    """ How to be pretty """
    res = ""
    for row in self.rows:
      res += (str(row) + "\n")
    # Skip the last \n when returning
    return res[:-1]

  def squared(self):
    """ Returns the rows squared """
    # Stolen from here: https://stackoverflow.com/a/27025330/893211
    return [list(map(pow, row, repeat(2))) for row in self.rows]


#############################     get_row_sums     #############################
def get_row_sums(square: Square) -> List[int]:
  """ Returns the sum of each row in a square. """
  sums = []
  for row in square.rows:
    sums.append(sum(row))
  return sums

#############################     get_col_sums     #############################
def get_col_sums(square: Square) -> List[int]:
  """ Returns the sum of each column in a square. """
  sums = []
  for col in square.columns:
    sums.append(sum(col))
  return sums

##########################     get_diagonal_sums     ##########################
def get_diagonal_sums(square: Square) -> List[int]:
  """ Returns a list of the sum of each diagonal. """
  topleft = 0
  bottomleft = 0
  # Seems like this could be more compact
  i = 0
  for row in square.rows:
    topleft += row[i]
    i += 1
  i = 0
  for col in square.columns:
    bottomleft += col[i]
    i += 1
  return [topleft, bottomleft]

###########################     CHECK MAGICNESS     ###########################
def is_magic(square: Square) -> bool:
  assert type(square) is Square
  all_sums = (
      get_row_sums(square) +
      get_col_sums(square) +
      get_diagonal_sums(square)
      )
  # Check if all elements are equal.
  if all_sums.count(all_sums[0]) == len(all_sums):
    return True
  else:
    return False

def file_to_square(input_file: io.TextIOWrapper) -> Square:
  if input_file:
    # Read all non-empty lines from the file
    _rows = [line.split() for line in input_file.readlines() if line.strip()]
    # Stolen from here: https://stackoverflow.com/a/642169/893211
    rows = [list(map(int, x)) for x in _rows]
  else:
    # Some default value...
    rows = [[1, 2], [3, 4]]
  return Square(*rows)

def main(input_file: io.TextIOWrapper, parker: bool=False):
  """ Reads a square from a file, and runs magic analysis on it... """
  square = file_to_square(input_file)
  print(square)
  if is_magic(square):
    print("Woho! It's a magic square!! 🧙✨")
    sys.exit(0)
  else:
    print("That's a boring square.")
    sys.exit(2)

############################     Bootstrapping     ############################
if __name__ == '__main__':
  p = argparse.ArgumentParser(description="Finding magic squares...")
  # Add cli arguments
  p.add_argument('infile', nargs='?', type=argparse.FileType('r'))
  p.add_argument('-P', '--parker', action='store_true',
      help="Do a Parker Square instead!")
  p.add_argument('-V', '--version', action='version', version=version)
  # Run:
  args = p.parse_args()
  try:
    main(input_file=args.infile, parker=args.parker)
  except KeyboardInterrupt:
    sys.exit("\nInterrupted by ^C\n")

