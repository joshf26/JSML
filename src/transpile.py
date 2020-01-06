from xml.etree.ElementTree import Element, tostring


def transpile(data):
    root = None
    queue = [(data, None)]

    while queue:
        element_data, parent = queue.pop()

        if isinstance(element_data, dict):
            # Create the new element.
            element = Element(
                element_data['element'],  # TODO: Need to check for errors.
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
            parent.text = element_data

    return '<!DOCTYPE html>' + tostring(root, encoding='unicode', method='html')
