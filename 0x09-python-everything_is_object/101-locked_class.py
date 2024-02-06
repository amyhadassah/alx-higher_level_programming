#!/usr/bin/python3
class LockedClass:
    """
    LockedClass allows only `first_name` as a dynamic instance attribute.
    Attempting to set any other attribute will raise an AttributeError.
    """

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        self.__dict__[name] = value

