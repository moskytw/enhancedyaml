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

    print '### Dump Objects Which Are Generated in Runtime'
    print
    e1 = Example()
    e2 = Example()
    e1.data = "I don't have `anchor`."
    e2.data = "I don't have `anchor`, too."
    es = [e1, e2, e2, e1]
    print yaml.dump(es, default_flow_style=False)
