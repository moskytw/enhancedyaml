# Enhanced PyYAML

It enhances several PyYAML classes:

* `YAMLObject`: Use class name as the yaml tag if `yaml_tag` is not set.
* `Loader`: Extra load the anchor (`&`) name as an attribute of object. 
* `Dumper`: Unpack the anchor attribute from object and use it as the anchor in dumped YAML.

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

Use Enhanced PyYAML to load (output of `examples/test_enhanced.py`):
   
    ## Loaded YAML:

    {'examples': [<__main__.Example object at 0x7f96b946de50>,
                  <__main__.Example object at 0x7f96b946dc10>],
     'order': [<__main__.Example object at 0x7f96b946de50>,
               <__main__.Example object at 0x7f96b946dc10>]}

    ## Attributs of Examples:

    * Example 0
        * anchor: first
        * data  : I am the first one.
    * Example 1
        * anchor: second
        * data  : I am the second one.

    ## Dump data again:

    examples:
    - &first !Example
      data: I am the first one.
    - &second !Example
      data: I am the second one.
    order:
    - *first
    - *second

Have fun!
