#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: MIT
# Author: Andreas Lindhé

""" Hunting for a real magic square! """

import sys
import time
import argparse

version = "0.0.1"


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

