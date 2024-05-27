#!/usr/bin/python3
"""To define a base model for rectangle and square"""

import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of dictionary lists

        Args:
            list_dictionaries (list): dictionary list
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """To save to a file using the list_objs

        Args:
            save_to_file(cls, list_objs)
            cls:same as self
            list_objs: a list of instance inheriting from base
        """
        filename = cls.__name__+ ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Method to return the deserialization of JSON string.

        Args:
            json_string: a string representing a list of dictionaries

        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """To create an instance of the base with all attributes set.

        Args:
            **dictionary: used as a double pointer to a dictionary

        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """To update a list of instances."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method to write the CSV serialization of a 
        list of object to a file

        Args:
            list_objs (list): Inherited Base instance list
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id","size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
                for items in list_objs:
                    writer.writerow(items.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Method to read the CSV deserialization of a
        list of object from a file

        Args:
            list_objs (list): Inherited Base instance list

        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dict = [dict([k, int(v)] for k, v in c.items())
                            for c in list_dict]
                return [cls.create(**c) for c in  list_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Method to give a graphical representation of 
        rectangle list and square list

        Args:
            list_rectangle: for rectangle's list
            list_squares: for square's list
        """
        tut = turtle.Turtle()
        tut.screen.bgcolor("#b7323c")
        tut.pensize(3)
        tut.shape("turtle")

        tut.color("#ffffff")
        for rect in list_rectangles:
            tut.showturtle()
            tut.up()
            tut.goto(rect.x, rect.y)
            tut.down()
            for i in range(2):
                tut.forward(rect.width)
                tut.left(90)
                tut.forward(rect.height)
                tut.left(90)
            tut.hideturtle()

        tut.color("#b5e3d8")
        for squr in list_squares:
            tut.showturtle()
            tut.up()
            tut.goto(squr.x, squr.y)
            tut.down()
            for i in range(2):
                tut.forward(squr.width)
                tut.left(90)
                tut.forward(squr.height)
                tut.left(90)
                tut.hideturtle()

        turtle.exitonclick()
