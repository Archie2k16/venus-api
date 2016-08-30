# encoding:utf-8
# !/usr/bin/env python
# me@archie.cc

from tools.dotdict import dot_dict

a = dot_dict({})
b = dot_dict({'asa': 123})
a.sb = 'liwenlong'
print a
print b
