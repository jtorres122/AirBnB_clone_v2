#!/usr/bin/python3
'''Module contains a new engine class'''
import os
from sqlalchemy import *
from sqlalchemy.orm import *
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    '''This class manages storage of hbnb models with a database'''
    __engine = None
    __session = None

    def __init__(self):
        '''Class instantiator'''
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Method queries objs on the current db session'''
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

        new_dict = {}
        if cls is None:
            pass
        else:
            pass
        return new_dict
