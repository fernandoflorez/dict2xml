dict2xml
========

Small utility to convert a python dict into an xml tree.

Supports node attributes and text nodes.

Uses cElementTree internally so no deps under python 2.5+


Installation
============

.. code-block:: bash

    pip install pydict2xml


Examples
========

.. code-block:: python

    from dict2xml import dict2xml
    from xml.etree.cElementTree import tostring


    tree = {
        'root': {
            'foo': 'bar',
            'children': [
                {
                    'name': 'child 1'
                },
                {
                    'name': 'child 2'
                }
            ],
            'text_node': {
                '_text': 'This is a test'
            }
        }
    }

    data = dict2xml(tree)

    print data

    print tostring(data, encoding='UTF-8')
