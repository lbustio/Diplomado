# Area graph

# Instalar los paquetes requeridos
!pip install numpy
!pip install matplotlib

# library
import numpy as np
import matplotlib.pyplot as plt
import random

# Create data
rng = 100
x=range(0,rng)
y=list()

# generating random values
for i in range(rng):
  y.append(random.randint(0,99))

# Area plot
plt.fill_between(x, y)
plt.show()