class ImageNotFoundException(Exception):
    """
    A custom exception class for image not found errors.
    """

    def __init__(self, message):
        """
        Initializes a new ImageNotFoundException with the specified detail message.

        :param message: The detail message. The detail message is saved for later retrieval.
        """
        super().__init__(message)
