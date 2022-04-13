import ast
import json

from .errors import *

__all__ = ['PYONDecoder', 'is_json', 'is_pyon']

def is_json(obj_as_string:str):
    try:
        json.loads(obj_as_string)
    except ValueError:
        return False
    
    return True

def is_pyon(obj_as_string:str):
    try:
        ast.literal_eval(obj_as_string)
    except ValueError:
        return False

    return True

def convert(string:str):
    '''
    convert `string` to a `dict`
    works on json
    '''
    if not string:
        raise ArgumentTypeError(string, 'Was not expecting empty string')

    if is_json(string):
        return json.loads(string)
    if is_pyon(string):
        return ast.literal_eval(string)
        
    return None

def convert_json(obj_as_string):
    '''
    convert python dict to json string
    '''

    return json.dumps(obj_as_string)

def convert_json_to_pyon(obj_as_string):
    '''
    convert json string to pyon string
    '''
    obj_as_dict = json.loads(obj_as_string)
    obj_as_pyon = convert(obj_as_dict)

    return obj_as_pyon

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

        return 