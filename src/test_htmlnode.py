import unittest

from htmlnode import *

class testHTMLNode(unittest.TestCase):
    
    def test_repr(self):
        node = HTMLNode()
        node2 = HTMLNode('href', 'https://www.Google.com')
        # Test repr with all default values
        text1 = 'HTMLNode:\ntag = None\nvalue = None\nchildren = None\nprops = None'
        text2 = node.__repr__()
        self.assertEqual(text1, text2)
        # Test repr with href and value set
        text3 = 'HTMLNode:\ntag = href\nvalue = https://www.Google.com\nchildren = None\nprops = None'
        text4 = node2.__repr__()
        self.assertEqual(text3, text4)
        # Test all default values does not equal one with values
        self.assertNotEqual(text2, text4)
    
    def test_props_to_html(self):
        # Test props_to_html functionality
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank",})
        text1 = ' href="https://www.google.com" target="_blank"'
        text2 = node.props_to_html()
        self.assertEqual(text1, text2)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        