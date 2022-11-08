import numpy as np
import django


def main():
    n = int(input('Введите размер матрицы '))
    matrix = []
    for i in range(n):
        try:
            a = list(map(int, input().split()))
        except Exception as e:
            print("введена буква")
            exit(0)
        if len(a) != n:
            print('Неверное количество элементов в строке ')
            exit(-1)
        matrix.append(a)
    matrix = np.array(matrix)

    try:
        inverse = np.linalg.inv(matrix)
    except np.linalg.LinAlgError as e:
        print("Определитель матрицы равен нулю")
        exit(0)

    print(str(inverse))


if __name__ == '__main__':
    main()
