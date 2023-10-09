import numpy as np
import RobPy as rp

M = rp.matriz_rotacao_x(43*np.pi/100)
r = rp.cria_vetor3([2, 3, 1])


T = rp.cria_operador4(M, r)

print(T)