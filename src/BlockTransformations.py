from enum import Enum
import re
from htmlnode import *
from textnode import *
from InlineTransformations import *

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks

def block_to_block_type(block):
    heading = re.compile(r"^#{1,6}\s")
    code = re.compile(r"^```[\s\S]*?```$", re.MULTILINE)
    quote = re.compile(r"^>", re.MULTILINE)
    unordered_list = re.compile(r"^-\s", re.MULTILINE)
    ordered_list = re.compile(r"^(\d+)\.\s", re.MULTILINE)

    if re.match(heading, block):
        return BlockType.HEADING
    elif re.match(code, block):
        return BlockType.CODE
    elif re.match(quote, block):
        return BlockType.QUOTE
    elif re.match(unordered_list, block):
        return BlockType.UNORDERED_LIST
    elif re.match(ordered_list, block):
        numbers = [int(match.group(1)) for match in re.finditer(ordered_list, block)]
        if numbers and all(numbers[i] + 1 == numbers[i + 1] for i in range(len(numbers) - 1)):
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH