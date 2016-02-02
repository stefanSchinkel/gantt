#!/usr/bin/env python
"""
see: http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html to get
started
"""
# setup pyplot w/ tex support
import numpy as np
import matplotlib.pyplot as plt


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 20}


from matplotlib import rc, rcParams

rc('text', usetex=True)
rcParams.update({'font.size': 10})


from operator import sub

# load data
from sample import packages, start, end, mileStones, title, xlabel, xticks

def loadData():
    """
    """
    pass


def addMilestones(milestones, yPos):
    """Add milestones to GANTT chart.
    The milestones have to provided in dict with the packages they belong
    to as keys and a list the (discreet) due date for the milestones as values

    :arg dict milestones: dict with milestones
    :arg list yPos: positions on y scale
    """

    x = []
    y = []
    for key in milestones.iterkeys():
        for value in milestones[key]:
            y += [yPos[packages.index(key)]]
            x += [value]

    plt.scatter(x, y, s=40, marker="D" ,
                color="yellow", edgecolor="black", zorder=3)

""" main()
"""
def main():
    # process data
    nPackages = len(packages)
    durations = map(sub, end, start)
    # reverse y-ordering so pkg 1 is at top
    yPos = np.arange(nPackages, 0, -1)

    # init figure
    fig, ax = plt.subplots()
    ax.yaxis.grid(False)
    ax.xaxis.grid(True)

    # format x-a
    plt.tick_params(
        axis='both',    # format x and y
        which='both',   # major and minor ticks affected
        bottom='on',    # bottom edge ticks are on
        top='off',      # top, left and right edge ticks are off
        left='off',
        right='off')

    # plot barchart
    plt.barh(yPos, durations,
            left=start,
            align='center',
            height=.5,
            alpha=.9,
            color='#004579')

    # label x and y ticks
    plt.yticks(yPos, packages)
    plt.xticks(xticks, map(str,xticks))

    # milestones
    addMilestones(mileStones, yPos)

    # tighten axis but give a little room from bar height
    plt.xlim(0, max(end))
    plt.ylim(0.5, nPackages+.5)

    # add text
    plt.xlabel(xlabel)
    plt.title(title)

    plt.show()

    # plt.savefig('GANTT.png', bbox_inches='tight')

if __name__ == '__main__':
    main()