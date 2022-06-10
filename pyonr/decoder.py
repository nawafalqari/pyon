import ast
import json

from .errors import *
from .builtins import *

class PYONDecoder:
    def __init__(self, obj_as_string:str):
        if not isinstance(obj_as_string, str):
            raise UnexpectedType(obj_as_string, f'Expected `str` not ({type(obj_as_string)})')

        self.obj = obj_as_string

    def decode(self):
        obj = self.obj
        if not obj:
            return None

        return convert(obj)
    
    def decode_json(self):
        '''
        convert obj to a json obj (string)
        '''
        obj = self.obj
        if not obj:
            return '{}'

        return json.dumps(convert(obj))