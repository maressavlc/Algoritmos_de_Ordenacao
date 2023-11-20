import random
import time

def merge_sort(lista):
    trocas = 0
    comparacoes = 0

    if len(lista) > 1:
        meio = len(lista) // 2
        lista_esquerda = lista[:meio]
        lista_direita = lista[meio:]

        trocas_esquerda, comparacoes_esquerda = merge_sort(lista_esquerda)
        trocas_direita, comparacoes_direita = merge_sort(lista_direita)

        trocas += trocas_esquerda + trocas_direita
        comparacoes += comparacoes_esquerda + comparacoes_direita

        i = j = k = 0

        # Combina as listas ordenadas
        while i < len(lista_esquerda) and j < len(lista_direita):
            comparacoes += 1
            if lista_esquerda[i] < lista_direita[j]:
                lista[k] = lista_esquerda[i]
                i += 1
            else:
                lista[k] = lista_direita[j]
                j += 1
            trocas += 1
            k += 1

        # Adiciona os elementos restantes, se houver
        while i < len(lista_esquerda):
            lista[k] = lista_esquerda[i]
            i += 1
            k += 1
            trocas += 1

        while j < len(lista_direita):
            lista[k] = lista_direita[j]
            j += 1
            k += 1
            trocas += 1

    return trocas, comparacoes

minha_lista = [1,2,3,4,5]

# Guarda o tempo de início
inicio = time.time()

# Chama a função e obtém o resultado
trocas, comparacoes = merge_sort(minha_lista)

# Guarda o tempo de término
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Exibe os resultados
print("Lista ordenada:", minha_lista)
print("Quantidade de Trocas:", trocas)
print("Quantidade de Comparações:", comparacoes)
print("Tempo de Execução:", tempo_total, "segundos")
