from typing import List

Matrix = List[List[float]]

def matsum(A: Matrix, B: Matrix) -> Matrix:
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def matsub(A: Matrix, B: Matrix) -> Matrix:
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

def matmul(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    result = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result

def scalarsum(s: float, A: Matrix) -> Matrix:
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + s)
        result.append(row)
    return result

def scalarsub(s: float, A: Matrix) -> Matrix:
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - s)
        result.append(row)
    return result

def matnorm(A: Matrix) -> Matrix:
    total = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            total += A[i][j] ** 2
    norm = total ** 0.5

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] / norm)
        result.append(row)
    return result

# Test
if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6]]
    B = [[7, 8, 9],
         [10, 11, 12]]
    print("A+B =", matsum(A, B))
    print("A-B =", matsub(A, B))

    C = [[1, 2],
         [3, 4],
         [5, 6]]
    D = [[7, 8, 9],
         [10, 11, 12]]
    print("C*D =", matmul(C, D))

    print("A+10 =", scalarsum(10, A))
    print("A-1.5 =", scalarsub(1.5, A))

    E = [[3, 4]]
    print("norm(E) =", matnorm(E))