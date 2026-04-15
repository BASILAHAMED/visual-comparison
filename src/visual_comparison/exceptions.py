class ImageComparisonException(Exception):
    """Raised when image comparison operations fail."""

    def __init__(self, message, cause=None):
        super().__init__(message)
        self.cause = cause


class ImageNotFoundException(Exception):
    """Raised when an image cannot be loaded from the provided path."""

    def __init__(self, message):
        super().__init__(message)
