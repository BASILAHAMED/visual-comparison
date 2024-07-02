import unittest
from image_comparison.exceptions import ImageNotFoundException
from image_comparison.image_comparison_util import ImageComparisonUtil

class TestImageComparisonUtil(unittest.TestCase):
    def test_read_image_from_resources(self):
        with self.assertRaises(ImageNotFoundException):
            ImageComparisonUtil.read_image_from_resources("non_existent_path.jpg")
    
if __name__ == "__main__":
    unittest.main()
