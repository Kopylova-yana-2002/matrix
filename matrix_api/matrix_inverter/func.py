import numpy as np
from PIL import Image
import base64

class MatrixCalculator:
    @staticmethod
    def calculate_inverse_matrix(matrix):
        try:
            inverse_matrix = np.linalg.inv(matrix)
        except np.linalg.LinAlgError as e:
            inverse_matrix = None

        return inverse_matrix

def generate_image(image_path):
    img = Image.new('RGB', (200,200), 'red')
    img.save(image_path)

def encode_image(image_path):
    with open(image_path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base_64_enc_data = base64.b64encode(binary_file_data)
        base_64_message = base_64_enc_data.decode('utf-8')

        return base_64_message