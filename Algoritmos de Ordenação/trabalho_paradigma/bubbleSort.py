import random
import time

minha_lista = [1,2,3,4,5]

def bubble_sort(lista):
    n = len(lista)
    trocas = 0
    comparacoes = 0

    # Percorre todos os elementos da lista
    for i in range(n):
        # Últimos i elementos já estão ordenados, então não é necessário considerá-los
        for j in range(0, n-i-1):
            # Compara elementos adjacentes
            comparacoes += 1
            if lista[j] > lista[j+1]:
                # Troca se estiverem fora de ordem
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocas += 1

    return trocas, comparacoes

# Guarda o tempo de início
inicio = time.time()

# Chama a função e obtém o resultado
trocas, comparacoes = bubble_sort(minha_lista)

# Guarda o tempo de término
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Exibe os resultados
print("Lista ordenada:", minha_lista)
print("Quantidade de Trocas:", trocas)
print("Quantidade de Comparações:", comparacoes)
print("Tempo de Execução:", tempo_total, "segundos")
