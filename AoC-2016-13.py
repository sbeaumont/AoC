#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 13."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

x = y = 1

loc = x*x + 3*x + 2*x*y + y + y*y
designerNumber = 1352

print(loc, bin(loc))