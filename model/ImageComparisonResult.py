import os
from enum import Enum
from PIL import Image

class ImageComparisonState(Enum):
    """
    Enum representing the state of image comparison.
    """
    SIZE_MISMATCH = "SIZE_MISMATCH"
    MISMATCH = "MISMATCH"
    MATCH = "MATCH"


class ImageComparisonResult:
    """
    Data transfer object containing all the needed data for the result of the comparison.
    """

    def __init__(self):
        """
        Initializes a new ImageComparisonResult instance.
        """
        self.expected = None
        self.actual = None
        self.result = None
        self.image_comparison_state = None
        self.difference_percent = None
        self.rectangles = []

    @classmethod
    def default_size_mismatch_result(cls, expected, actual, difference_percent):
        """
        Creates a default instance of ImageComparisonResult with SIZE_MISMATCH state.

        :param expected: Expected image (PIL Image object).
        :param actual: Actual image (PIL Image object).
        :param difference_percent: The percentage of differences between images.
        :return: Instance of the ImageComparisonResult object.
        """
        result = cls()
        result.image_comparison_state = ImageComparisonState.SIZE_MISMATCH
        result.difference_percent = difference_percent
        result.expected = expected
        result.actual = actual
        result.result = actual
        result.rectangles = []
        return result

    @classmethod
    def default_mismatch_result(cls, expected, actual, difference_percent):
        """
        Creates a default instance of ImageComparisonResult with MISMATCH state.

        :param expected: Expected image (PIL Image object).
        :param actual: Actual image (PIL Image object).
        :param difference_percent: The percentage of differences between images.
        :return: Instance of the ImageComparisonResult object.
        """
        result = cls()
        result.image_comparison_state = ImageComparisonState.MISMATCH
        result.difference_percent = difference_percent
        result.expected = expected
        result.actual = actual
        result.result = actual
        result.rectangles = []
        return result

    @classmethod
    def default_match_result(cls, expected, actual):
        """
        Creates a default instance of ImageComparisonResult with MATCH state.

        :param expected: Expected image (PIL Image object).
        :param actual: Actual image (PIL Image object).
        :return: Instance of the ImageComparisonResult object.
        """
        result = cls()
        result.image_comparison_state = ImageComparisonState.MATCH
        result.expected = expected
        result.actual = actual
        result.result = actual
        result.rectangles = []
        return result

    def write_result_to(self, file_path):
        """
        Saves the image to the provided file path.

        :param file_path: The file path to save the image.
        :return: This ImageComparisonResult object.
        """
        self.result.save(file_path)
        return self
