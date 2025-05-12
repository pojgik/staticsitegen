import unittest

from htmlnode import *
from textnode import *
from BlockTransformations import *

class testBlockTransformations(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_markdown(self):
        md = """"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = """This is a single block."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single block."])

    def test_multiple_consecutive_newlines(self):
        md = """
This is a paragraph



This is another paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a paragraph", "This is another paragraph"])

    def test_only_whitespace(self):
        md = """
   
   
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_special_characters(self):
        md = """!@#$%^&*()_+{}|:"<>?~`"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["!@#$%^&*()_+{}|:\"<>?~`"])

    def test_nested_lists(self):
        md = """- Item 1\n  - Subitem 1\n  - Subitem 2\n- Item 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["- Item 1\n  - Subitem 1\n  - Subitem 2\n- Item 2"])

    def test_headings(self):
        md = """# Heading 1\n\n## Heading 2\n\n### Heading 3"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["# Heading 1", "## Heading 2", "### Heading 3"])

class testBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = """```
def code_block():
    pass
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_invalid_ordered_list(self):
        block = "1. First\n3. Second\n2. Third"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)