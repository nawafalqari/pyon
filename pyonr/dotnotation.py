import types

class DotNotation(types.SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        self.__dictionary = dictionary

        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DotNotation(value))
            else:
                self.__setattr__(key, value)

    def to_dict(self) -> dict:
        return self.__dictionary

    def __repr__(self) -> str:
        return f'{self.__dictionary}'