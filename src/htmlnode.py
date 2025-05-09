class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError('Not Yet Implemented')
    
    def props_to_html(self):
        result = " "
        for prop in self.props:
            result = result + prop + "=" + f"\"{self.props[prop]}\" "
        return result[:-1]
    
    def __repr__(self):
        return (f"HTMLNode:\ntag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError('Leaf nodes MUST have a value')
        elif self.tag == None:
            return self.value
        else:
            result = "<" + self.tag
            if self.props != None:
                result = result + self.props_to_html() + ">"
            else:
                result = result + ">"
            result = result + self.value + f"</{self.tag}>"
            return result