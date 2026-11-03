from module5_mod import NumberCollection


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
