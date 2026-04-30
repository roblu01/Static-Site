from textnode import*

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