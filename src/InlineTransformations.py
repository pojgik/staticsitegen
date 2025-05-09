from enum import Enum
from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            if node.text.count(delimiter) % 2 != 0:
                raise ValueError(f"Missing closing delimiter {delimiter}")
            split_nodes = node.text.split(delimiter)
            for i in range (0, len(split_nodes)):
                if i % 2 != 0:
                    new_nodes.append(TextNode(split_nodes[i], text_type))
                else:
                    new_nodes.append(TextNode(split_nodes[i], TextType.TEXT))
    return new_nodes