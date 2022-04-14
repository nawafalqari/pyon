import os

from .errors import *
from .decoder import PYONDecoder, is_pyon, is_json, convert, convert_json, convert_json_to_pyon
from .encoder import PYONEncoder

def dumps(obj):
    '''
    convert `obj` to string
    '''
    return PYONEncoder(obj).encode()

def loads(string):
    '''
    convert `string` (pyon) to python dict
    '''
    return PYONDecoder(string).decode()

class Read:
    def __init__(self, filepath:str, auto_save:bool=False):
        if not os.path.isfile(filepath):
            raise FileExistsError(filepath)
        if not isinstance(auto_save, bool):
            raise UnexpectedType(auto_save, 'Expected Bool')
        
        self.__filepath = filepath
        self.__auto_save = auto_save

        with open(self.__filepath, 'r') as file:
            self.__decoder = PYONDecoder(file.read())
            self.__file_data = self.__decoder.decode()

    def write(self, obj):
        '''
        write `obj` to file

        `obj` can be pyon string or json string or python dict
        '''
        filepath = self.__filepath
        obj_as_string = dumps(obj)
        
        # types handling
        if isinstance(obj, dict):
            with open(filepath, 'w') as file:
                file.write(obj_as_string)

            return True
        if is_pyon(obj_as_string):
            with open(filepath, 'w') as file:
                file.write(obj_as_string)

            return True
        if is_json(obj_as_string):
            with open(filepath, 'w') as file:
                file.write(convert_json_to_pyon(obj))

            return True

        
        with open(filepath, 'w') as file:
            file.write(obj_as_string)

    @property
    def readfile(self):
        '''
        reads file while still updating it (if a change was occure)
        '''
        with open(self.__filepath, 'r') as file:
            self.__decoder = PYONDecoder(file.read())
            self.__file_data = self.__decoder.decode()

        return self.__file_data

    @property
    def filepath(self):
        '''
        return filepath
        '''
        return self.__filepath

    @property
    def auto_save(self):
        '''
        returns if user wanted the file to be autosaved
        '''
        return self.__auto_save