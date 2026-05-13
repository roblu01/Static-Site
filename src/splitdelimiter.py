from textnode import*
from enum import Enum
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        separated_list = old_node.text.split(delimiter)

        if len(separated_list)%2==0:
            raise Exception('delimiter is uneven')
        
        for i in range(0,len(separated_list)):
            if separated_list[i] == '':
                continue
            if i%2 != 0:
                new_nodes.append(TextNode(separated_list[i],text_type))
            else:
                new_nodes.append(TextNode(separated_list[i],TextType.TEXT))

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        extracted_image_tupple = extract_markdown_images(old_node.text)
        
        if extracted_image_tupple == []:
            new_nodes.append(old_node)
            continue

        raw_text = old_node.text
        
        for img_pair in extracted_image_tupple:
            alt_img = img_pair[0]
            link_img = img_pair[1]
            delimiter = f'![{alt_img}]({link_img})'

            separated_list = raw_text.split(delimiter,1)
            if separated_list[0] != '':
                new_nodes.append(TextNode(separated_list[0],TextType.TEXT))
            new_nodes.append(TextNode(alt_img,TextType.IMAGE,link_img))
            raw_text = separated_list[1]

        if raw_text != '':
            new_nodes.append(TextNode(raw_text,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        extracted_link_tupple = extract_markdown_links(old_node.text)

        if extracted_link_tupple == []:
            new_nodes.append(old_node)
            continue

        raw_text = old_node.text

        for link_pair in extracted_link_tupple:
            alt_link = link_pair[0]
            link_link = link_pair[1]
            delimiter = f'[{alt_link}]({link_link})'

            separated_list = raw_text.split(delimiter,1)
            if separated_list[0] != '':
                new_nodes.append(TextNode(separated_list[0],TextType.TEXT))
            new_nodes.append(TextNode(alt_link,TextType.LINK,link_link))
            raw_text = separated_list[1]

        if raw_text != '':
            new_nodes.append(TextNode(raw_text,TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    og_textnode = TextNode(text,TextType.TEXT)
    old_nodes = [og_textnode]
    splitted_bold = split_nodes_delimiter(old_nodes,'**',TextType.BOLD)
    splitted_italic = split_nodes_delimiter(splitted_bold,'_',TextType.ITALIC)
    splitted_code = split_nodes_delimiter(splitted_italic,"`",TextType.CODE)
    splitted_image = split_nodes_image(splitted_code)
    splitted_all = split_nodes_link(splitted_image)

    return splitted_all

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
    
    '''
    # I did not made an initial check if the block started correctly
    ok_quote = []
    for splitt in splitted:
        if not splitt.startswith(">"):
            return BlockType.PARAGRAPH
        if splitt.startswith(">") or splitt.startswith("> "):
            ok_quote.append('yes')
    if len(set(ok_quote)) <=1:
        return BlockType.QUOTE

    #ordered tweaked. it works but became convoluted when not using an initial check that would let me return early if something is amiss.
    ok_ordered = []
    for i in range(len(splitted)):
        splitt = splitted[i]
        if not splitt.startswith(f"{i+1}. "):
            return BlockType.PARAGRAPH
        if splitt.startswith(f"{i+1}. "):
            ok_ordered.append('yes')
    if len(set(ok_ordered)) <=1:
        return BlockType.ORDERED_LIST

    #ordered first try
    ok_ordered = []
    for i in range(len(splitted)):
        splitt = splitted[i]
        if splitt.startswith(f"{i+1}. "):
            if splitt[0] != f'{i+1}':
                return BlockType.PARAGRAPH
            ok_ordered.append('yes')
    if len(set(ok_ordered)) <=1:
        return BlockType.ORDERED_LIST
    '''
        

