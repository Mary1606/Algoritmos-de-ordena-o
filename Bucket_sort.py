import random

def bucketSort(lista):
    n = len(lista)

    # Listas com 0 ou 1 elemento já estão ordenadas
    if n < 2:
        return lista

    # O menor e o maior valor definem a faixa que será dividida em baldes
    menor, maior = min(lista), max(lista)
    if menor == maior:  # todos iguais: nada a ordenar (e evita divisão por zero)
        return lista

    # Passo 1: cria n baldes (listas) vazios
    bucket = [[] for _ in range(n)]

    # Passo 2: distribui cada elemento no balde correspondente.
    # A fórmula normaliza o valor para [0, 1) e multiplica por n,
    # então valores pequenos vão para os primeiros baldes e valores
    # grandes para os últimos (a ordem entre os baldes já fica correta).
    for j in lista:
        index_b = int(n * (j - menor) / (maior - menor))
        if index_b == n:  # o valor máximo daria índice n, fora dos baldes
            index_b = n - 1
        bucket[index_b].append(j)

    # Passo 3: ordena cada balde individualmente.
    # Como cada balde tem poucos elementos, essa etapa é rápida.
    # sorted() usa Timsort, que é estável.
    for i in range(n):
        bucket[i] = sorted(bucket[i])

    # Passo 4: junta os baldes, em ordem, de volta na lista original.
    # k é a posição de escrita na lista final.
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            lista[k] = bucket[i][j]
            k += 1
    return lista

# ----- Programa principal: gera uma lista de teste e executa o algoritmo -----
lista = []

# Preenche a lista com 100000 números aleatórios
for i in range(100000):
    d100000 = random.uniform(0, 10000)
    lista.append(d100000)
# Mostra a lista original e a quantidade de elementos
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {len(lista)} elementos')

# Ordena a lista e mostra o resultado
resultado = bucketSort(lista)
print(f'\nA lista ordenada é: {resultado}')

# ==================== BUCKET SORT ====================

# Complexidade de tempo (n = elementos, k = baldes):
# - Melhor caso: O(n + k)
# - Médio caso: O(n + k), ou O(n) quando k ~ n e a distribuição é uniforme
# - Pior caso: depende do algoritmo usado dentro dos baldes:
#     * O(n²) com Insertion Sort e todos os elementos em um único balde
#     * O(n log n) com sorted() (Timsort), como neste código
# - Memória extra: O(n + k)
# - Estável, se o algoritmo usado nos baldes for estável (sorted() é)

# Vantagens:
# - Pode apresentar complexidade próxima de O(n) com distribuição uniforme.
# - Funciona bem com números de ponto flutuante.
# - Permite ordenar os baldes separadamente (inclusive em paralelo).
# - Pode utilizar outros algoritmos para ordenar os baldes.

# Desvantagens:
# - Depende da distribuição dos dados.
# - Necessita de memória adicional para armazenar os baldes.
# - Se muitos elementos caírem em um único balde, o desempenho degrada.
# - A quantidade de baldes influencia diretamente o desempenho.

# A ordenação por balde é usada quando a entrada é distribuída
# uniformemente em uma faixa e existem valores de ponto flutuante.
