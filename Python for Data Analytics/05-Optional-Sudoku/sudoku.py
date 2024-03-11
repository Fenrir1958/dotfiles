# pylint: disable=missing-docstring


def sudoku_validator(grid):
    num_validos = [1,2,3,4,5,6,7,8,9]

    # pass  # YOUR CODE HER
    for index,fila in enumerate(grid):
        if sorted(fila) != num_validos:
            return False
        columnas = []
        for columna in grid:
            columnas.append(columna[index])
        if sorted(columnas) != num_validos:
            return False
        index = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cuadrado = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if sorted(cuadrado) != list(range(1, 10)):
                return False
    return True
