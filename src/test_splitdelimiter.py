
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
    
    def test_extract_markdown_images_A(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_B(self):
        matches = extract_markdown_images(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

        
if __name__ == "__main__":
    unittest.main()
