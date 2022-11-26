#!/usr/bin/python3
import uuid
from datetime import datetime
import models

date_format = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    def __init__(self,*args,**kwargs):
        if kwargs:
            for key,value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key],date_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key],date_format)
                elif key == "__class__":
                    pass
                else:
                    setattr(self,key,value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic


#all_objs = storage.all()
#print("-- Reloaded objects --")
#for obj_id in all_objs.keys():
    #obj = all_objs[obj_id]
   # print(obj)
