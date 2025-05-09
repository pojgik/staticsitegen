from textnode import *
from htmlnode import *

def main():
    node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(node.__repr__())
    htmlNode = HTMLNode()
    print(htmlNode.__repr__())
    
if __name__ == '__main__':
    main()