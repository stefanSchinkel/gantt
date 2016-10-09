#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
00_basics.py - basic tests for gantt
"""
import unittest
import sys
from os import path

# this has to be done first, otherwise Gantt sets the agg
import matplotlib
matplotlib.use('agg')

# add to path for sure
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from gantt import Gantt
from gantt import Package as WP


# file we use
BASICS = './basics.json'


class ExtendedTestCase(unittest.TestCase):

    def assertRaisesMsg(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except Exception as inst:
            self.assertEqual(inst.message, msg)


class TestsPackage(ExtendedTestCase):
    """Basic tests for package class
    """

    def testValuePassing(self):
        """ reject pointless dates
        """
        PKG = {"label": "A", "start": 0, "end": 2, "milestones": [1]}
        pkg = WP(PKG)
        self.assertEqual(pkg.label, "A")
        self.assertEqual(pkg.start, 0)
        self.assertEqual(pkg.end, 2)
        self.assertEqual(pkg.milestones, [1])

    def testValError(self):
        """ reject pointless dates
        """
        # start must be after begin
        PKG = {"label": "A", "start": 3, "end": 2}
        self.assertRaises(ValueError, WP, PKG)

    def testNegatives(self):
        """ reject negative start/end
        """
        # start must be after begin
        PKG = {"label": "A", "start": -1, "end": 2}
        self.assertRaisesMsg("Package cannot begin at t < 0", WP, PKG)
        PKG = {"label": "A", "start": -1, "end": -1}
        self.assertRaisesMsg("Package cannot begin at t < 0", WP, PKG)
        PKG = {"label": "A", "start": 3, "end": -1}
        self.assertRaisesMsg("Package cannot begin at t < 0", WP, PKG)

    def testDefColor(self):
        """ reject pointless dates
        """
        PKG = {"label": "A", "start": 0, "end": 2}
        pkg = WP(PKG)
        self.assertEqual(pkg.color, "#32AEE0")


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
        self.assertEqual(len(g.packages), 4)

    def testTimings(self):
        """ Make sure start/end is set properly
        """
        g = Gantt(BASICS)
        self.assertEqual(g.start, [0, 3, 3, 6])
        self.assertEqual(g.end, [2, 6, 5, 8])

    def testPlotTitle(self):
        """ Make sure title is passed to plot
        """
        g = Gantt(BASICS)
        g.render()
        x = g.ax.get_title()
        self.assertEqual(x, "Basic Title")


if __name__ == '__main__':
    unittest.main()
