###README

gantt.py is a python class to produce, well, Gantt charts. The charts are kept (very) simple, using a discreet time scale, unicolor bars and optional milesstones. Adapt the data structure according to your needs.

###Background
Gantt charts are commonly is in project management. I had to make one myself and LibreProject was way too involved for that. Hence I used OOCalc and a plain horizontal bar chart. That took some time but was ok. One day I was requested to add milestones (basically just a marker) to the chart. I completely failed doing this in OOCalc (and still don't know if its possible at all).

Long story short: I don't know how to [excel](https://xkcd.com/559/).

### Data structure

All data is provided in plain python.
```python
# a set called package holding the name of workpackages
# it has to set is need to maintain the ordering (see todos)
packages = ("A", "B", "C")

# dictionary called timing with package name as key and start/end as values
timing = {
    "A" : "0,3",
    "B" : "2,4",
    "C" : "3,5"
}

# a title string (may contain TeX)
title = r" Sample GANTT for \textbf{myProject}"

#OPTIONAL
# a dictionary mapping milestones to packages
mileStones = { "A" : 2, "B" 4}
# label for x axis
xlabel = "time (weeks)"
# manual ticks on x axis
xticks = [2,4,6,8,10,12]

```

See sample.py for the data used to produce the image below.
### Requirements

 - numpy
 - matplotlib

### ToDo
 - nicer data structure
 - add parameter object/dict for more control over colors etc

###Screenshot
![Sample Gantt with milestone](img/GANTT.png)