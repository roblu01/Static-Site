import unittest
from htmlnode import*
from textnode import*

class TestHTMLnode(unittest.TestCase):
    def test_props(self):
        props={
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode(None,None,None,props)
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
    
    def test_props_None(self):
        node = HTMLNode(None,None,None,None)
        self.assertEqual(node.props_to_html(),"")
    
    def test_props_empty(self):
        node = HTMLNode(None,None,None,{})
        self.assertEqual(node.props_to_html(),"")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_anchor_tag(self):
        node = LeafNode("a","Click me!",{"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )   
    
    def test_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):parent_node.to_html()
        # self.assertRaises(ValueError, parent_node.to_html) 

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node") 

if __name__ == "__main__":
    unittest.main()