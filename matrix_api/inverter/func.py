import numpy as np


class MatrixCalculator:
    @staticmethod
    def calculate_inverse_matrix(size, matrix):
        if size <= 0:
            return False, 'Размер меньше или равен 0'

        if len(matrix) != size:
            return False, 'Матрица неверного размера'

        for row in matrix:
            if len(row) != size:
                return False, 'Неверный размер строки в матрице'

        try:
            inverse_matrix = np.linalg.inv(matrix)
        except np.linalg.LinAlgError as e:
            return False, "Определитель матрицы равен нулю"

        return True, inverse_matrix
