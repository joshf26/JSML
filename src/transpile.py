from xml.etree.ElementTree import Element, tostring, ElementTree

DOCTYPE_HEADER = '<!DOCTYPE html>'


class JSMLError(Exception):
    pass


def get_path(root, element):
    parent_map = {child: parent for parent in ElementTree(root).iter() for child in parent}

    path = [root]
    current_element = element
    while current_element is not root:
        path.insert(1, current_element)
        current_element = parent_map[current_element]

    return path


def transpile(data):
    root = None
    queue = [(data, None)]

    while queue:
        element_data, parent = queue.pop()

        if isinstance(element_data, dict):
            # Every element must have a "tag" key.
            if 'tag' not in element_data:
                if parent is None:
                    raise JSMLError('Top level element is missing "tag" key.')
                else:
                    raise JSMLError('Element with path "{} -> ?" is missing "tag" key.'.format(
                        ' -> '.join(element.tag for element in get_path(root, parent))
                    ))

            # Create the new element.
            element = Element(
                element_data['tag'],
                element_data['attributes'] if 'attributes' in element_data else {},
            )

            # Append the element to its parent.
            if parent is None:
                root = element
            else:
                parent.append(element)

            # Process the element's children.
            if 'children' in element_data:
                for child in element_data['children'][::-1]:
                    queue.append((child, element))
        else:
            if parent is None:
                # Edge case where entire document is only a string value.
                return DOCTYPE_HEADER + element_data
            else:
                parent.text = element_data

    return DOCTYPE_HEADER + tostring(root, encoding='unicode', method='html')
