#
# # import numpy as np
# import sympy as sp
#
# # A = sp.Matrix([[1, 3, 4],
# #                [0, 2, 0],
# #                [4, 1, 1]])
#
# A = sp.Matrix([[3, 2, -1],
#                [1, 1, 3],
#                [2, -2, 0]])
#
# def print_hi(name):
#
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# def determinant():
#     det = A.det()
#     print("행렬식:", det)
#
#
# def make_symmetric_matrix(A):
#     A_T = A.transpose()
#     A_sym = (A + A_T) / 2
#     return A_sym
#
#
# def print_matrix_pretty(A):
#     print("\n[AT 입력 행렬 보기 좋은 숫자 형태]")
#     for i in range(A.rows):
#         row = [f"{str(A[i, j]):>4}" for j in range(A.cols)]
#         print("".join(row))
#
#
# def print_cofactor_matrix_pretty(A):
#     print("\n[여인자 행렬 보기 좋은 숫자 형태]")
#     for i in range(A.rows):
#         row = []
#         for j in range(A.cols):
#             minor = A.minor_submatrix(i, j).det()
#             cofactor = (-1) ** (i + j) * minor
#             row.append(f"{int(cofactor):4}")  # ← str 대신 int로 변환하고 :4로 간결 정렬
#         print(" ".join(row))
#
#
# def print_cofactor_matrix_with_override(A, override=None):
#     print("\n[여인자 행렬 - 일부 덮어쓰기 출력]")
#     for i in range(A.rows):
#         row = []
#         for j in range(A.cols):
#             if override and (i, j) in override:
#                 val = override[(i, j)]
#             else:
#                 minor = A.minor_submatrix(i, j).det()
#                 val = (-1) ** (i + j) * minor
#             row.append(f"{int(val):4}")
#         print(" ".join(row))
#
#
# def print_cofactor_swapped_row_col(A):
#     print("\n[여인자 행렬 (2행과 2열 바꿔서 출력)]")
#
#     C = A.cofactor_matrix()
#     C_swapped = C.copy()
#
#     # 복사해서 직접 값 교체 (1-indexed → Python 0-based index: 1)
#     for i in range(C.rows):
#         # 임시 저장
#         temp = C_swapped[1, i]
#         C_swapped[1, i] = C_swapped[i, 1]
#         C_swapped[i, 1] = temp
#
#     # 출력
#     for i in range(C_swapped.rows):
#         row = [f"{int(C_swapped[i, j]):4}" for j in range(C_swapped.cols)]
#         print(" ".join(row))
#
#
# def print_minors_and_cofactors(A):
#     print("\n[소행렬식 및 여인자]")
#     for i in range(A.rows):
#         for j in range(A.cols):
#             minor = A.minor_submatrix(i, j).det()
#             cofactor = (-1) ** (i + j) * minor
#             print(f"소행렬식 A[{i + 1},{j + 1}] = {str(minor):<3}, 여인자 = {str(cofactor)}")
#
#
# def use_transpose_matrix_for_cofactor():
#     A_T = A.transpose()
#     print_matrix_pretty(A_T)
#     print_cofactor_matrix_pretty(A_T)
#
#
# def inverse_matrix():
#     # 역행렬
#     A_inv = A.inv()
#     print("\n역행렬:")
#     sp.pprint(A_inv)
#
#     # (1,1) 위치의 소행렬식 (0-indexed)
#     # minor_00 = A.minor_submatrix(0, 0).det()
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     determinant()
#     use_transpose_matrix_for_cofactor()
#     inverse_matrix()
#

import sympy as sp


def analyze_matrix(A):
    print("▶ 입력 행렬 A:")
    sp.pprint(A)

    # 1. 행렬식 계산
    print("\n① 행렬식 (Determinant):")
    det = A.det()
    print(f"det(A) = {det}")

    # 2. 전치 행렬
    print("\n② 전치 행렬 (Transpose of A):")
    A_T = A.T
    sp.pprint(A_T)

    # 3. 전치행렬의 소행렬식 (각 원소에 대한 Minor 출력)
    print("\n③ 전치 행렬의 소행렬식 (Minors of A^T):")
    for i in range(A_T.rows):
        for j in range(A_T.cols):
            minor = A_T.minor_submatrix(i, j).det()
            print(f"Minor(A^T)[{i + 1},{j + 1}] = {minor}")

    # 4. 역행렬
    print("\n④ 역행렬 (Inverse of A):")
    if det == 0:
        print("역행렬이 존재하지 않습니다. (det = 0)")
    else:
        A_inv = A.inv()
        sp.pprint(A_inv)


# 예시 행렬
A = sp.Matrix([
    [3, 2, -1],
    [1, 1, 3],
    [2, -2, 0]
])

# 실행
analyze_matrix(A)