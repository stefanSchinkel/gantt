#!/usr/bin/env python
"""
Wrapper function to use the Gantt class
"""
from gantt import Gantt

g = Gantt('data.py')
g.render()
g.show()