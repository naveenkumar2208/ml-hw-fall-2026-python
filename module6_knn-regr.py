import numpy as np


class KNNRegressor:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.x_values = np.zeros(n)
        self.y_values = np.zeros(n)
        self.count = 0

    def insert(self, x, y):
        self.x_values[self.count] = x
        self.y_values[self.count] = y
        self.count = self.count + 1

    def predict(self, x):
        distances = np.abs(self.x_values - x)
        nearest = np.argsort(distances)
        nearest_y = self.y_values[nearest[0:self.k]]
        result = np.mean(nearest_y)
        return result


def main():
    n = int(input("Enter N: "))
    if n <= 0:
        print("Error: N must be a positive integer")
        return

    k = int(input("Enter k: "))
    if k <= 0:
        print("Error: k must be a positive integer")
        return

    knn = KNNRegressor(n, k)

    for i in range(n):
        x = float(input(f"Enter x {i + 1}: "))
        y = float(input(f"Enter y {i + 1}: "))
        knn.insert(x, y)

    x = float(input("Enter X: "))

    if k > n:
        print("Error: k must be less than or equal to N")
    else:
        print(knn.predict(x))


if __name__ == "__main__":
    main()
