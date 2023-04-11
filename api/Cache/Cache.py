from pydantic import BaseModel , UUID4
    
class Cache:
    """A singleton class for initialising the cache"""
    __cache = {}
    __instance = None

    def __new__(cls,*args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        # print(cls.__instance) # same instance is getting returned
        return cls.__instance

    
    def add(self,id:UUID4,metadata:dict):
        id = self.id
        Cache.__cache[id] = metadata
    
    def remove(self):
        id = self.id
        if self[id]:
            Cache.__cache.pop(id)

    def get(self):
        id = self.id
        return Cache.__cache.get(id)
    
    def __repr__(self) -> str:
        return str(Cache.__cache)