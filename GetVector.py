import numpy as np

def GetVector(vector1, vector2):
    """
    Данная функция создает из 2-х векторов один вектор, в котором элементы чередуются
    """
    nn = np.size(vector1) + np.size(vector2)
    s = np.zeros(nn, float)
    vecIndex1 = 0
    vecIndex2 = 0
    for kk in range(nn):
        if (kk + 1) % 2 != 0:
            s[kk] = vector1[vecIndex1]
            vecIndex1 += 1
        else:
            s[kk] = vector2[vecIndex2]
            vecIndex2 += 1
    return s
