#!/usr/bin/env python
"""
Wrapper function to use the Gantt class
"""
from gantt import Gantt

g = Gantt('./tests/basics.json')
g.render()
g.show()