class LocationException(Exception):
    # Raised when the given coordinates cannot be found
    pass


class InvalidCoordinateException(Exception):
    # Raised when an invalid coordinate was passed into a function
    pass