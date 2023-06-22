from selectionSort import *
from mergeSort import *
import numpy as np
import time
import matplotlib
np.set_printoptions(threshold=np.inf, suppress=True)

ARR_SIZE = 50000

dados_aleatorios = {
    '50-merge': [],
    '500-merge': [],
    '5000-merge': [],
    '50000-merge': [],
    '50-selection': [],
    '500-selection': [],
    '5000-selection': [],
    '50000-selection': [],
}

decrescente = {
    '50-merge': [],
    '500-merge': [],
    '5000-merge': [],
    '50000-merge': [],
    '50-selection': [],
    '500-selection': [],
    '5000-selection': [],
    '50000-selection': [],
}

crescente = {
    '50-merge': [],
    '500-merge': [],
    '5000-merge': [],
    '50000-merge': [],
    '50-selection': [],
    '500-selection': [],
    '5000-selection': [],
    '50000-selection': [],
}

# print(data)

# Gerando um array em ordem crescente
ordered_array = np.array([])
for i in range(ARR_SIZE):
    ordered_array = np.append(ordered_array, [i])

# Gerando um array em ordem decrescente
reordered_array = np.array([])
for i in range(ARR_SIZE, -1, -1):
    reordered_array = np.append(reordered_array, [i])

# Driver code

### MERGE-SORT ###

# 50 ELEMENTOS
for i in range(100):
   random_array = np.random.randint(1, 100000001, size=50)
   
   start_time = time.time()
   mergeSortedList = mergeSort(random_array)
   elapsed_time = time.time() - start_time
   
   if elapsed_time:
       dados_aleatorios['50-merge'].append(elapsed_time)
   print(f'--- {elapsed_time} seconds to order a randomized 50-element array using Merge-Sort. ---')
   
   start_time_selectionSort = time.time()
   selectionSortedList = selectionSort(random_array)
   elapsed_time_selectionSort = time.time() - start_time_selectionSort
   
   if (elapsed_time_selectionSort):
      dados_aleatorios['50-merge'].append(elapsed_time_selectionSort)
   print(f'--- {elapsed_time_selectionSort} seconds to order a randomized 50-element array using Selection-Sort. ---')

# print(dados_aleatorios['50-merge'])

# 500 ELEMENTOS

for i in range(10):
   random_array = np.random.randint(1, 100000001, size=500)
   
   start_time = time.time()
   mergeSortedList = mergeSort(random_array)
   elapsed_time = time.time() - start_time
   if elapsed_time:
       dados_aleatorios['500-merge'].append(elapsed_time)
   print(f'--- {elapsed_time} seconds to order a randomized 500-element array using Merge-Sort. ---')
   
   start_time_selectionSort = time.time()
   selectionSortedList = selectionSort(random_array)
   elapsed_time_selectionSort = time.time() - start_time_selectionSort
   if (elapsed_time_selectionSort):
      dados_aleatorios['50-merge'].append(elapsed_time_selectionSort)
   print(f'--- {elapsed_time_selectionSort} seconds to order a randomized 500-element array using Selection-Sort. ---')
   

# print(dados_aleatorios['500-merge'])

# 5000 ELEMENTOS

for i in range(10):
   random_array = np.random.randint(1, 100000001, size=5000)
   start_time = time.time()
   mergeSortedList = mergeSort(random_array)
   elapsed_time = time.time() - start_time
   if elapsed_time:
       dados_aleatorios['5000-merge'].append(elapsed_time)
   print(f'--- {elapsed_time} seconds to order a randomized 5000-element array using Merge-Sort. ---')

   start_time_selectionSort = time.time()
   selectionSortedList = selectionSort(random_array)
   elapsed_time_selectionSort = time.time() - start_time_selectionSort
   if (elapsed_time_selectionSort):
      dados_aleatorios['50-merge'].append(elapsed_time_selectionSort)
   print(f'--- {elapsed_time_selectionSort} seconds to order a randomized 5000-element array using Selection-Sort. ---')

# print(dados_aleatorios['5000-merge'])

# 50000 ELEMENTOS

for i in range(10):
   random_array = np.random.randint(1, 100000001, size=50000)
   
   start_time = time.time()
   mergeSortedList = mergeSort(random_array)
   elapsed_time = time.time() - start_time
   
   if elapsed_time:
       dados_aleatorios['50000-merge'].append(elapsed_time)
   print(f'--- {elapsed_time} seconds to order a randomized 50000-element array using Merge-Sort. ---')

   start_time_selectionSort = time.time()
   selectionSortedList = selectionSort(random_array)
   elapsed_time_selectionSort = time.time() - start_time_selectionSort
   
   if (elapsed_time_selectionSort):
      dados_aleatorios['50-merge'].append(elapsed_time_selectionSort)
   print(f'--- {elapsed_time_selectionSort} seconds to order a randomized 50000-element array using Selection-Sort. ---')

print ("--------------------------MERGE--------------------------")
print(dados_aleatorios['50000-merge'])
print ("--------------------------SELECTION--------------------------")
print(dados_aleatorios['50000-selection'])

"""

import time

start_time = time.time()
***ALGORITMO***
print('Tempo levado para executar: ' + elapsed_time)



"""



# print(reordered_array)
