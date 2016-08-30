#!/usr/bin/env python
# encoding:utf-8
# me@archie.cc

class meta_dot_dict(type):
    def __new__(cls, name, bases, attrs):
        def setattr_(self, key, value):
            if key.startswith('_'):
                super(dot_dict, self).__setattr__(key, value)
            else:
                self._map[key] = value

        def getattr_(self, key):
            return self._map[key]

        def repr_(self):
            return repr(self._map)

        def str_(self):
            return self.__repr__()

        attrs.update({'__setattr__': setattr_,
                      '__getattr__': getattr_,
                      '__repr__': repr_,
                      '__str__': str_})

        return type.__new__(cls, name, bases, attrs)


class dot_dict(object):
    __metaclass__ = meta_dot_dict

    def __init__(self, map):
        self._map = map

    def dump(self, fmt='conf'):
        for key, val in self._map.iteritems():
            print '{} = {}'.format(key, val)


class many2one(dot_dict):
    def __init__(self, arg, file_ext=None):
        rv = {}
        for key, val in arg.iteritems():
            if isinstance(key, tuple):
                for item in key:
                    if item in rv:
                        raise ValueError(
                            'Duplicate assign! key:"{}" vals:"{}"&"{}"'.format(item, rv[item], val))
                    rv.update({item: val})
            else:
                if key in rv:
                    raise ValueError(
                        'Duplicate assign! key:"{}" vals:"{}"&"{}"'.format(key, rv[key], val))
                rv.update({key: val})
        super(many2one, self).__init__(rv)


m21 = many2one


#
#
# def one2many(arg):
#     pass
#
#
