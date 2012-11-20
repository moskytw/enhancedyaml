#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class Example(yaml.YAMLObject):
    yaml_tag = '!Example'

if __name__ == '__main__':
    from pprint import pprint

    data = yaml.load(open('data/original_data.yaml'))


    print '### Loaded YAML'
    print
    pprint(data)
    print

    print "### Content of `data['order']`"
    print
    pprint(list(example.__dict__ for example in data['order']))
    print

    print '### Dump Data Again'
    print
    print yaml.dump(data, default_flow_style=False)
