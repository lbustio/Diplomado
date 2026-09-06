# Chord graph (diagrama de cuerdas)
#
# NOTA: la versión anterior de este script no generaba un diagrama de
# cuerdas; solo construía una tabla con plotly y la subía a una cuenta en
# línea de Chart Studio (chart_studio.plotly.iplot), que además ya está
# obsoleto. Esta versión sí dibuja el diagrama de cuerdas con matplotlib,
# sin depender de ningún servicio externo.
!pip install mpl-chord-diagram

import numpy as np
import matplotlib.pyplot as plt
from mpl_chord_diagram import chord_diagram

names = ['Emma', 'Isabella', 'Ava', 'Olivia', 'Sophia']

# Matriz de flujos/relaciones entre los nombres (misma información que la
# tabla original, sin la columna/fila de "row-sum")
matrix = np.array([
    [16,  3, 28,  0, 18],
    [18,  0, 12,  5, 29],
    [ 9, 11, 17, 27,  0],
    [19,  0, 31, 11, 12],
    [23, 17, 10,  0, 34],
])

chord_diagram(matrix, names)
plt.show()
