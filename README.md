# JSML

XML and JSON are two very common ways of storing data and can be interchangeable in most circumstances.
HTML is ***one*** way of describing the presentation of data.
HTML is XML-like, so where isn't there a JSON-like language in which HTML can be interchanged with?

JSML lets you create websites using JSON... for some reason.

### Example Usage
Create a JSON file that looks something like this (see [syntax.md](docs/syntax.md) for more details):
```json
{
  "element": "p",
  "children": [
      "Hello World"
  ]
}
```

Now run the transpiler using `python3 src/main.py /path/to/file.json`.

You should now see a file called `index.html` in your working directory with the following contents:
```html
<!DOCTYPE html><p>Hello World</p>
```

For more examples, look in the [examples](examples) folder.

### Disclaimer
This project is just a proof of concept. I see no actual benefit to making websites this way over normal HTML. Please do
not actually use this!