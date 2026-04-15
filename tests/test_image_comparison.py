import unittest
from pathlib import Path

import numpy as np

from visual_comparison.exceptions import ImageComparisonException, ImageNotFoundException
from visual_comparison.utils import ImageComparisonUtil
from visual_comparison.visual_comparison_util import ImageComparisonUtil as CompatibilityImport


class TestImageComparisonUtil(unittest.TestCase):
    def test_read_image_raises_for_missing_file(self):
        with self.assertRaises(ImageNotFoundException):
            ImageComparisonUtil.read_image("non_existent_path.jpg")

    def test_check_match_accepts_numpy_arrays(self):
        expected = np.zeros((10, 10, 3), dtype=np.uint8)
        actual = expected.copy()

        self.assertTrue(ImageComparisonUtil.check_match(expected, actual))

    def test_check_mismatch_accepts_numpy_arrays(self):
        expected = np.zeros((10, 10, 3), dtype=np.uint8)
        actual = expected.copy()
        actual[2:5, 2:5] = 255

        self.assertTrue(ImageComparisonUtil.check_mismatch(expected, actual))

    def test_compare_images_rejects_shape_mismatch(self):
        expected = np.zeros((10, 10, 3), dtype=np.uint8)
        actual = np.zeros((12, 10, 3), dtype=np.uint8)

        with self.assertRaises(ImageComparisonException):
            ImageComparisonUtil.compare_images(expected, actual)

    def test_compare_images_writes_result_file(self):
        expected = np.zeros((20, 20, 3), dtype=np.uint8)
        actual = expected.copy()
        actual[4:10, 4:10] = 255

        result_path = Path.cwd() / "test_result.png"
        try:
            similarity_index = ImageComparisonUtil.compare_images(
                expected, actual, str(result_path)
            )

            self.assertLess(similarity_index, 1.0)
            self.assertTrue(result_path.exists())
        finally:
            try:
                result_path.unlink(missing_ok=True)
            except PermissionError:
                pass

    def test_compatibility_import_exposes_same_class(self):
        self.assertIs(CompatibilityImport, ImageComparisonUtil)


if __name__ == "__main__":
    unittest.main()
