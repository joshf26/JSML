from inputparser import parse_input
from transpile import transpile


def main():
    data, output_file = parse_input()
    html = transpile(data)
    output_file.write(html)


if __name__ == '__main__':
    main()
