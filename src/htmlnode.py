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
        return result
    
    def __repr__(self):
        return (f"HTMLNode:\ntag = {self.tag}\nvalue = {self.value}\nchildren = {self.children}\nprops = {self.props}")