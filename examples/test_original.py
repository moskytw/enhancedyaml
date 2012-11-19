#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

class Example(yaml.YAMLObject):
    yaml_tag = '!Example'

if __name__ == '__main__':
    from pprint import pprint

    data = yaml.load(open('data/original_data.yaml'))

    print 'Loaded YAML:'
    pprint(data)
    print

    print 'Data of Examples:'
    for i, example in enumerate(data['order']):
        print 'Example %d:' % i
        print '    anchor:', example.anchor
        print '    data  :', example.data

    print Example.yaml_tag
    print yaml.dump(data)

