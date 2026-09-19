import numpy as np

def concatenar_listas(*listas, dtype=None):

    if not listas:
        return np.array([], dtype=dtype)
    return np.concatenate([np.asarray(I, dtype=dtype).ravel() for I in listas])

grupos = []
for i in range(1, 5):    
    grupos.append([i] * i)

print(concatenar_listas(*grupos))