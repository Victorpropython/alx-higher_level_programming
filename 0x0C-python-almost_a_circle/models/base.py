#!/usr/bin/python3


class Base:
    """Base model class.

        Use in creating the base class of all the classes in the 
        project 
        
        This class will manage the id attribute to avoid code duplication

        Private Class Attribute:
            __nb_object(int): instances of the base class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base Instance.

        Args:
            id (int): The id of the new instance. if not provided,
                      the id will be automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
