#!/usr/bin/python3
class LockedClass:
    """
    Prevents the user from creating new instance attributes
    except if the new instance attributes is called 'first_name'
    """

    __slots__ = ["first_name"]
