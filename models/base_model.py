#!/usr/bin/python3
"""Module for Base class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Class for base model of object hierarchy."""

    def __init__(self, *args, **kwarg):
        """Initialization of a base model"""

        if kwarg is not None and kwarg != {}:
            for key in kwarg:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwarg["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwarg["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwarg[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_diction = self.__dict__.copy()
        my_diction["__class__"] = type(self).__name__
        my_diction["created_at"] = my_dict["created_at"].isoformat()
        my_diction["updated_at"] = my_dict["updated_at"].isoformat()
        return my_diction
