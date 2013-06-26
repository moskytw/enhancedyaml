Enhanced PyYAML
===============

It makes PyYAML more convenient and avoids duplicate YAML data.

Here are the features:

- By deafult, it uses name of class as the `yaml_tag` of YAMLObject.
- It loads anchor `&` as an attribute `anchor` of YAMLObject instance.
- It dumps the attribute `anchor` of YAMLObject instance as the anchor `&` name.

Installation
------------

You can install it via PyPI,

::

    sudo pip install enhancedyaml

or download it manually.

Examples
--------

Here is `a yaml file
<https://github.com/moskytw/enhancedyaml/blob/dev/examples/data/enhanced_data.yaml>`_:

::

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

Create an YAMLObject Without Specifiying `yaml_tag`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    import enhancedyaml

    class Example(enhancedyaml.YAMLObject): pass

Loaded YAML
~~~~~~~~~~~

Code:

::

    from pprint import pprint

    data = enhancedyaml.load(open('data/enhanced_data.yaml'))
    pprint(data)

Output:

::

    {'examples': [<__main__.Example object at 0x7fa825fb4fd0>,

                  <__main__.Example object at 0x7fa825fb4cd0>],
     'order': [<__main__.Example object at 0x7fa825fb4fd0>,
               <__main__.Example object at 0x7fa825fb4cd0>]}

Content of `data['order']`
~~~~~~~~~~~~~~~~~~~~~~~~~~

Code:

::

    pprint(list(example.__dict__ for example in data['order']))

Output:

::

    [{'anchor': u'first', 'data': 'I am the first one.'},
     {'anchor': u'second', 'data': 'I am the second one.'}]

`Example` has addational attribute `anchor`.

Dump Data Again
~~~~~~~~~~~~~~~

Code:

::

    print enhancedyaml.dump(data, default_flow_style=False)

Output:

::

    examples:
    - &first !Example
      data: I am the first one.
    - &second !Example
      data: I am the second one.
    order:
    - *first
    - *second

It is almost same as the original YAML.

Dump Objects Which are Generated in Runtime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Code:

::

    e1 = Example()
    e2 = Example()
    e1.data = "I don't have `anchor`."
    e2.data = "I don't have `anchor`, too."
    es = [e1, e2, e2, e1]
    print enhancedyaml.dump(es, default_flow_style=False)

Output:

::

    - &example002 !Example
      data: I don't have `anchor`.
    - &example001 !Example
      data: I don't have `anchor`, too.
    - *example001
    - *example002

You can find more examples `here
<https://github.com/moskytw/enhancedyaml/tree/dev/examples>`_.

Have fun!
