from pydantic import BaseModel , UUID4 , EmailStr
from pprint import pprint
    
class Cache:
    """A singleton class for initialising the cache"""
    __cache = {}
    __instance = None

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        # print(cls.__instance) # same instance is getting returned
        return cls.__instance

    
    def add(self,id:UUID4|EmailStr,metadata:dict):
        Cache.__cache[id] = metadata
    
    def remove(self,id:UUID4|EmailStr):
        if Cache.__id_exists_in_cache(id=id):
            Cache.__cache.pop(id)

    @staticmethod
    def __id_exists_in_cache(id:UUID4|EmailStr):
        return id in Cache.__cache

    def get(self,id:UUID4|EmailStr):
        return Cache.__cache.get(id)
    
    def get_all(self):
        return Cache.__cache
    
    def __repr__(self) -> str:
        return str(Cache.__cache)