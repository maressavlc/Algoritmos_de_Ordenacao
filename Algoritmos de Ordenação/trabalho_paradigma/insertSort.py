import random
import time


def insertion_sort(lista):
    n = len(lista)
    trocas = 0
    comparacoes = 0

    # Percorre todos os elementos da lista
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        comparacoes += 1

        # Move os elementos maiores que a chave para a direita
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
            trocas += 1
            comparacoes += 1

        lista[j + 1] = chave

    return trocas, comparacoes

minha_lista = [1,2,3,4,5]

# Guarda o tempo de início
inicio = time.time()

# Chama a função e obtém o resultado
trocas, comparacoes = insertion_sort(minha_lista)

# Guarda o tempo de término
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Exibe os resultados
#print("Lista ordenada:", minha_lista)
print("Quantidade de Trocas:", trocas)
print("Quantidade de Comparações:", comparacoes)
print("Tempo de Execução:", tempo_total, "segundos")
