#!/usr/bin/env python
"""
Gantt.py is a simple class to render Gantt charts, as commonly used in
"""

import json
# setup pyplot w/ tex support
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

from operator import sub

# class Package(object):
#     """Encapsulation of a work package

#     A work package **must** have a label, start and end.
#     Optionally it may contain milestones.
#     :arg str label: package name
#     :arg int start: start time (discreet)
#     :arg int end: end time (discreet)
#     """
#     def __init__(self, label, start, end):
#         self.label = label
#         self.start = start
#         self.end = end

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
        self._loadData()
        self._procData()

    def _loadData(self):
        """ Load data from dataFile or use sample data. We just import the plain
        python data structures. This is lazy but serves the purpose here.
        """

        # load data file
        with open(self.dataFile) as fh:
            data = json.load(fh)

        # must-haves
        self.title    = data['title']
        self.packages = data['packages']
        self.labels   = []
        for key in self.packages:
            self.labels.append(key)
        self.labels.sort()

        # optionals
        try:
            self.milestones = data['milestones']
        except:
            self.milestones = None
        try:
            self.xlabel = data['xlabel']
        except:
            self.xlabel = None
        try:
            self.xticks = data['xticks']
        except:
            self.xticks = None

    def _procData(self):
        """ Process data to have all values needed for plotting
        """
        # parameters for bars
        self.nPackages = len(self.labels)
        self.start = [None] * self.nPackages
        self.end = [None] * self.nPackages

        for key, vals in self.packages.iteritems():
            idx = self.labels.index(key)
            self.start[idx], self.end[idx] = map(int, vals.split(','))

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

        plt.scatter(x, y, s=50, marker="D" ,
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

        # render barchart
        self.barlist = plt.barh(self.yPos, self.durations,
                left= self.start,
                align='center',
                height=.3,
                alpha=.9,
                color='#32AEE0')

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
    for bar in [0,1] :
        g.barlist[bar].set_color('#F1C231')
    for bar in range(2,6):
        g.barlist[bar].set_color('#32E07A')
    g.show()
