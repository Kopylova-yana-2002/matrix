import numpy as np

class MatrixCalculator:
    @staticmethod
    def calculate_inverse_matrix(matrix):
        try:
            inverse_matrix = np.linalg.inv(matrix)
        except np.linalg.LinAlgError as e:
            inverse_matrix = None

        return inverse_matrix
