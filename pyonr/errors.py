class FileExistsError(Exception):
    def __init__(self, element, message="File does's exist"):
        self.element = element
        self.message = message

        super().__init__(self.message)
    def __str__(self):
        return f'"{self.element}": {self.message}'

class UnexpectedType(Exception):
    def __init__(self, element, message="Unexpected Type"):
        self.element = element
        self.message = message

        super().__init__(self.message)
    def __str__(self):
        return f'"{self.element}": {self.message}'

class ArgumentTypeError(Exception):
    def __init__(self, element, message="Unexpected Type"):
        self.element = element
        self.message = message

        super().__init__(self.message)
    def __str__(self):
        return f'"{self.element}": {self.message}'