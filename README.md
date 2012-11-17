# Enhanced PyYAML

It enhances serval PyYAML classes:

* `Loader`: Addationally load the anchor (`&`) name as an attribute of object. 
* `YAMLObject`: Defaultly use class name as the yaml tag.

# Example

Here is the yaml file:

    # tests/enhanced_data.yaml

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

    # tests/test_enhanced.py
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
