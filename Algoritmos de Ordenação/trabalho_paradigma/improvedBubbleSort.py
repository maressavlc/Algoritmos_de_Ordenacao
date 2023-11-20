import random
import time

def improved_bubble_sort(lista):
    n = len(lista)
    trocas = 0
    comparacoes = 0

    # Flag para indicar se ocorreu alguma troca durante a passagem
    troca_ocorreu = True

    # Percorre todos os elementos da lista enquanto houver trocas
    for i in range(n):
        # Se nenhuma troca ocorreu durante a passagem anterior, a lista está ordenada
        if not troca_ocorreu:
            break

        troca_ocorreu = False

        # Últimos i elementos já estão ordenados, então não é necessário considerá-los
        for j in range(0, n-i-1):
            # Compara elementos adjacentes
            comparacoes += 1
            if lista[j] > lista[j+1]:
                # Troca se estiverem fora de ordem
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocas += 1
                troca_ocorreu = True

    return trocas, comparacoes

minha_lista = [1,2,3,4,5]
# Guarda o tempo de início
inicio = time.time()

# Chama a função e obtém o resultado
trocas, comparacoes = improved_bubble_sort(minha_lista)

# Guarda o tempo de término
fim = time.time()

# Calcula o tempo total
tempo_total = fim - inicio

# Exibe os resultados
print("Lista ordenada:", minha_lista)
print("Quantidade de Trocas:", trocas)
print("Quantidade de Comparações:", comparacoes)
print("Tempo de Execução:", tempo_total, "segundos")
