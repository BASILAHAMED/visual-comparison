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
