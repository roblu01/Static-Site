from textnode import TextNode, TextType
from static_to_public import copy_static_to_public

def main():
    print(TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev'))
    copy_static_to_public()

if __name__ == "__main__":
    main()