from textnode import *

def main():
    node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(node.__repr__())
    
if __name__ == '__main__':
    main()