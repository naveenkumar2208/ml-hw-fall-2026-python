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


def main():
    n = int(input("Enter N: "))
    collection = NumberCollection()

    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))
        collection.insert(number)

    x = int(input("Enter X: "))
    print(collection.search(x))


if __name__ == "__main__":
    main()
