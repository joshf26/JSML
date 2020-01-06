# JSML Syntax
JSML uses JSON for its initial parsing, so all of those rules apply.
However, JSML only supports strings, so avoid using numbers or boolean types for data.

### Elements
An element is a JSON key/value pair collection that contains the following keys:
- `tag`: the HTML tag the element should have
- `attributes` (optional): a JSON key/value pair collection that represents the attributes an element has
- `children` (optional): a JSON ordered list of elements that are children of this one

For example, the following html code:
```html
<body>
  <img src="img.jpg" alt="Image">
</body>
```

Would be written as the following JSON file:
```json
{
  "tag": "body",
  "children": [
    {
      "tag": "img",
      "attributes": {
        "src": "img.jpg",
        "alt": "Image"
      }
    }
  ]
}
```

### Text
To insert text, simply add a string in place of where an element would be.

For example, the following html code:
```html
<p>Hello World</p>
```

Would be written as the following JSON file:
```json
{
  "tag": "p",
  "children": [
    "Hello World"
  ]
}
```

Note that this text is escaped, so you don't have to worry about characters like `<` or `>` getting in the way.
For example,
```json
{
  "tag": "p",
  "children": [
    "<b>Hello World</b>"
  ]
}
```

Transpiles to
```html
<p>&lt;b&gt;Hello World&lt;/b&gt;</p>
```

### More Examples
If you're still confused, check out the [examples](../examples) folder.
