import random
import time
import sys

# Aumenta o limite de recursão (ajuste conforme necessário)
sys.setrecursionlimit(1500)

def quick_sort_iterativo(lista):
    trocas = 0
    comparacoes = 0

    # Pilha para armazenar tuplas (início, fim) a serem processadas
    pilha = [(0, len(lista) - 1)]

    while pilha:
        inicio, fim = pilha.pop()

        if fim - inicio <= 0:
            continue

        pivô = lista[inicio]
        i, j = inicio + 1, fim

        while i <= j:
            comparacoes += 1
            if lista[i] <= pivô:
                i += 1
            elif lista[j] > pivô:
                j -= 1
            else:
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
                i += 1
                j -= 1

        lista[inicio], lista[j] = lista[j], lista[inicio]
        trocas += 1

        # Empilha sub-listas não ordenadas
        if j - inicio > fim - j:
            pilha.append((inicio, j - 1))
            pilha.append((j + 1, fim))
        else:
            pilha.append((j + 1, fim))
            pilha.append((inicio, j - 1))

    return lista, trocas, comparacoes

minha_lista = [1,2,3,4,5]

# Guarda o tempo de início
inicio = time.time()

# Chama a função e obtém o resultado
lista_ordenada, trocas, comparacoes = quick_sort_iterativo(minha_lista.copy())

# Guarda o tempo de término
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Exibe os resultados
print("Lista ordenada:", lista_ordenada)
print("Quantidade de Trocas:", trocas)
print("Quantidade de Comparações:", comparacoes)
print("Tempo de Execução:", tempo_total, "segundos")
