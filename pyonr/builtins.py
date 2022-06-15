from requests import get
from typing import Any
from warnings import warn
import os.path
from json import loads, dumps

from .errors import *

def fetch(url_or_path:str) -> Any:
   if os.path.isfile(url_or_path): # if "url_or_path" is a file
      with open(url_or_path, 'r', encoding='utf-8') as file:
         file_data = file.read()

         if is_pyon(file_data) or is_json(file_data):
            return convert(file_data)
            
         warn('Warning: The path given is not either pyon or json, it will import the file text for you')
         return file.read()

   # if it's a url (it could not be a url but requests will raise an Exception)
   url_content = get(url_or_path).content.decode('utf-8')
   if is_pyon(url_content) or is_json(url_content):
      return convert(url_content)
   
   warn('Warning: The URL given is not either pyon or json, it will import the html string for you')
   return url_content

builtins = {'fetch': fetch}
def is_json(obj_as_string:str):
    '''
    checks if `obj_as_string` is json
    return `bool`
    '''
    try:
        loads(obj_as_string)
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
        eval(obj_as_string, builtins)
    except ValueError:
        return False
    except SyntaxError:
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
        return loads(string)
    if is_pyon(string):
        return eval(string, builtins)

    return None

def convert_json_to_pyon(string):
    '''
    convert json string to pyon string
    '''
    obj_as_dict = loads(string)
    obj_as_pyon = convert(str(obj_as_dict))

    return obj_as_pyon