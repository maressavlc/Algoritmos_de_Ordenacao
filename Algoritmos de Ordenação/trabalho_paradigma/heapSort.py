import random
import time

def heapify(lista, n, i, trocas, comparacoes):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Encontrar o maior elemento entre o pai, a esquerda e a direita
    comparacoes[0] += 1  # Conta a comparação
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    comparacoes[0] += 1  # Conta a comparação
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    # Se o maior não é o pai, troca e chama a heapify recursivamente
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        trocas.append((lista[i], lista[maior]))
        heapify(lista, n, maior, trocas, comparacoes)

def heap_sort(lista):
    n = len(lista)
    trocas = []
    comparacoes = [0]  # Lista mutável para armazenar o número de comparações

    # Construir uma max heap (rearranjar a lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i, trocas, comparacoes)

    # Extrair elementos um por um da heap
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # Troca o maior elemento (raiz) com o último
        trocas.append((lista[i], lista[0]))
        heapify(lista, i, 0, trocas, comparacoes)  # Chama heapify no heap reduzido

    return trocas, comparacoes[0]

minha_lista = [10,9,8,7,6,5,4,3,2,1]

print("minha lista: ",minha_lista)
# Guarda o tempo de início
inicio = time.time()

# Chama a função Heap Sort e obtém o resultado
trocas_heap_sort, comparacoes_heap_sort = heap_sort(minha_lista)

# Guarda o tempo de término
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Exibe os resultados

print("Lista ordenada:", minha_lista)


# Exibe a quantidade total de trocas e comparações
print("Quantidade total de trocas:", len(trocas_heap_sort))
print("Quantidade total de comparações:", comparacoes_heap_sort)

print("Tempo de Execução:", tempo_total, "segundos")
