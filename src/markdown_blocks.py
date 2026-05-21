from enum import Enum

def markdown_to_blocks(markdown):
    separated = markdown.split('\n\n')
    clean_list = []
    for piece in separated:
        cleaned = piece.strip()
        if cleaned !='':
            clean_list.append(cleaned)
    return clean_list

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    splitted = block.split("\n")

    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for splitt in splitted:
            if not splitt.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for splitt in splitted:
            if not splitt.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith("1. "):
        for i in range(len(splitted)):
            splitt = splitted[i]
            if not splitt.startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH