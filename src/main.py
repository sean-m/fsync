#!/usr/bin/env python
'''
Open cross platform DropBox alternative without the security implications.
Sean McArdle
'''

from uuid import uuid4
import os


class File(dict):
    '''Base file object for fsync'''
    def __init__(self, fileName=None):
        dict.__init__(self)
        self["name"] = fileName
        self["guid"] = uuid4()

