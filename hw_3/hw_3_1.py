import numpy as np
from typing import List

class Matrix:
    def __init__(self, data: List[List[int]]) -> None:
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Passed data is not a matrix")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Cannot add matricies with different dimentions")

        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Cannot multiply elements of matricies with different dimentions")

        result = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        if self.cols != other.rows:
            raise ValueError("Cannot multiply matricies with unfitting dimentions")

        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

def main() -> None:
    np.random.seed(0)
    matrix_data_1 = np.random.randint(0, 10, (10, 10)).tolist()
    matrix_data_2 = np.random.randint(0, 10, (10, 10)).tolist()

    matrix1 = Matrix(matrix_data_1)
    matrix2 = Matrix(matrix_data_2)

    with open("matrix+.txt", "w") as f:
        f.write(str(matrix1))
        f.write("\n\n+\n\n")
        f.write(str(matrix2))
        f.write("\n\n=\n\n")
        f.write(str(matrix1 + matrix2))

    with open("matrix*.txt", "w") as f:
        f.write(str(matrix1))
        f.write("\n\n*\n\n")
        f.write(str(matrix2))
        f.write("\n\n=\n\n")
        f.write(str(matrix1 * matrix2))

    with open("matrix@.txt", "w") as f:
        f.write(str(matrix1))
        f.write("\n\n@\n\n")
        f.write(str(matrix2))
        f.write("\n\n=\n\n")
        f.write(str(matrix1 @ matrix2))

if __name__ == "__main__":
    main()
