__all__ = ['PYONEncoder']

def _convert(obj):
    return str(obj)

class PYONEncoder(object):
    def __init__(self, obj):
        self.obj = obj

    def encode(self):
        return _convert(self.obj)