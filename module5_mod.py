class NumberCollection:
    def __init__(self):
        self._numbers = []

    def insert(self, value):
        self._numbers.append(value)

    def search(self, value):
        for index, number in enumerate(self._numbers, start=1):
            if number == value:
                return index
        return -1
