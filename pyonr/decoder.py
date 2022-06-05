import ast
import json

from .errors import *

def is_json(obj_as_string:str):
    '''
    checks if `obj_as_string` is json
    return `bool`
    '''
    try:
        json.loads(obj_as_string)
    except ValueError:
        return False
    except TypeError:
        return False
    
    return True

def is_pyon(obj_as_string:str):
    '''
    checks if `obj_as_string` is pyon
    return `bool`
    '''
    try:
        try:
            ast.literal_eval(obj_as_string)
        except:
            eval(obj_as_string)
    except ValueError:
        return False

    return True

def convert(string:str):
    """
    convert `string` to a `dict`
    works on json

    ```python
    pyon = '''
    {
        "user1": {
            "username": "nawaf",
            "email": "nawaf@domain.com",
            "verified": True
        }
    }
    '''

    converted = pyonr.convert(pyon)

    type(converted) # <class 'dict'>
    ```
    """
    if not string:
        raise ArgumentTypeError(string, 'Was not expecting empty string')

    if is_json(string):
        return json.loads(string)
    if is_pyon(string):
        try:
            return ast.literal_eval(string)
        except:
            return eval(string)
        
    return None

def convert_json_to_pyon(string):
    '''
    convert json string to pyon string
    '''
    obj_as_dict = json.loads(string)
    obj_as_pyon = convert(str(obj_as_dict))

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