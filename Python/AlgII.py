import matplotlib.pyplot as plt
import math
import numpy as np
x = np.arange(-10, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x) * 3 + 2 * x)
ax.plot(x, x - 3)

plt.show()
'''
(7x - 5)(x^3 + 4x)
7x^4 + 28x^2
-5x^3 - 20x
7x^4 - 5x^3 + 28x^2 - 20x

(2x^2 + 15x - 8)/(x^2 + 10x + 16)
                 (x + 8)(x + 2)
2x^2 + 65x - x - 8
-1(x + 8) + 2x(x + 8)
(2x - 1)(x + 8)

2x - 1
------  (when x != -2)
x + 2


'''