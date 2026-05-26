import unittest
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestDelimiter(unittest.TestCase):
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

        def test_block_heading(self):
            blocks = [
                "# This is a heading",
                "## This is a heading",
                "### This is a heading", 
                "#### This is a heading", 
                "##### This is a heading", 
                "###### This is a heading"] 
            for block in blocks:
                self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        def test_block_not_heading(self):
            blocks = [
                "#not a heading",  
                "####### too many hashes",
                "just a paragraph",
            ]
            for block in blocks:
                self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
        def test_block_ordered(self):
            block = "1. This is an ordered list\n2. This is an ordered list\n3. This is an ordered list"
            self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        def test_block_not_ordered(self):
            block = "1. This is an ordered list\n4. This is an ordered list\n3. This is an ordered list"
            self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        def test_block_code(self):
            blocks = [
                "```\n not a heading```",  
                "```\n this should be a code```",
                "```\naslkdjlaksjdlaksjdlkasjdlaksjd alskdjlaksjd alskdjalskjd laksjd```",
            ]
            for block in blocks:
                self.assertEqual(block_to_block_type(block), BlockType.CODE)
                
if __name__ == "__main__":
    unittest.main()