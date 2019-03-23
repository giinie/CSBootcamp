class Error(Exception):
    """Base-class for all exceptions raised by this module."""


class InvalidDensityError(Error):
    """There was a problem with a provided density value."""


class NegativeDensityError(InvalidDensityError):
    """A provided density value was negative."""


class WeightError(Error):
    """Base-class for weight calculation errors."""


class VolumeError(Error):
    """Base-class for volume calculation errors."""


class DensityError(Error):
    """Base-class for density calculation errors."""


def determine_weight(volume, density):
    if density == 0:
        raise InvalidDensityError('Density must be positive')
    elif density < 0:
        raise NegativeDensityError

