import unittest
from static_to_docs import extract_title

class TestDelimiter(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is the Title

**bolded** paragraph

text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is the Title",
        )

    def test_extract_no_title(self):
        md = """
This is the Title

**bolded** paragraph

text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()