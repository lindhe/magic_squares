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

def main():
  """ Main function description """
  return (0)


############################     Bootstrapping     ############################
if __name__ == '__main__':
  p = argparse.ArgumentParser(description="Finding magic squares...")
  # Add cli arguments
  p.add_argument('-P', '--parker', action='store_true',
      help="Do a Parker Square instead!")
  p.add_argument('-V', '--version', action='version', version=version)
  # Run:
  args = p.parse_args()
  try:
    main()
  except KeyboardInterrupt:
    sys.exit("\nInterrupted by ^C\n")

