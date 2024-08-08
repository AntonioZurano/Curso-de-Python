'''
Probar a declarar un array con la función array() de numpy con los siguientes valores:
'''

import numpy as np
# a) Un array de una dimensión con los valores 1, 2, 3, 4, 5
print("*** Array de una dimensión ***")
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(type(my_array))
# b) Un array de dos dimensiones con los valores 1, 2, 3, 4, 5, 6, 7, 8, 9
print("*** Array de dos dimensiones ***")
my_array_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array_2)
print(type(my_array_2))