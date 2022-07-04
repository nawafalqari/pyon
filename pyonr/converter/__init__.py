from ast import literal_eval
from json import loads as json_loads
from json import dumps as json_dumps

PYON = 'pyon'
JSON = 'json'
OBJ = 'obj'
STR = 'str'

def convert(from_:str, to_:str, str_obj:str):
   '''
   
   Convert from types between (PYON, JSON, Python Object, String)

   `Parameters`:
   `from_`: what to convert from
   `to_`: what to convert to
   `str_obj`: the main object (PYON, JSON, Python Object, String)

   `Supported types`:

   `pyonr.converter.PYON` PYON String,

   `pyonr.converter.JSON` JSON String,

   `pyonr.converter.OBJ` Python Object,

   `pyonr.converter.STR` Python String,

   `Example`:
   ```
   import pyonr.converter as converter

   pyon_str = """
   {
      'str': 'string',
      'set': {1, 2, 3, 'string'}
   }
   """

   converted = converter.convert(converter.PYON, converter.OBJ, pyon_str)

   print(converted)
   # {'str': 'string', 'set': {1, 2, 3, 'string'}}

   print(type(converted))
   # <class 'dict'>
   ```
   
   '''
   if from_ == PYON:
      if to_ == JSON:
         return json_dumps(literal_eval(str_obj)) if isinstance(str_obj, (str, bytes)) else json_dumps(str_obj)
      if to_ == OBJ:
         return literal_eval(str_obj)
      if to_ == STR:
         return str(str_obj)
   
   if from_ == JSON:
      if to_ == PYON:
         return str(json_loads(str_obj))
      if to_ == OBJ:
         return json_loads(str_obj)
      if to_ == STR:
         return json_dumps(str_obj)

   if from_ == OBJ:
      if to_ == PYON:
         return str(str_obj)
      if to_ == JSON:
         return json_dumps(str_obj)
      if to_ == STR:
         return str(str_obj)

   if from_ == STR:
      if to_ == PYON:
         return str(literal_eval(str_obj))
      if to_ == JSON:
         return json_dumps(json_loads(str_obj))
      if to_ == OBJ:
         return literal_eval(str_obj)

def isPYON(obj):
    try:
        literal_eval(obj)
    except:
        return False
    
    return True

def isJSON(obj):
    try:
        pass
    except:
        return False
    
    return True