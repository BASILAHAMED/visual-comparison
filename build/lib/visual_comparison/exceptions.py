class ImageComparisonException(Exception):
    """
    A custom exception class for image comparison failures.
    """

    def __init__(self, message, cause=None):
        """
        Initializes a new ImageComparisonException with the specified detail message and cause.

        :param message: The detail message. The detail message is saved for later retrieval.
        :param cause: The cause of the exception (optional).
        """
        super().__init__(message)
        self.cause = cause

class ImageNotFoundException(Exception):
    """
    A custom exception class for image not found errors.
    """

    def __init__(self, message):
        """
        Initializes a new ImageNotFoundException with the specified detail message.

        : param message: The detail message. The detail message is saved for later retrieval.
        """
        super().__init__(message)