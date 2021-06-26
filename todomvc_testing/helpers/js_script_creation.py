from typing import Literal

Option = Literal['active', 'completed']

class Todo:
    def __init__(self, value: str, status: Option):
        self.value = value
        self.status = status

    def to_json(self):
        if self.status == 'active':
            return '{\"completed\":false,\"title\":\"' + self.value + '\"},'
        else:
            return '{\"completed\":true,\"title\":\"' + self.value + '\"},'
