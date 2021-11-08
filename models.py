"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name, hazardous=False, diameter=float("nan")):
        """Create a new `NearEarthObject`.

        :param designation: A primary designation of a NEO.
        :param name: An IAU name of a NEO.
        :param diameter: The diameter of a NEO, in kilometers, .
        :param hazardous: Whether or not this NEO is potentially hazardous.
        """
        self.designation = designation
        self.name = name if name else None
        self.diameter = float(diameter) if diameter else float("nan")
        self.hazardous = bool(hazardous == "Y")
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        full_name = (
            f"{self.designation} ({self.name})"
            if self.name
            else f"{self.designation}"
        )
        return full_name

    def __str__(self):
        """Return `str(self)`."""
        return (
            f"NEO {self.fullname} has a diameter of {self.diameter} km "
            f"and {'is' if self.hazardous else 'is not'} "
            f"potentially hazardous.In addition, "
            f"include {len(self.approaches)} approaches metadata."
        )

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r}, "
            f"include {len(self.approaches)} approaches metadata."
        )

    def serialize(self):
        """Return a dictionary containing relevant attributes serialization."""
        return {
            "designation": self.designation,
            "name": self.name if self.name is not None else "",
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous,
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, time, designation=None, distance="0.0", velocity="0.0", neo=None):
        """Create a new `CloseApproach`.

        :param time: The date and time (in UTC) of a NEO's closest approach to Earth.
        :param distance: The distance of a NEO's closest approach to Earth.
        :param velocity: The velocity of a NEO's closest approach to Earth.
        :param neo: The NearEarthObject that is making a close approach to Earth.
        """
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)
        self.neo = neo if neo else None
        self._designation = designation

    @property
    def designation(self):
        """Return designation value of a neo."""
        return self._designation

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        return f"{datetime_to_str(self.time)}"

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return (
            f"On {self.time_str}, '{self._designation if self._designation else ''}' "
            f"approaches Earth at a distance of {self.distance.__round__(2)} au and a "
            f"velocity of {self.velocity.__round__(2)} km/s. "
        )

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
        )

    def serialize(self):
        """Return a dictionary containing relevant attributes serialization."""
        return {
            "datetime_utc": datetime_to_str(self.time),
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
        }
