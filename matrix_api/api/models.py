from django.db import models

class MatrixInverter:
    def __init__(self, size, matrix, invertedMatrix):
        self.size = size
        self.matrix = matrix
        self.invertedMatrix = invertedMatrix

class PillowImage:
    def __init__(self, image_base64, encoding):
        self.image_base64 = image_base64
        self.encoding = encoding