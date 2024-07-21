#!/usr/bin/env python
# pylint: disable=R0902, R0903, C0103
"""
Gantt.py is a simple class to render Gantt charts, as commonly used in
"""

import os
import json
import platform
from datetime import datetime
from operator import sub

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# TeX support: on Linux assume TeX in /usr/bin, on OSX check for texlive
if (platform.system() == "Darwin") and "tex" in os.getenv("PATH"):
    LATEX = True
elif (platform.system() == "Linux") and os.path.isfile("/usr/bin/latex"):
    LATEX = True
else:
    LATEX = False

# setup pyplot w/ tex support
if LATEX:
    rc("text", usetex=True)


class Package:
    """Encapsulation of a work package

    A work package is instantiated from a dictionary. It **has to have**
    a label, a start, and an end. Optionally it may contain milestones
    and a color.

    :arg str pkg: dictionary w/ package data name
    """

    def __init__(self, pkg):

        DEFCOLOR = "#32AEE0"

        self.label = pkg["label"]
        self.start = self._parse_date(pkg["start"])
        self.end = self._parse_date(pkg["end"])

        if self.start > self.end:
            raise ValueError("Cannot end before started")

        try:
            self.milestones = [self._parse_date(m) for m in pkg["milestones"]]
        except KeyError:
            self.milestones = []

        try:
            self.color = pkg["color"]
        except KeyError:
            self.color = DEFCOLOR

        try:
            self.legend = pkg["legend"]
        except KeyError:
            self.legend = None

    @staticmethod
    def _parse_date(date_str):
        """Parse date string to datetime object"""
        try:
            return datetime.strptime(date_str, "%m-%Y")
        except ValueError:
            raise ValueError(f"Date format for {date_str} should be MM-YYYY")


class Gantt:
    """Gantt
    Class to render a simple Gantt chart, with optional milestones
    """

    def __init__(self, dataFile):
        """Instantiation

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
        """Load data from a JSON file that has to have the keys:
        packages & title. Packages is an array of objects with
        a label, start and end property and optional milestones
        and color specs.
        """

        # load data
        with open(self.dataFile) as fh:
            data = json.load(fh)

        # must-haves
        self.title = data["title"]

        for pkg in data["packages"]:
            self.packages.append(Package(pkg))

        self.labels = [pkg["label"] for pkg in data["packages"]]

        # optionals
        self.milestones = {}
        for pkg in self.packages:
            try:
                self.milestones[pkg.label] = pkg.milestones
            except AttributeError:
                pass

        try:
            self.xlabel = data["xlabel"]
        except KeyError:
            self.xlabel = ""
        try:
            self.xticks = data["xticks"]
        except KeyError:
            self.xticks = []

    def _procData(self):
        """Process data to have all values needed for plotting"""
        # parameters for bars
        self.nPackages = len(self.labels)
        self.start = [None] * self.nPackages
        self.end = [None] * self.nPackages

        for pkg in self.packages:
            idx = self.labels.index(pkg.label)
            self.start[idx] = pkg.start
            self.end[idx] = pkg.end

        self.durations = [(e - s).days for s, e in zip(self.start, self.end)]
        self.start = [s.toordinal() for s in self.start]
        self.end = [e.toordinal() for e in self.end]

        self.yPos = np.arange(self.nPackages, 0, -1)

    def format(self):
        """Format various aspects of the plot, such as labels, ticks, BBox
        :todo: Refactor to use a settings object
        """
        # format axis
        plt.tick_params(
            axis="both",  # format x and y
            which="both",  # major and minor ticks affected
            bottom="on",  # bottom edge ticks are on
            top="off",  # top, left and right edge ticks are off
            left="off",
            right="off",
        )

        # tighten axis but give a little room from bar height
        plt.xlim(min(self.start), max(self.end))
        plt.ylim(0.5, self.nPackages + 0.5)

        # add title and package names
        plt.yticks(self.yPos, self.labels)
        plt.title(self.title)

        if self.xlabel:
            plt.xlabel(self.xlabel)

        if self.xticks:
            plt.xticks([datetime.strptime(tick, "%m-%Y").toordinal() for tick in self.xticks], self.xticks)

    def add_milestones(self):
        """Add milestones to GANTT chart.
        The milestones are simple yellow diamonds
        """

        if not self.milestones:
            return

        x = []
        y = []
        for key in self.milestones.keys():
            for value in self.milestones[key]:
                y += [self.yPos[self.labels.index(key)]]
                x += [value.toordinal()]

        plt.scatter(
            x, y, s=120, marker="D", color="yellow", edgecolor="black", zorder=3
        )

    def add_legend(self):
        """Add a legend to the plot if there are legend entries in
        the package definitions
        """

        cnt = 0
        for pkg in self.packages:
            if pkg.legend:
                cnt += 1
                idx = self.labels.index(pkg.label)
                self.barlist[idx].set_label(pkg.legend)

        if cnt > 0:
            self.legend = self.ax.legend(shadow=False, ncol=3, fontsize="medium")

    def render(self):
        """Prepare data for plotting"""

        # init figure
        self.fig, self.ax = plt.subplots()
        self.ax.yaxis.grid(False)
        self.ax.xaxis.grid(True)

        # assemble colors
        colors = [pkg.color for pkg in self.packages]

        self.barlist = plt.barh(
            self.yPos,
            self.durations,
            left=self.start,
            align="center",
            height=0.5,
            alpha=1,
            color=colors,
        )

        # format plot
        self.format()
        self.add_milestones()
        self.add_legend()

    @staticmethod
    def show():
        """Show the plot"""
        plt.show()

    @staticmethod
    def save(saveFile="img/GANTT.png"):
        """Save the plot to a file. It defaults to `img/GANTT.png`.

        :arg str saveFile: file to save to
        """
        plt.savefig(saveFile, bbox_inches="tight")


if __name__ == "__main__":
    g = Gantt("sample.json")
    g.render()
    g.show()
    # g.save('img/GANTT.png')
