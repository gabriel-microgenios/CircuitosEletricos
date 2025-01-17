#Resolução de Análise de Circuitos Elétricos utilizando Python
#(Problema 4.40 Livro Circuitos Elétricos Nilsson e Riedel): 
#Utilize o método de corrente de malha para encontrar 
#a potência fornecida pela fonte de tensão dependente 
#no circuito ao lado:


#Resolução mais longa
import numpy as np

#Matriz de coeficientes (A):
A = np.array([
    [30, -10, -15],
    [-10, 40, -30],
    [-15, -50, 90]
])

#Vetor dos termos independentes (B):
B = np.array([660, 0, 0])

#Calculo do determinante de A:
det_A = np.linalg.det(A)

if det_A == 0:
    print("O sistema nao tem solucao unica (determinante e zero).")
else:
    #Calculo dos determinantes das matrizes substituidas (Ai):
    I1 = np.linalg.det(np.column_stack((B, A[:, 1], A[:, 2]))) / det_A
    I2 = np.linalg.det(np.column_stack((A[:, 0], B, A[:, 2]))) / det_A
    I3 = np.linalg.det(np.column_stack((A[:, 0], A[:, 1], B))) / det_A

    #Exibe os resultado:
    print("Solucoes:")
    print(f"I1 = {I1:.2f}A, I2 = {I2:.2f}A, I3 = {I3:.2f}A")

#------------------------------------------------------------------------------
#Resolucao mais rápida, usando apenas 1 comando:
# import numpy as np
# 
# #Matriz de coeficientes (A):
# A = np.array([
#     [30, -10, -15],
#     [-10, 40, -30],
#     [-15, -50, 90]
# ])
# 
# #Vetor dos termos independentes (B):
# B = np.array([660, 0, 0])
# 
# #Resolvendo o sistema:
# I = np.linalg.solve(A, B)
# 
# #Exibe os resultado:
# print("Solucoes:")
# print(f"I1 = {I[0]:.2f}A, I2 = {I[1]:.2f}A, I3 = {I[2]:.2f}A")
# 