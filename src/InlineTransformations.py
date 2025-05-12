from enum import Enum
import re
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

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    # Only process text; if the node contains anything else, ignore it
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        images = extract_markdown_images(old_node.text)
        # If no image is found, simply append the original node
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        for image in images:
            image_alt = image[0]
            image_url = image[1]
            
            # Separate text into everything before and everything after the image link
            sections = text.split(f"![{image_alt}]({image_url})", 1)
            if len(sections) == 1:
                # Check that there is indeed an image, just to be safe
                new_nodes.append(old_node)
            elif len(sections) == 2:
                before_text = sections[0]
                after_text = sections[1]
                
                if before_text: # Add the text before the image, if it exists
                    new_nodes.append(TextNode(before_text, TextType.TEXT))
                
                # Add the image as an image
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
                text = after_text
        if len(text) != 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
    
def split_nodes_link(old_nodes):
    new_nodes = []
    # Only process text; if the node contains anything else, ignore it
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        links = extract_markdown_links(old_node.text)
        # If no link is found, simply append the original node
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        for link in links:
            anchor = link[0]
            link_url = link[1]
            
            # Separate text into everything before and everything after the link
            sections = text.split(f"[{anchor}]({link_url})", 1)
            if len(sections) == 1:
                # Check that there is indeed a link, just to be safe
                new_nodes.append(old_node)
            elif len(sections) == 2:
                before_text = sections[0]
                after_text = sections[1]
                
                if before_text: # Add the text before the link, if it exists
                    new_nodes.append(TextNode(before_text, TextType.TEXT))
                
                # Add the link as an link
                new_nodes.append(TextNode(anchor, TextType.LINK, link_url))
                text = after_text
        if len(text) != 0:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes