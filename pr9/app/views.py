from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from rest_framework.response import Response
from rest_framework.views import APIView
from .Models import MatrixInverter
from .seriaaizers import MatrixSerializer



# Create your views here.
class MatrixInverterView(APIView):



    def get(self, request):
        size = request.GET.get('size', None)

        if size is None:
            return HttpResponse('Размер не указан')

        try:
            size = int(size)
        except:
            return HttpResponse('Размер не число')

        if size <= 0:
            return HttpResponse('Размер меньше или равен 0')

        matrix = request.GET.get('matrix', None)

        if matrix is None:
            return HttpResponse('Матрица не указана')

        matrix = matrix.split('-')

        new_matrix = []

        if len(matrix) != size:
            return HttpResponse('Матрица неверного размера')

        for row in matrix:
            try:
                row = list(map(float, row.split('_')))
            except:
                return HttpResponse('В матрице содержатся недопустимые значения')

            if len(row) != size:
                return HttpResponse('Реверный размер строки в матрице')

            new_matrix.append(row)

        new_matrix = np.array(new_matrix)

        try:
            inverse_matrix = np.linalg.inv(new_matrix)
        except np.linalg.LinAlgError as e:
            return HttpResponse("Определитель матрицы равен нулю")

        for row in inverse_matrix:
            for i in range(len(row)):
                row[i] = round(row[i], 3)

        matrixInverter = MatrixInverter(size, new_matrix, inverse_matrix)
        serializer_for_request = MatrixSerializer(instance=matrixInverter)
        return Response(serializer_for_request.data)

