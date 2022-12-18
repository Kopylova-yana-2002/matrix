import numpy as np
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MatrixInverter
from .serializers import MatrixSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
import time
from inverter import MatrixCalculator


# Create your views here.
class MatrixInverterView(APIView):

    @extend_schema(
        responses={400: str, 200: MatrixSerializer},
        methods=["GET"]
    )
    @extend_schema(
        parameters=[
            OpenApiParameter(name='size', location=OpenApiParameter.QUERY,
                             description='matrix size', required=True, type=int),
            OpenApiParameter(name='matrix', location=OpenApiParameter.QUERY,
                             description='matrix', required=True,
                             examples=[OpenApiExample('2x2 matrix', value='1_2-3_4'),
                                       OpenApiExample('3x3 matrix', value='1_2_3-4_5_6-9_4_2')])
        ],
        description='Calculates inverse matrix',
        examples=[OpenApiExample('2x2 matrix',
                                 value=MatrixSerializer(
                                     instance=MatrixInverter(2, [[1, 2], [2, 1]], [[-0.33, 0.66], [0.66, -0.33]])).data,
                                 response_only=True,
                                 status_codes=[200]
                                 ),
                  OpenApiExample('No size',
                                 value='Размер не указан',
                                 response_only=True,
                                 status_codes=[400]
                                 ),
                  OpenApiExample('Invalid matrix',
                                 value='Матрица неверного размера',
                                 response_only=True,
                                 status_codes=[400]
                                 )
                  ]
    )
    def get(self, request):
        size = request.GET.get('size', None)

        if size is None:
            return Response('Размер не указан', 400)

        try:
            size = int(size)
        except:
            return Response('Размер не число', 400)

        matrix_str = request.GET.get('matrix', None)

        if matrix_str is None:
            return Response('Матрица не указана', 400)

        matrix_rows_str = matrix_str.split('-')

        matrix = []

        for row in matrix_rows_str:
            try:
                row = list(map(float, row.split('_')))
            except:
                return Response('В матрице содержатся недопустимые значения', 400)

            matrix.append(row)

        matrix = np.array(matrix)

        success, result = MatrixCalculator.calculate_inverse_matrix(size, matrix)

        if not success:
            return Response(result, 400)

        for row in result:
            for i in range(len(row)):
                row[i] = round(row[i], 3)

        matrix_inverter = MatrixInverter(size, matrix, result)
        serializer_for_request = MatrixSerializer(instance=matrix_inverter)
        return Response(serializer_for_request.data, 200)
