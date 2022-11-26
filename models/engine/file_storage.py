#!/usr/bin/python3
import json
from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place, "Amenity": Amenity, "City": City, "Review": Review,"State": State}
    
    def all(self):
        return self.__objects
    def new(self,obj):
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key,obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path,'w',encoding="UTF-8")as f:
            json.dump(obj_dict,f)

    def reload(self):
        try:
            with open(self.__file_path,'r',encoding = "UTF-8")as f:
                new_obj_dict = json.load(f)
            for key, obj in new_obj_dict.items():
                obj = self.class_dictt[obj["__class__"]](**obj)
                self.__object[key] = obj
        except FileNotFoundError:
            pass


g = FileStorage()
print(g)
print(g.all())

