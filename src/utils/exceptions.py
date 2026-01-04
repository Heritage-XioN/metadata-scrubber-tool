class MetadataException(Exception):
    """Base class for other exceptions in this module."""

    pass


class UnsupportedFormatError(MetadataException):
    """Exception raised when an unsupported file format is encountered."""

    pass


class MetadataNotFoundError(MetadataException):
    """Exception raised when metadata is not found."""

    pass


class MetadataProcessingError(MetadataException):
    """Exception raised when an error occurs during metadata processing."""

    pass
