# Enhanced PyYAML

It enhances several PyYAML classes:

* `Loader`: Extra load the anchor (`&`) name as an attribute of object. 
* `YAMLObject`: Use class name as the yaml tag if `yaml_tag` is not set.

# Example

Here is the yaml file:

    # examples/enhanced_data.yaml

    %YAML 1.1
    ---
    examples:
        - !Example &first
            data: I am the first one.
        - !Example &second
            data: I am the second one.
    order:
        - *first
        - *second

Load it with enhanced PyYAML:

    # examples/test_enhanced.py
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

Have fun!
