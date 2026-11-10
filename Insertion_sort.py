import random

def insertion_sort(arr):
    # A parte à esquerda de i está sempre ordenada.
    # Começa em 1 porque um único elemento (posição 0) já é uma "parte ordenada".
    for i in range(1, len(arr)):
        key = arr[i]   # elemento que será inserido na parte ordenada
        j = i - 1      # último índice da parte ordenada

        # Desloca para a direita todos os elementos maiores que key,
        # abrindo espaço para ele. O "<" estrito para em iguais,
        # preservando a ordem original deles (estabilidade).
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Coloca key na posição livre que sobrou
        arr[j + 1] = key
    return arr

# ----- Programa principal: gera uma lista de teste e executa o algoritmo -----
lista = []

# Preenche a lista com 100000 números aleatórios
for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
# Mostra a lista original e a quantidade de elementos
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {len(lista)} elementos')

# Ordena a lista e mostra o resultado
resultado = insertion_sort(lista)
print(f'A lista ordenada é: {resultado}')

# ==================== INSERTION SORT ====================

# - Melhor caso: O(n)  (lista já ordenada)
# - Pior caso: O(n²)
# - Médio caso: O(n²)
# - Memória extra: O(1)
# - Estável (a comparação estrita key < arr[j] preserva a ordem dos iguais)

# Vantagens:
# - Fácil de implementar.
# - É estável.
# - Possui complexidade O(n) no melhor caso.
# - Não necessita de memória adicional significativa (in-place).
# - É eficiente para listas pequenas ou quase ordenadas.
# - É online: consegue ordenar elementos conforme eles chegam.

# Desvantagens:
# - Possui complexidade O(n²) no caso médio e no pior caso.
# - Realiza muitos deslocamentos quando a lista está desordenada.
# - Não é indicado para listas grandes e desordenadas.

# A ordenação por inserção é usada quando:
# - O array tem poucos elementos.
# - A lista está quase ordenada (restam apenas alguns elementos fora do lugar).
