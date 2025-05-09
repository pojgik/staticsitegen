import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Testing Node Equality
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_different_text_types(self):
        text = "Same text"
        text_types = [TextType.BOLD, TextType.ITALIC, TextType.TEXT, TextType.CODE]
        
        # Testing Non-Equality of Different Text Types
        for i, type1 in enumerate(text_types):
            node1 = TextNode(text, type1)
            for type2 in text_types[i+1:]:
                node2 = TextNode(text, type2)
                self.assertNotEqual(node1, node2)
                
    def test_different_url(self):
        # Testing 2 Unique URLS
        node1 = TextNode('Same text', TextType.TEXT, 'https://www.Youtube.com')
        node2 = TextNode('Same text', TextType.TEXT, 'https://www.Google.com')
        self.assertNotEqual(node1, node2)
        
        # Testing URL vs No URL
        node3 = TextNode('Same text', TextType.TEXT)
        node4 = TextNode('Same text', TextType.TEXT, 'https://www.Google.com')
        self.assertNotEqual(node3, node4)
        
    def test_different_text(self):
        # Testing different test
        node1 = TextNode('Different Text', TextType.TEXT)
        node2 = TextNode('Diff Text', TextType.TEXT)
        self.assertNotEqual(node1, node2)
        
    # def test_text(self):
    #     # Test to_html_node
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, None)
    #     self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node(self):
        # Test TEXT type
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        # Test BOLD type
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

        # Test ITALIC type
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

        # Test CODE type
        node = TextNode("Code snippet", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code snippet")

        # Test LINK type
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

        # Test IMAGE type
        node = TextNode("Image alt text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "Image alt text"})

        # Test invalid text type
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(TextNode("Invalid", "invalid_type"))
        self.assertEqual(str(context.exception), "Invalid Text Type")

        # Test no text type
        with self.assertRaises(AttributeError):
            text_node_to_html_node(TextNode("No type", None))


if __name__ == "__main__":
    unittest.main()