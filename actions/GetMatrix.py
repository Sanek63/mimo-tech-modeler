def GetMatrix(r, colCount):
    """
    функция,которая делит вектор-сигнала
    на колл-во-colCount длинну фильтра(3),
    из вектора получаем матрицу
    """
    array = r
    m = len(r)
    matrix = [[]]
    rowIndex = 0
    for ii in range(m):
        matrix[rowIndex].append(array[ii])
        if (ii + 1) % colCount == 0 and (ii + 1) != m:
            rowIndex += 1
            matrix.append([])
    return matrix
