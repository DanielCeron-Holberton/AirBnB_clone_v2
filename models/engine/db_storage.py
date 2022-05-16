#!/usr/bin/python3
"""Module contains database engine"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from os import getenv
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class_dict = {'City': City, 'State': State, 'User': User,
              'Place': Place, 'Review': Review, 'Amenity': Amenity}


class DBStorage():
    """Engine class"""
    __engine = None
    __session = None

    def __init__(self):
        """Construct a dbclass"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_MYSQL_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query for all classes"""
        obj_dict = {}
        if cls:
            try:
                query_result = self.__session.query(cls).all()
            except Exception:
                print("Class not found")
                pass
        else:
            try:
                for key in class_dict.keys():
                    value = class_dict.get(key)
                    query_result = self.__session.query(value).all()
            except Exception:
                pass
        for obj in query_result:
            obj_dict[obj.__class__.__name__+'.' + obj.id] = obj

        return obj_dict

    def new(self, obj):
        """Creates and save a new object"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """Commit the changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object"""
        if obj:
            self.__session.delete(obj)
        self.save()

    def reload(self):
        """Creates session on start"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
