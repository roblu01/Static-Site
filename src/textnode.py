from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "text"
    ITALIC_TEXT = "_Italic text_"
    CODE_TEXT = "'Code text'"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"

class TextNode:
    def __init__(self,text,text_type,url):
        self.text = text
        self.text_type = text_type
        if url is None:
            self.url = None
        else:
            self.url = url

    def __eq__(self, other):
        if isinstance(other,TextNode):
            return True
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"