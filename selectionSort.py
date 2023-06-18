# -*- coding: utf-8 -*-

def selectionSort(array):
    n = len(array)
    for i in range(n):
        minimum = i

        for j in range(i+1, n):
            if array[j] < array[minimum]:
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]

    return array

"""

O código acima mostra como escrever Selection Sort em Python. Agora vamos entender isso em detalhes.

O primeiro for loop percorre todo o array. Ele inicialmente define o minimumcomo o índice do primeiro elemento na matriz não classificada.

O loop interno for percorre a parte restante da matriz para encontrar a posição do valor mínimo nessa parte. Depois de concluído, ele troca o valor mínimo na parte não classificada pelo primeiro valor da parte não classificada.

Ele repete o procedimento passando para o próximo valor da lista e considerando-o como o novo mínimo.

"""