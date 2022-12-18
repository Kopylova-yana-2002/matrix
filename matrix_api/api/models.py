from django.db import models


class MatrixInverter:
    def __init__(self, size, matrix, invertedMatrix):
        self.size = size
        self.matrix = matrix
        self.invertedMatrix = invertedMatrix
