import os
import types
from typing import Any

from .errors import *
from .decoder import PYONDecoder, is_pyon, is_json, convert, convert_json_to_pyon
from .encoder import PYONEncoder
from .dotnotation import DotNotation

def dumps(obj):
    '''
    convert `obj` to string
    '''
    return PYONEncoder(obj).encode()

def loads(string:str):
    '''
    convert `string` (pyon) to python dict
    '''
    return PYONDecoder(string).decode()

class Read:
    def __init__(self, filepath:str):
        if not os.path.isfile(filepath):
            raise FileExistsError(filepath)
        if not filepath.endswith('.pyon') and not filepath.endswith('.ndb'):
            raise NotPyonFile(filepath)
        
        self.__filepath = filepath

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
                converted = str(convert(obj_as_string))
                file.write(converted)

            return True
        
        with open(filepath, 'w') as file:
            file.write(obj_as_string)

    @property
    def readfile(self) -> str:
        '''
        reads file while still updating it (if a change was occurred)
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
        return os.path.abspath(self.__filepath)

    # Magic methods
    def __repr__(self):
        args = []
        args.append(f'filepath={self.filepath}')

        return f'{self.__class__.__qualname__}({", ".join(args)})'

    def __add__(self, other):
        '''
        Return self+value.
        '''
        self_data = self.readfile
        try:
            other_data = other.readfile
        except AttributeError:
            other_data = other


        if isinstance(self_data, dict) and isinstance(other_data, dict):
            return {**self_data, **other_data}
        
        if isinstance(self_data, (list, int, str)) and isinstance(other_data, (list, int, str)):
            return self_data + other_data

    def __eq__(self, other) -> bool:
        self_data = self.readfile
        try:
            other_data = other.readfile
        except AttributeError:
            other_data = other

        return self_data == other_data

    def __ne__(self, other) -> bool:
        self_data = self.readfile
        try:
            other_data = other.readfile
        except AttributeError:
            other_data = other

        return self_data != other_data