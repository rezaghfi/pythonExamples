"""
    annotation - typing
    pylint, mypy for forced code to use annotations
"""

import typing as tp

def show(names:tp.List[str]):
  for name in names:
    print(name)

show(['amir', 'hasan', 'hossein', 'reza'])