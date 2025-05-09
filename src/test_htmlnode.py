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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node_2 = LeafNode("span", "child2")
        child_node_3 = LeafNode("span", "child3")
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [child_node, child_node_2])
        parent_node3 = ParentNode("div", [parent_node, child_node_3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        self.assertEqual(parent_node2.to_html(), "<div><span>child</span><span>child2</span></div>")
        self.assertEqual(parent_node3.to_html(), "<div><div><span>child</span></div><span>child3</span></div>")
        

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_with_no_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("span", "child")]).to_html()
        self.assertEqual(str(context.exception), 'Parent nodes MUST have a tag')

    def test_parent_node_with_no_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), 'Parent nodes MUST have children')

    def test_parent_node_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_parent_node_with_multiple_children(self):
        child_node_1 = LeafNode("span", "child1")
        child_node_2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), '<div><span>child1</span><span>child2</span></div>')
