import numpy as np
from django.test import TestCase
from inverter import MatrixCalculator


class InverseMatrixTests(TestCase):
    def test_inverse_calculation_has_result(self):
        '''
        Тестирование что при вычислении обратной матрицы есть результат и он верный
        '''
        size = 2
        origin_matrix = np.array([[2, 2], [2, 1]])
        inverse_matrix_answer = np.array([[-0.5, 1], [1, -1]])
        success, inverse_matrix = MatrixCalculator.calculate_inverse_matrix(size, origin_matrix)
        self.assertEqual(success, True)
        for i in range(len(inverse_matrix_answer)):
            self.assertListEqual(list(inverse_matrix[i]), list(inverse_matrix_answer[i]))

    def test_inverse_calculation_determinator_is_0(self):
        '''
        Тестирование что при вычислении обратной матрицы нет результата, когда определитель 0
        '''
        size = 2
        origin_matrix = np.array([[2, 2], [2, 2]])
        success, error_msg = MatrixCalculator.calculate_inverse_matrix(size, origin_matrix)
        self.assertEqual(success, False)
        self.assertEqual(error_msg, 'Определитель матрицы равен нулю')

    def test_inverse_calculation_wrong_amount_of_rows(self):
        size = 2
        origin_matrix = np.array([[2, 2], [2, 2], [2, 2]])
        success, error_msg = MatrixCalculator.calculate_inverse_matrix(size, origin_matrix)
        self.assertEqual(success, False)
        self.assertEqual(error_msg, 'Матрица неверного размера')

    def test_inverse_calculation_non_positive_size(self):
        '''
        Тестирование что переданный размер не положительный
        '''
        size = -1
        origin_matrix = np.array([[2, 2], [2, 2]])
        success, error_msg = MatrixCalculator.calculate_inverse_matrix(size, origin_matrix)
        self.assertEqual(success, False)
        self.assertEqual(error_msg, 'Размер меньше или равен 0')

    def test_inverse_calculation_wrong_amount_of_columns(self):
        '''
        Тестирование что строки в матрице неверного размера
        '''
        size = 2
        origin_matrix = np.array([[2, 3, 2], [2, 4, 2]])
        success, error_msg = MatrixCalculator.calculate_inverse_matrix(size, origin_matrix)
        self.assertEqual(success, False)
        self.assertEqual(error_msg, 'Неверный размер строки в матрице')

