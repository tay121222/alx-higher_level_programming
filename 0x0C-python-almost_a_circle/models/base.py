#!/usr/bin/python3
"""Contains Base of other classes"""
import json
import csv
from os import path


class Base:
    """Base of other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs:
            json_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = None
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return {}
        with open(filename, 'r') as file:
            json_data = file.read()
            data_list = cls.from_json_string(json_data)
            return [cls.create(**data) for data in data_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']

            writer.writerow(fieldnames)

            for obj in list_objs:
                writer.writerow(
                        [getattr(obj, field) for field in fieldnames]
                        )

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        ret = []
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    row = [int(r) for r in row]
                    if cls.__name__ == "Rectangle":
                        d = {
                                "id": row[0], "width": row[1],
                                "height": row[2],
                                "x": row[3], "y": row[4]
                                }
                    else:
                        d = {
                                "id": row[0], "size": row[1],
                                "x": row[2], "y": row[3]
                                }
                    ret.append(cls.create(**d))
            return ret
        except IOError:
            return []
