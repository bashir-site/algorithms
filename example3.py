def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(hash((i, j)) % 100)
        matrix.append(row)

    return matrix


def find_minimal_number(matr):
    '''
        Дана матрица размера NxM. Предложи алгоритм поиска минимального элемента в матрице,
        проанализируй его сложность (best, worst, average)
    '''
    print(matr)
    cur = matr[0][0]
    for row in matr:
        for value in row:
            if cur > value:
                cur = value
    return cur


print(find_minimal_number(create_matrix(4,3)))
