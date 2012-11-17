#!/usr/bin/env python
# -*- coding: utf-8 -*-

import enhancedyaml

class Example(enhancedyaml.YAMLObject): pass

if __name__ == '__main__':
    from pprint import pprint
    data = enhancedyaml.load(open('data/enhanced_data.yaml'))
    print 'Loaded YAML:'
    pprint(data)
    print

    print 'Data of Examples:'
    for i, example in enumerate(data['order']):
        print 'Example %d:' % i
        print '    anchor:', example.anchor
        print '    data  :', example.data

