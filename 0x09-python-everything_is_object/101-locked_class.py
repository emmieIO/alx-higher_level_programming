#!/usr/bin/python3
class LockedClass:
    """
    A class that prevents the dynamic creation of new instance attributes
    except for the 'first_name' attribute.

    Attributes:
        None

    Methods:
        __setattr__(self, name, value):
            Overrides the default attribute assignment behavior to allow
            setting 'first_name' and raise an AttributeError for other
            attribute names.
    """

    def __setattr__(self, name, value):
        """
        Override the attribute assignment behavior.

        Args:
            name (str): The name of the attribute being assigned.
            value: The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute name is not 'first_name'.
        """
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
