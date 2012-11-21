#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yaml import *

_Loader = Loader
class Loader(_Loader):

    def compose_node(self, parent, index):
        anchor = None
        if self.check_event(AliasEvent):
            anchor = self.peek_event().anchor

        node = super(Loader, self).compose_node(parent, index)

        if anchor is not None:
            node.anchor = anchor

        return node

    def construct_object(self, node, deep=False):
        data = super(Loader, self).construct_object(node, deep)
        if hasattr(node, 'anchor') and hasattr(data, '__dict__'):
            data.anchor = node.anchor
        return data

_Dumper = Dumper
class Dumper(_Dumper):

    ANCHOR_TEMPLATE = u'%s%03d'

    def __init__(self, *args, **kargs):
        super(Dumper, self).__init__(*args, **kargs)
        self.last_anchor_id_by_tag = {}

    def serialize(self, node):
        super(Dumper, self).serialize(node)
        self.last_anchor_id_by_tag = {}

    def generate_anchor(self, node):
        if hasattr(node, 'anchor'):
            # TODO: rename `anchor` to `_id`?
            return node.anchor
        elif hasattr(node, 'tag'):
            last_anchor_id = self.last_anchor_id_by_tag[node.tag] = self.last_anchor_id_by_tag.setdefault(node.tag, 0) + 1
            return self.ANCHOR_TEMPLATE % (node.tag[1:].lower(), last_anchor_id)
        else:
            self.last_anchor_id = self.last_anchor_id + 1
            return self.ANCHOR_TEMPLATE % ('id', last_anchor_id)

    def represent_yaml_object(self, tag, data, cls, flow_style=None):
        anchor = None
        if hasattr(data, 'anchor'):
            anchor = data.anchor
            del data.anchor

        node = super(Dumper, self).represent_yaml_object(tag, data, cls, flow_style)

        if anchor is not None:
            node.anchor = anchor

        return node

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

_dump = dump
def dump(data, stream=None, Dumper=Dumper, **kwds):
    return dump_all([data], stream, Dumper=Dumper, **kwds)
