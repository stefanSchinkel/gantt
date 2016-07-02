[![Build Status](https://travis-ci.org/stefanSchinkel/gantt.svg?branch=master)](https://travis-ci.org/stefanSchinkel/gantt)
###README

Gantt is a python class to produce, well, Gantt charts.
The charts are kept (very) simple, using a discreet time scale,
unicolor bars and optional milesstones.

###Background
Gantt charts are commonly used in project management. I wanted to  make one myself and LibreProject was way too involved for the project in question.
Hence I used OpenOffice Calc and made a plain horizontal bar chart.
That took little time but was ok. Then I needed to add milestones (basically just a marker) to the chart. I completely failed doing this in OpenOffice (and still don't know how to do that ...).

Long story short: I don't know how to [excel](https://xkcd.com/559/).

### Basic usage

```python
from gantt import Gantt # import
g = Gantt("data.json")  # init
g.render()              # render
g.show()                # or save w/ g.save('foo.png')
```

### Data structure :construction:

All data is provided as a JSON structure that **has to contain**:

 - a key **packages** containing an array of package definitions with **label**, **end** and **start**. Start and end value are discreet.
 - a **title** string (may contain TeX, escaped)

```json

{
"packages" : [
    { "label" : "WP 1",
      "start": 0,
      "end": 3
    },
    { "label" : "WP 2",
      "start": 4,
      "end": 6,
      "milestones" : [5],
      "color" : "#FFCC00"
    }
  ],

"title" : "Sample GANTT for \\textbf{myProject}"
}
```
The milestones and colors are optional and the title may contain TeX.
Optionally the JSON may also contain:

 - a label for the x-axis
 - a definition of where set tickmarks

```json

{
"xlabel" : "time (weeks)",
"xticks" :  [2,4,6,8,10,12]
}
```

See [sample.json](./sample.json) for the data used to produce the image below.
### Requirements

 - numpy
 - matplotlib

### ToDo
 - nicer data structure (JSON) :white_check_mark:
 - dedicated class for packages :white_check_mark:
 - dynamic TeX support :white_check_mark:
 - add parameter object/dict for more control over colors etc

###Screenshot
![Sample Gantt with milestone](img/GANTT.png)

See [sample.json](./sample.json) for definition.