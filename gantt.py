#!/usr/bin/env python
"""
Gantt.py is a simple class to render Gantt charts, as commonly used in
"""
# setup pyplot w/ tex support
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)

from operator import sub

class Gantt(object):
    """Gantt
    Class to redner a simple Gantt chart, with optional milestones
    """
    def __init__(self, dataFile='sample.py'):
        """ Instantiation

        Create a new Gantt using the data in the file provided or the sample
        data that came along with the script

        :arg str dataFile: file holding Gantt data
        """
        self.dataFile = dataFile
        self._loadData()
        self._procData()

    def _loadData(self):
        """ Load data from dataFile or use sample data. We just import the plain
        python data structures. This is lazy but serves the purpose here.
        """
        import imp
        from os import path
        with open(self.dataFile) as fp:
            data = imp.load_source('data', path.dirname(self.dataFile), fp)

        # # must-haves
        self.packages   = data.packages
        self.timing     = data.timing
        self.title      = data.title

        # optionals
        try:
            self.milestones = data.milestones
        except:
            self.milestones = None
        try:
            self.xlabel = data.xlabel
        except:
            self.xlabel = None
        try:
            self.xticks = data.xticks
        except:
            self.xticks = None

    def _procData(self):
        """ Process data to have all values needed for plotting
        """
        # parameters for bars
        self.nPackages = len(self.packages)
        self.start = [None] * self.nPackages
        self.end = [None] * self.nPackages

        for key, vals in self.timing.iteritems():
            idx = self.packages.index(key)
            self.start[idx], self.end[idx]  = map(int, vals.split(','))

        self.durations = map(sub, self.end, self.start)
        self.yPos = np.arange(self.nPackages, 0, -1)

    def _addMilestones(self, milestones):
        """Add milestones to GANTT chart.
        The milestones have to provided in dict with the packages they belong
        to as keys and a list the (discreet) due date for the milestones as values

        :arg dict milestones: dict with milestones
        """
        x = []
        y = []
        for key in milestones.iterkeys():
            for value in milestones[key]:
                y += [self.yPos[self.packages.index(key)]]
                x += [value]

        plt.scatter(x, y, s=40, marker="D" ,
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
        plt.yticks(self.yPos, self.packages)
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
        plt.barh(self.yPos, self.durations,
                left= self.start,
                align='center',
                height=.5,
                alpha=.9,
                color='#004579')

        # optionals
        if self.milestones:
            self._addMilestones(self.milestones)

        # format plot
        self.format()

    def show(self):
        """ Show the plot
        """
        plt.show()

    def save(self, saveFile='img/GANTT.png'):
        """ Save the plot to a file. It defaults to `img/GANTT.png`.

        :arg str saveFile: file to save to
        """
        plt.savefig(saveFile, bbox_inches='tight')

if __name__ == '__main__':
    g = Gantt()
    g.render()
    g.show()
