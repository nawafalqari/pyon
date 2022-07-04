from .converter import convert, STR, PYON

class PYONDecoder:
    def __init__(self, obj, encoding):
        self.obj = obj
        self.encoding = encoding

    def decode(self):
        obj = self.obj

        return convert(STR, PYON, obj)