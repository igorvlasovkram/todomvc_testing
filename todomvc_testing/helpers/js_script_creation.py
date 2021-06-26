class Todo:
    def __init__(self, value: str, status):
        self.value = value
        self.status = status

    def to_json(self):
        return '{\"completed\":true,\"title\":\"' + self.value + '\"},'
