from vectoresmatricescomplejos import *
import matplotlib.pyplot as plot
import numpy as np

def sistemaprobabicuantico(matriz,vectori,clicks):
    """Funcion que calcula el sistema probabilistico cuantico
        (list2d,list,int)-->list"""
    if type(clicks) == int and clicks >= 0:
        for i in range(clicks):
            matrizmu = multiplimatr(matriz,matriz[:])
        #
        for k in range(len(matrizmu)):
            fila = []
            for j in range(len(matrizmu[i])):
                fila.append([modulo(matrizmu[k][j])**2])
            matriz[k] = fila
        return matriz
    else:
        ArithmeticError

def graficaprobabilidades(vector):
    """Funcion que grafica con un diagrama de barras la probabilidad de un vector de estados
        (list) --> grafica"""
    x = np.array([ x for x in range( len(vector) )])
    y = np.array([ round(vector[x][0]*100,2) for x in range(len(vector))])

    plot.bar( x,y , color ='pink', align='center')
    plot.title('Probabilidades vector')
    plot.show()
matrizdoblerendija = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],[[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [0, 0],[1, 0], [0, 0], [0, 0]],[[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],[[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
estadoi = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
resp = accion([[[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],[[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],[[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],[[0.1666666666666667, 0], [0.3333333333333334, 0], [0.0, 0], [1.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],[[0.1666666666666667, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [1.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],[[0.0, 0], [0.3333333333333334, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [1.0, 0], [0.0, 0], [0.0, 0]],[[0.1666666666666667, 0], [0.0, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [0.0, 0], [1.0, 0], [0.0, 0]],[[0.1666666666666667, 0], [0.0, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [1.0, 0]]], estadoi)
print(graficaprobabilidades(resp))