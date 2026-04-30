
import unittest
from textnode import*
from splitdelimiter import*

class TestDelimiter(unittest.TestCase):

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)

    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_mult_delimit(self):
        node = TextNode("This is _text_ with a _italic_ block _word_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.ITALIC),
            TextNode(" with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" block ", TextType.TEXT),
            TextNode("word", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_delimit(self):
        node = TextNode("This is text with an only text block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        expected = [
            TextNode("This is text with an only text block word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_non_text(self):
        node = TextNode("This is text with an only text block word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        expected = [
            TextNode("This is text with an only text block word", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected)

    def test_unmatched_delimit(self):
        node = TextNode("This is text with _bold text block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)
        
if __name__ == "__main__":
    unittest.main()
