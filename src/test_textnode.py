import unittest

from textnode import TextNode, TextType


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
        


if __name__ == "__main__":
    unittest.main()