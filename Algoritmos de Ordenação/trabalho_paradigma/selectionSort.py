import random
import time

def selection_sort(lista):
    n = len(lista)
    trocas = 0
    comparacoes = 0

    # Percorre todos os elementos da lista
    for i in range(n):
        # Encontra o índice do menor elemento não ordenado
        indice_minimo = i
        for j in range(i+1, n):
            comparacoes += 1
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Troca o elemento atual com o menor elemento não ordenado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        trocas += 1

    return trocas, comparacoes

minha_lista = [1,2,3,4,5]


# Guarda o tempo de início
inicio = time.time()

# Chama a função e obtém o resultado
trocas, comparacoes = selection_sort(minha_lista)

# Guarda o tempo de término
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Exibe os resultados
print("Lista ordenada:", minha_lista)
print("Quantidade de Trocas:", trocas)
print("Quantidade de Comparações:", comparacoes)
print("Tempo de Execução:", tempo_total, "segundos")
