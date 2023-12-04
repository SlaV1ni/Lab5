import numpy as np

a = 1.21
b = 0.371

y = np.tan(a + b)**2 - np.sqrt(3 * (a + 1.5) + a * b**5 - (b / np.log(a**2)))


print("Значение выражения:", y)
