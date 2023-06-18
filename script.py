from selectionSort import *
from mergeSort import *
import numpy as np
import time

ARR_SIZE = 50000
# Driver code
# start_time = time.time()
# random_array = np.random.randint(1, 100000001, size=ARR_SIZE)
# sortedList = mergeSort(random_array)
# print(sortedList)

# print('--- ' + str(time.time() - start_time) + ' seconds to order a randomized ' + str(ARR_SIZE) + '-element array. ---')



"""

import time

start_time = time.time()
***ALGORITMO***
print('Tempo levado para executar: ' + str(time.time() - start_time))



"""
ordered_array = np.array([])
for i in range(ARR_SIZE):
   ordered_array = np.append(ordered_array, [i])

np.set_printoptions(threshold=np.inf, suppress=True)

print(ordered_array)
