import os
from typing import Any
from ast import literal_eval

from .errors import *
from .decoder import PYONDecoder
from .encoder import PYONEncoder
from .converter import convert, PYON, JSON, OBJ, STR
from .builtins import is_pyon, is_json

class Read:
    def __init__(self, filepath:str, encoding:str='utf-8'):
        self.filepath = filepath
        self.encoding = encoding

        with open(filepath, 'r', encoding=self.encoding) as file:
            PYONDecoder(file.read(), self.encoding).decode()

    def write(self, obj):
        filepath = self.filepath
        
        with open(filepath, 'w', encoding=self.encoding) as file:
            file.write(PYONEncoder(obj, self.encoding).encode())

    @property
    def read(self) -> Any:
        filepath = self.filepath

        with open(filepath, 'r', encoding=self.encoding) as file:
            return PYONDecoder(file.read(), self.encoding).decode()


    
    def __repr__(self) -> str:
        args = []
        args.append(f'filepath={self.filepath}')
        args.append(f'encoding={self.encoding}')

        return f'{self.__class__.__qualname__}({", ".join(args)})'

    def __str__(self) -> str:
        return convert(PYON, STR, self.read)

def read(fp:str, encoding:str='utf-8') -> Read:
    return Read(fp, encoding)