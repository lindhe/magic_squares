#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

""" Hunting for the magic square! """

import sys
import time
import argparse

version = "0.1.1"


class NotASquare(Exception):
  def __init__(self, message):
    super().__init__(message)

class Square:
  """ Defines an n by n square. """

  def __init__(self, *rows):
    """ Create a from n lists of length n """
    # Check that it is a square
    for row in rows:
      if len(row) != len(rows):
        raise NotASquare("A square must be n by n!")
    self.rows = [*rows]
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


def main():
  """ Main function description """
  return (0)

if __name__ == '__main__':
  # Bootstrapping
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

