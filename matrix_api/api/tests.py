from django.urls import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class InverseMatrixAPITests(APITestCase):
    def test_inverse_request_has_result(self):
        '''
        Тестирование корректного запроса
        '''
        url = reverse('inverse') + '?size=2&matrix=2_2-2_1'
        response = self.client.get(url)
        self.assertEqual(response.data,
                         {
                             'size': 2,
                             'matrix': [[2, 2], [2, 1]],
                             'invertedMatrix': [[-0.5, 1], [1, -1]]
                         })
        self.assertEqual(response.status_code, 200)

    def test_inverse_no_size(self):
        '''
        Тестирование запроса без указания размера
        '''
        url = reverse('inverse') + '?matrix=3_2_2-3_2_1'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Размер не указан')
        self.assertEqual(response.status_code, 400)

    def test_inverse_size_is_not_number(self):
        '''
        Тестирование запроса где размер не число
        '''
        url = reverse('inverse') + '?size=abc'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Размер не число')
        self.assertEqual(response.status_code, 400)

    def test_inverse_size_size_is_not_positive(self):
        '''
        Тестирование запросов где размер <= 0
        '''
        url = reverse('inverse') + '?size=0'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Размер меньше или равен 0')
        self.assertEqual(response.status_code, 400)
        url = reverse('inverse') + '?size=-5'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Размер меньше или равен 0')
        self.assertEqual(response.status_code, 400)

    def test_inverse_request_no_matrix(self):
        '''
        Тестирование запроса без матрицы
        '''
        url = reverse('inverse') + '?size=2'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Матрица не указана')
        self.assertEqual(response.status_code, 400)

    def test_inverse_request_wrong_size(self):
        '''
        Тестирование запроса с матрицей неверного размера
        '''
        url = reverse('inverse') + '?size=2&matrix=3_2-2_1-3_3'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Матрица неверного размера')
        self.assertEqual(response.status_code, 400)

    def test_inverse_request_incorrect_data(self):
        '''
        Тестирование запроса с матрицей содержащей не числа
        '''
        url = reverse('inverse') + '?size=3&matrix=3_g-2_1-3_3'
        response = self.client.get(url)
        self.assertEqual(response.data, 'В матрице содержатся недопустимые значения')
        self.assertEqual(response.status_code, 400)

    def test_inverse_request_wrong_row_size(self):
        '''
        Тестирование запроса с матрицей с неверными строками
        '''
        url = reverse('inverse') + '?size=2&matrix=3_2-2_3_1'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Неверный размер строки в матрице')
        self.assertEqual(response.status_code, 400)

    def test_inverse_request_determinator_is_0(self):
        '''
        Тестирование запроса с матрицей с определителем 0
        '''
        url = reverse('inverse') + '?size=2&matrix=2_2-2_2'
        response = self.client.get(url)
        self.assertEqual(response.data, 'Определитель матрицы равен нулю')
        self.assertEqual(response.status_code, 400)
