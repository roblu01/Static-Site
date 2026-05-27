import os
from markdown_to_html import markdown_to_html_node
from markdown_blocks import BlockType, markdown_to_blocks
from htmlnode import ParentNode
from pathlib import Path

def generate_page(from_path,template_path,dest_path,basepath):
    print(f"Generating page from {from_path} to {dest_path}\n using {template_path}\n")

    with open(from_path,'r') as f:
        content_from_path = f.read()
    
    with open(template_path,'r') as f:
        content_template_path = f.read()

    html_node = markdown_to_html_node(content_from_path)
    html_content = html_node.to_html()
    title = extract_title(content_from_path)
    replace_title = content_template_path.replace('{{ Title }}',title)
    replace_content = replace_title.replace('{{ Content }}',html_content)
    replace_href = replace_content.replace('href="/',f'href={basepath}') 
    full_html = replace_href.replace('src"/',f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path,'w') as f:
        f.write(full_html)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith('#'):
            return block.strip('#').strip()
        raise Exception('there is no h1 header')
    
def generate_pages_recursive(dir_path_content,template_path,dest_dir_path,basepath):
    contents = os.listdir(dir_path_content)
    for content in contents:
        current_path = os.path.join(dir_path_content,content)
        target_path = os.path.join(dest_dir_path,content)
        if os.path.isfile(current_path):
            if current_path.endswith('.md'):
                #html_target = target_path.replace('.md','.html')
                html_target = Path(target_path).with_suffix('.html')
                generate_page(current_path,template_path,html_target,basepath)
        else:
            generate_pages_recursive(current_path,template_path,target_path,basepath)