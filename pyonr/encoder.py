from .converter import convert, PYON, OBJ

class PYONEncoder:
    def __init__(self, obj, encoding):
        self.obj = obj
        self.encoding = encoding

    def encode(self):
        obj = self.obj

        return convert(OBJ, PYON, obj)