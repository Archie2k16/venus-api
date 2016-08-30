# encoding:utf-8
# !/usr/bin/env python
# me@archie.cc

class dot_dict(object):
    def __init__(self, map):
        self._map = map

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super(dot_dict, self).__setattr__(key, value)
        else:
            self._map[key] = value

    def __getattr__(self, key):
        return self._map[key]

    def __repr__(self):
        return repr(self._map)

    def __str__(self):
        return self.__repr__()
