[![Build Status](https://travis-ci.org/stefanSchinkel/gantt.svg?branch=master)](https://travis-ci.org/stefanSchinkel/gantt)
###README

Gantt is a python class to produce, well, Gantt charts. The charts are kept (very) simple, using a discreet time scale, unicolor bars and optional milesstones.

###Background
Gantt charts are commonly used in project management. I wanted to  make one myself and LibreProject was way too involved for the project in question. Hence I used OpenOffice Calc and made a plain horizontal bar chart. That took little time but was ok. Then I needed to add milestones (basically just a marker) to the chart. I completely failed doing this in OpenOffice (and still don't know how to do that ...).

Long story short: I don't know how to [excel](https://xkcd.com/559/).

### Basic usage

```python

from gantt import Gantt
g = Gantt('./sample.json')
g.render()
g.show()                # or save w/ g.save('foo.png')

```

Or simply call `runner.py`

### Data structure :construction:

All data is provided as a JSON structure that **has to contain**:

 - a key **packages** containing an array of package definitions with **label**, **end** and **start**. Start and end values are discreet.
 - a **title** string (may contain TeX, escaped)

```json

{
  "packages": [
  { "label" : "WP 1-1",
    "start": 0,
    "end": 2,
    "milestones" : [2],
    "legend": "worker one"
  },
  { "label" : "WP 1-2",
    "start": 2,
    "end": 4,
    "milestones" : [3, 4]
  }
  ],

"title" : " Sample GANTT for \\textbf{myProject}",
"xlabel" : "time (weeks)",
"xticks" : [2,4,6,8,10,12]
}

```
The milestones, colors and legend entry are optional as are the label for the x-axis and the definition of the tickmarks.
The title may contain TeX, but make sure your system supports it. For

See [sample.json](./sample.json) for the data used to produce the image below.
### Requirements

 - numpy
 - matplotlib

### ToDo
 - nicer data structure (JSON) :white_check_mark:
 - dedicated class for packages :white_check_mark:
 - dynamic TeX support :white_check_mark:
 - add parameter object/dict for more control over colors etc :construction:

###Screenshot
![Sample Gantt with milestone](img/GANTT.png)

See [sample.json](./sample.json) for definition.