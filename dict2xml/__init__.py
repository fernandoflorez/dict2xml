from xml.etree.cElementTree import Element, SubElement
from xml.sax.saxutils import escape


def _dict2xml(src, parent_element=None):
    _res = []
    if isinstance(src, dict):
        for name, value in src.iteritems():
            if isinstance(value, dict):
                if parent_element is None:
                    _ = Element(name)
                else:
                    _ = SubElement(parent_element, name)
                _dict2xml(value, _)
                _res.append(_)
            elif isinstance(value, list):
                for item in value:
                    if parent_element is None:
                        _ = Element(name)
                    else:
                        _ = SubElement(parent_element, name)
                    _dict2xml(item, _)
                    _res.append(_)
            else:
                if name == '_text':
                    parent_element.text = escape(
                        str(value),
                        {
                            '"': '&quot;',
                            "'": '&apos;'
                        }
                    )
                else:
                    parent_element.attrib.update({name: str(value)})
    elif isinstance(src, list):
        for item in src:
            for sub_item in dict2xml(item, parent_element):
                _res.append(sub_item)

    return _res


def dict2xml(src):
    if not isinstance(src, dict):
        return None

    _ = _dict2xml(src)
    if len(_) == 0:
        _ = None
    elif len(_) == 1:
        _ = _[0]

    return _
