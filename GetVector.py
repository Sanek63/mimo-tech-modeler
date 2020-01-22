import numpy

def GetVector(vector1, vector2):
    """
        Данная функция создает из 2-х
        векторов один вектор,
        в котором элементы чередуются
    """
    nn = len(vector1) + len(vector2)
    s = []
    vecIndex1 = 0
    vecIndex2 = 0
    for kk in range(0, nn):
        if ((kk + 1) % 2) != 0:
            s.append(vector1[vecIndex1])
            vecIndex1 = vecIndex1 + 1
        else:
            s.append(vector2[vecIndex2])
            vecIndex2 = vecIndex2 + 1
    return numpy.matrix(s)
