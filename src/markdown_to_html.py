from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from splitdelimiter import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        HTML_Node = block_to_htmlnode(block)
        children.append(HTML_Node)
    Parent_node = ParentNode("div",children)
    return Parent_node 
    
def block_to_htmlnode(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        return heading_to_HTMLNode(block)
    if block_type == BlockType.QUOTE:
        return quote_to_HTMLNode(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unorderedlist_to_HTMLNode(block)
    if block_type == BlockType.ORDERED_LIST:
        return orderedlist_to_HTMLNode(block)
    if block_type == BlockType.CODE:
        return code_to_HTMLNode(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_HTMLNode(block)

def text_to_children(text_string):
    children = []
    textnodes = text_to_textnodes(text_string)
    for tnod in textnodes:
        children.append(text_node_to_html_node(tnod))
    return children

def orderedlist_to_HTMLNode(block):
    count = 0
    splitted_block = block.split("\n")
    list_items =[]
    for split_block in splitted_block:
        count+=1
        cleaned = split_block[len(f"{count}")+2:]
        children = text_to_children(cleaned)
        list_items.append(ParentNode("li",children))
    return ParentNode("ol",list_items)

def unorderedlist_to_HTMLNode(block):
    splitted_block = block.split("\n")
    list_items =[]
    for split_block in splitted_block:
        cleaned = split_block[2:]
        children = text_to_children(cleaned)
        list_items.append(ParentNode("li",children))
    return ParentNode("ul",list_items)

def heading_to_HTMLNode(block):
    count=0
    for char in block:
        if char == "#":
            count+=1
        else:
            break
    cleaned = block[count+1:]
    children = text_to_children(cleaned)
    return ParentNode(f"h{count}",children)

def paragraph_to_HTMLNode(block):
    lines = block.split("\n")
    block_strip =[]
    for line in lines:
        block_strip.append(line.strip())
    cleaned = " ".join(block_strip)
    children = text_to_children(cleaned)
    return ParentNode("p",children)

def quote_to_HTMLNode(block):
    lines = block.split("\n")
    block_strip =[]
    for line in lines:
        block_strip.append(line.strip(">").strip())
    cleaned = " ".join(block_strip)
    children = text_to_children(cleaned)
    return ParentNode("blockquote",children)

def code_to_HTMLNode(block):
    block_tick_strip = block[4:-3]
    text_code = TextNode(block_tick_strip,TextType.CODE)
    leaf_code = text_node_to_html_node(text_code)
    return ParentNode("pre",[leaf_code])    