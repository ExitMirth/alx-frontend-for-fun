#!/usr/bin/env python3
''' Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
'''


import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    
    # Check if the Markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Perform the Markdown to HTML conversion logic
    # Here, let's assume a simple conversion using an external tool like pandoc
    conversion_command = f"pandoc {markdown_file} -o {output_file}"
    os.system(conversion_command)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Extract arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Perform the conversion
    convert_markdown_to_html(markdown_file, output_file)

    # Exit with success status
    sys.exit(0)
