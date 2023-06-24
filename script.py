from selectionSort import *
from mergeSort import *
import numpy as np
import time
import matplotlib
np.set_printoptions(threshold=np.inf, suppress=True)

ARR_SIZE = 50000

mergeData = {
                '50-ascending': np.array([]),'50-descending': np.array([]),'50-random': np.array([]),'500-ascending': np.array([]),'500-descending': np.array([]),'500-random': np.array([]),'5000-ascending': np.array([]),'5000-descending': np.array([]),'5000-random': np.array([]),'50000-ascending': np.array([]),'50000-descending': np.array([]),'50000-random': np.array([])
}

selectionData = {
                '50-ascending': np.array([]),'50-descending': np.array([]),'50-random': np.array([]),'500-ascending': np.array([]),'500-descending': np.array([]),'500-random': np.array([]),'5000-ascending': np.array([]),'5000-descending': np.array([]),'5000-random': np.array([]),'50000-ascending': np.array([]),'50000-descending': np.array([]),'50000-random': np.array([])}


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
       np.append(dados_aleatorios['50-merge'], [elapsed_time])
    #    dados_aleatorios['50-merge'].append(elapsed_time)
   print(f'--- {elapsed_time} seconds to order a randomized 50-element array using Merge-Sort. ---')
   
   start_time_selectionSort = time.time()
   selectionSortedList = selectionSort(random_array)
   elapsed_time_selectionSort = time.time() - start_time_selectionSort
   
   if (elapsed_time_selectionSort):
      np.append(dados_aleatorios['50-selection'], [elapsed_time_selectionSort])
    #   dados_aleatorios['50-selection'].append(elapsed_time_selectionSort)
   print(f'--- {elapsed_time_selectionSort} seconds to order a randomized 50-element array using Selection-Sort. ---')

# print(dados_aleatorios['50-merge'])
# dados_aleatorios = {
#                 '50-merge': np.arra#                 '500-merge': np.arra#                 '5000-merge': np.arra#                 '50000-merge': np.arra#                 '50-selection': np.arra#                 '500-selection': np.arra#                 '5000-selection': np.arra#                 '50000-selection': np.array([])
# }

# decrescente = {
#                 '50-merge': np.arra#                 '500-merge': np.arra#                 '5000-merge': np.arra#                 '50000-merge': np.arra#                 '50-selection': np.arra#                 '500-selection': np.arra#                 '5000-selection': np.arra#                 '50000-selection': np.array([])
# }

# crescente = {
#                 '50-merge': np.arra#                 '500-merge': np.arra#                 '5000-merge': np.arra#                 '50000-merge': np.arra#                 '50-selection': np.arra#                 '500-selection': np.arra#                 '5000-selection': np.arra#                 '50000-selection': np.array([])
# }