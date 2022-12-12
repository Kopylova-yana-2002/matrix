import numpy as np
from django.test import TestCase
from matrix_api.app.matrix_calculator import MatrixCalculator


class InverseMatrixTests(TestCase):
    def test_inverse_calculation_has_result(self):
        '''
        Тестирование что при вычислении обратной матрицы есть результат и он верный
        '''
        origin_matrix = np.array([[2, 2], [2, 1]])
        inverse_matrix_answer = np.array([[-0.5, 1], [1, -1]])
        inverse_matrix = MatrixCalculator.calculate_inverse_matrix(origin_matrix)
        self.assertIsNot(inverse_matrix, None)
        for i in range(len(inverse_matrix_answer)):
            self.assertListEqual(list(inverse_matrix[i]), list(inverse_matrix_answer[i]))

    def test_inverse_calculation_result_is_none(self):
        '''
        Тестирование что при вычислении обратной матрицы нет результата, когда определитель 0
        '''
        origin_matrix = np.array([[2, 2], [2, 2]])
        inverse_matrix = MatrixCalculator.calculate_inverse_matrix(origin_matrix)
        self.assertIs(inverse_matrix, None)

