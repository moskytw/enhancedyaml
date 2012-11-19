#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import *

_Loader = Loader
class Loader(_Loader):

    def __getattribute__(self, name):

        if name[:8] == 'compose_' and name[-5:] == '_node' and name != 'compose_node':

            def compose_x_node_with_anchor(anchor):
                node = getattr(super(Loader, self), name)(anchor)
                node.anchor = anchor
                return node

            return compose_x_node_with_anchor

        else:
            return object.__getattribute__(self, name)

    def construct_object(self, node, deep=False):
        data = super(Loader, self).construct_object(node, deep)
        if hasattr(node, 'anchor') and hasattr(data, '__dict__'):
            data.anchor = node.anchor
        return data

_YAMLObjectMetaclass = YAMLObjectMetaclass
class YAMLObjectMetaclass(_YAMLObjectMetaclass):

    def __init__(cls, name, bases, attrs):
        if hasattr(cls, 'yaml_tag'):
            yaml_tag = '!'+name
            # PyYAML uses it to emit
            cls.yaml_tag = yaml_tag
            # PyYAML uses it to add constructor and representer (@ orignal YAMLObjectMetaclass)
            attrs['yaml_tag'] = yaml_tag

        super(YAMLObjectMetaclass, cls).__init__(name, bases, attrs)

_YAMLObject = YAMLObject
class YAMLObject(_YAMLObject):
    __metaclass__ = YAMLObjectMetaclass

_load = load
def load(stream, Loader=Loader):
    return _load(stream, Loader)
