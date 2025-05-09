from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode:
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, target):
        return self.text == target.text and self.text_type == target.text_type and self.url == target.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    typ = text_node.text_type
    text = text_node.text
    if typ is TextType.TEXT:
        return LeafNode(None, text)
    elif typ is TextType.BOLD:
        return LeafNode('b', text)
    elif typ is TextType.ITALIC:
        return LeafNode('i', text)
    elif typ is TextType.CODE:
        return LeafNode('code', text)
    elif typ is TextType.LINK:
        return LeafNode('a', text, {'href': text_node.url})
    elif typ is TextType.IMAGE:
        return LeafNode('img', '', {'src': text_node.url, 'alt': text})
    elif typ is None:
        raise AttributeError('No type')
    else:
        raise ValueError('Invalid Text Type')