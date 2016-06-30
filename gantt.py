#!/usr/bin/env python
"""
Gantt.py is a simple class to render Gantt charts, as commonly used in
"""

import json
# setup pyplot w/ tex support
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
# rc('text', usetex=True)

from operator import sub

DEFCOLOR = "#32AEE0"


class Package(object):
    """Encapsulation of a work package

    A work package is instantiate from a dictionary. It **has to have**
    a label, astart and an end. Optionally it may contain milestones
    and a color

    :arg str pkg: dictionary w/ package data name
    """
    def __init__(self, pkg):

        self.label = pkg['label']
        self.start = pkg['start']
        self.end = pkg['end']

        if self.start < 0 or self.end < 0:
            raise ValueError("Package cannot begin at t < 0")
        if self.start > self.end:
            raise ValueError("Cannot end before started")

        try:
            self.milestones = pkg['milestones']
        except KeyError:
            pass

        try:
            self.color = pkg['color']
        except KeyError:
            self.color = DEFCOLOR


class Gantt(object):
    """Gantt
    Class to render a simple Gantt chart, with optional milestones
    """
    def __init__(self, dataFile):
        """ Instantiation

        Create a new Gantt using the data in the file provided
        or the sample data that came along with the script

        :arg str dataFile: file holding Gantt data
        """
        self.dataFile = dataFile

        # some lists needed
        self.packages = []
        self.labels = []

        self._loadData()
        self._procData()

    def _loadData(self):
        """ Load data from dataFile or use sample data. We just import the plain
        python data structures. This is lazy but serves the purpose here.
        """

        # load data
        fh = open(self.dataFile)
        data = json.load(fh)
        fh.close()

        # must-haves
        self.title = data['title']
        for pkg in data['packages']:
            self.packages.append(Package(pkg))
            self.labels.append(pkg['label'])

        self.labels.sort()

        # optionals
        self.milestones = {}
        for pkg in self.packages:
            try:
                self.milestones[pkg.label] = pkg.milestones
            except AttributeError:
                pass

        try:
            self.xlabel = data['xlabel']
        except KeyError:
            self.xlabel = ""
        try:
            self.xticks = data['xticks']
        except KeyError:
            self.xticks = ""

    def _procData(self):
        """ Process data to have all values needed for plotting
        """
        # parameters for bars
        self.nPackages = len(self.labels)
        self.start = [None] * self.nPackages
        self.end = [None] * self.nPackages

        for pkg in self.packages:
            idx = self.labels.index(pkg.label)
            self.start[idx] = pkg.start
            self.end[idx] = pkg.end

        self.durations = map(sub, self.end, self.start)
        self.yPos = np.arange(self.nPackages, 0, -1)

    def addMilestones(self):
        """Add milestones to GANTT chart.
        The milestones have to provided in dict with the packages they belong
        to as keys and a list the (discreet) due date for the milestones as values
        """

        x = []
        y = []
        for key in self.milestones.iterkeys():
            for value in self.milestones[key]:
                y += [self.yPos[self.labels.index(key)]]
                x += [value]

        plt.scatter(x, y, s=50, marker="D",
                    color="yellow", edgecolor="black", zorder=3)

    def format(self):
        """ Format various aspect of the plot, such as labels,ticks, BBox
        :todo: Refactor to use a settings object
        """
        # format axis
        plt.tick_params(
            axis='both',    # format x and y
            which='both',   # major and minor ticks affected
            bottom='on',    # bottom edge ticks are on
            top='off',      # top, left and right edge ticks are off
            left='off',
            right='off')

        # tighten axis but give a little room from bar height
        plt.xlim(0, max(self.end))
        plt.ylim(0.5, self.nPackages+.5)

        # add title and package names
        plt.yticks(self.yPos, self.labels)
        plt.title(self.title)

        if self.xlabel:
            plt.xlabel(self.xlabel)

        if self.xticks:
            plt.xticks(self.xticks, map(str, self.xticks))

    def render(self):
        """ Prepare data for plotting
        """

        # init figure
        self.fig, self.ax = plt.subplots()
        self.ax.yaxis.grid(False)
        self.ax.xaxis.grid(True)

        #assemble colors
        colors = []
        for pkg in self.packages:
            colors.append(pkg.color)


        # render barchart
        self.barlist = plt.barh(self.yPos, self.durations,
                                left=self.start,
                                align='center',
                                height=.5,
                                alpha=.9,
                                color=colors)

        # optionals
        if self.milestones:
            self.addMilestones()

        # format plot
        self.format()

    @staticmethod
    def show():
        """ Show the plot
        """
        plt.show()

    @staticmethod
    def save(saveFile='img/GANTT.png'):
        """ Save the plot to a file. It defaults to `img/GANTT.png`.

        :arg str saveFile: file to save to
        """
        plt.savefig(saveFile, bbox_inches='tight')

if __name__ == '__main__':
    g = Gantt('sample.json')
    g.render()
    g.show()
