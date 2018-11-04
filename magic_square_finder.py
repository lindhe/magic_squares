#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

""" Hunting for the magic square! """

import sys
import time
import argparse

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


#############################     get_row_sums     #############################
def get_row_sums(square):
  """ Returns the sum of each row in a square. """
  sums = []
  for row in square.rows:
    sums.append(sum(row))
  return sums

#############################     get_col_sums     #############################
def get_col_sums(square):
  """ Returns the sum of each column in a square. """
  sums = []
  for col in square.columns:
    sums.append(sum(col))
  return sums

##########################     get_diagonal_sums     ##########################
def get_diagonal_sums(square):
  """ Returns a tuple of the sum of each diagonal. """
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
  return (topleft, bottomleft)

def main(input_file, parker=False):
  """ Main function description """
  # Read all non-empty lines from the file
  if input_file:
    rows = [line.split() for line in input_file.readlines() if line.strip()]
  else:
    rows = [[1, 2], [3, 4]]
  square = Square(*rows)
  print(square)

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

