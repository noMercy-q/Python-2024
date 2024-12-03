import numpy as np
from typing import List, Dict, Tuple, Optional

from hw_3_1 import *

def hash(matrix: Matrix) -> int:
    return sum(matrix.data[-1])

def find_collision(B: Matrix, D: Matrix) -> Tuple[Matrix, Matrix]:
    np.random.seed(1)
    generated_hashes = {}
    
    while True:
        A = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
        
        if hash(A) in generated_hashes:
            C = generated_hashes[hash(A)]
            if hash(A) == hash(C) and A != C and (A @ B) != (C @ D):
                return A, C
        else:
            generated_hashes[hash(A)] = A

def save_matrix(filename: str, matrix: Matrix) -> None:
    with open(filename, "w") as f:
        f.write(str(matrix))

def main() -> None:
    np.random.seed(0)
    B = D = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    A, C = find_collision(B, D)

    save_matrix("A.txt", A)
    save_matrix("B.txt", B)
    save_matrix("C.txt", C)
    save_matrix("D.txt", D)

    AB = A @ B
    CD = C @ D
    save_matrix("AB.txt", AB)
    save_matrix("CD.txt", CD)

    with open("hash.txt", "w") as f:
        f.write(f"hash(A @ B): {hash(AB)}\n")
        f.write(f"hash(C @ D): {hash(CD)}\n")

if __name__ == "__main__":
    main()
