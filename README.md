# JSML

XML and JSON are two common ways of storing data and are interchangeable in most circumstances.
HTML is ***one*** way of describing the presentation of data and is XML-like.
Why isn't there a JSON-like language that is used for describing the presentation of data?

JSML lets you create websites using JSON... for some reason. It is a Python script that converts a JSON file into an
HTML file.

### Example Usage
Create a JSON file that looks something like this (see [syntax.md](docs/syntax.md) for more details):
```json
{
  "tag": "p",
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

### Command Line Arguments
You can optionally add the following command line arguments:
- `-h` or `--help`: display a help message 
- `-o OUTPUT` or `--output OUTPUT`: specify the output html file name (default is "index.html")
- `-p`: print to stdout and skip writing to file

### Disclaimer
This project is just a proof of concept. I see no actual benefit to making websites this way over HTML. Please do not
actually use this!