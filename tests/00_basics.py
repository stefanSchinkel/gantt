#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
00_basics.py - basic tests for gantt
"""
import unittest
import sys, os

# add to path for sure
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from gantt import Gantt
from gantt import Package as WP
# file we use
BASICS = './basics.json'

class TestsPackage(unittest.TestCase):
    """Basic tests for package class
    """

    def testArg(self):
        """ Parameter handling
        """
        # start must be after begin
        self.assertRaises(ValueError, WP, "Foo", 3, 2)



class TestsBasics(unittest.TestCase):
    """ Tests to ensure the data ends up in the right places
    """
    def testTitle(self):
        """ Whats my name?
        """
        g = Gantt(BASICS)
        self.assertEqual(g.title, "Basic Title")

    def testPackages(self):
        """ Make sure the no. of packages is correct
        """
        g = Gantt(BASICS)
        nPackages = 4
        self.assertEqual(len(g.packages), 4)

    def testTimings(self):
        """ Make sure start/end is set properly
        """
        g = Gantt(BASICS)
        self.assertEqual(g.start, [0, 3, 3, 6])
        self.assertEqual(g.end, [2, 6, 5, 8])


if __name__ == '__main__':
    unittest.main()