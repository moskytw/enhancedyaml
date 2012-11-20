# Enhanced PyYAML

It makes PyYAML more convenient and avoids duplicate YAML data.

Here is the features:

* by deafult, use name of class as the `yaml_tag` of YAMLObject
* load anchor `&` as an attribute `anchor` of YAMLObject instance
* dump the attribute `anchor` of YAMLObject instance as the anchor `&` name

## Example

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

### Create an YAMLObject without specifiying `yaml_tag`

   import enhancedyaml

   class Example(enhancedyaml.YAMLObject): pass

### Loaded YAML

Code:

    from pprint import pprint

    data = enhancedyaml.load(open('data/enhanced_data.yaml'))
    pprint(data)

Output:

    {'examples': [<__main__.Example object at 0x7fa825fb4fd0>,

                  <__main__.Example object at 0x7fa825fb4cd0>],
     'order': [<__main__.Example object at 0x7fa825fb4fd0>,
               <__main__.Example object at 0x7fa825fb4cd0>]}

### Content of `data['order']`

Code:

    pprint(list(example.__dict__ for example in data['order']))

Output:

    [{'anchor': u'first', 'data': 'I am the first one.'},
     {'anchor': u'second', 'data': 'I am the second one.'}]

`Example` has addational attribute `anchor`.

### Dump Data Again

Code:

    print enhancedyaml.dump(data, default_flow_style=False)

Output:

    examples:
    - &first !Example
      data: I am the first one.
    - &second !Example
      data: I am the second one.
    order:
    - *first
    - *second

It is almost same as the original YAML.

You can find more examples in `enhancedyaml/examples` directory.

Have fun!
