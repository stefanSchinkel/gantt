#!/usr/bin/env python
"""
Wrapper function to use the Gantt class
"""
from gantt import Gantt

g = Gantt("./sample.json")
g.render()
g.show()
# g.save('img/GANTT.png')
