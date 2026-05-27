from textnode import TextNode, TextType
from static_to_public import copy_static_to_public
from generate_page import generate_pages_recursive
import sys

def main():
    basepath = sys.argv[1]
    if not basepath:
        basepath = '/'

    copy_static_to_public()
    generate_pages_recursive('content','template.html','docs',basepath)

if __name__ == "__main__":
    main()