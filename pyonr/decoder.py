from .converter import convert, STR, OBJ

class PYONDecoder:
    def __init__(self, obj, encoding):
        self.obj = obj
        self.encoding = encoding

    def decode(self):
        obj = self.obj

        return convert(STR, OBJ, obj)