from enum import Enum

class ImageComparisonState(Enum):
    """
    Enum for indicating the result of the comparison.
    """

    SIZE_MISMATCH = "SIZE_MISMATCH"
    MISMATCH = "MISMATCH"
    MATCH = "MATCH"
