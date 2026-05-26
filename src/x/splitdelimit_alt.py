from textnode import*

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        separated_list = old_node.text.split(delimiter,2)

        if len(separated_list)==2:
            raise Exception('delimiter is not supported')
        
        for i in range(0,len(separated_list)):
            if i == 1:
                new_nodes.append(TextNode(separated_list[i],text_type))
            else:
                new_nodes.append(TextNode(separated_list[i],TextType.TEXT))
                
        if delimiter in separated_list[2]:
            node = TextNode(separated_list[2],TextType.TEXT)
            deli = split_nodes_delimiter([node],delimiter,text_type)
            new_nodes.append(deli)
    return new_nodes