import random

def merge(left, right, compare):
    # Junta duas listas JÁ ORDENADAS em uma única lista ordenada
    result = []
    i, j = 0, 0  # i percorre left, j percorre right

    # Enquanto as duas têm elementos, pega o menor entre os da frente
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Uma das listas acabou; o que sobrou da outra já está ordenado
    # e é maior que tudo que foi copiado, então basta anexar.
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(arr, compare=lambda x, y: x <= y):
    # A função compare define a ordem: por padrão, ordem crescente.
    # Use "<=" (e não "<") para que, em caso de empate, o elemento da esquerda
    # venha primeiro. É isso que garante a estabilidade.

    # Caso base: lista com 0 ou 1 elemento já está ordenada.
    # Retorna uma cópia para nunca alterar a lista original.
    if len(arr) < 2:
        return arr[:]

    # Dividir: separa a lista ao meio
    middle = len(arr) // 2

    # Conquistar: ordena cada metade recursivamente
    left = merge_sort(arr[:middle], compare)
    right = merge_sort(arr[middle:], compare)

    # Combinar: junta as duas metades ordenadas
    return merge(left, right, compare)

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
resultado = merge_sort(lista)
print(f'A lista ordenada é: {resultado}')

# ==================== MERGE SORT ====================

# - Melhor caso: O(n log n)
# - Pior caso: O(n log n)
# - Médio caso: O(n log n)
# - Memória extra: O(n)
# - Estável (desde que compare use <=, como no padrão acima)

# Vantagens:
# - Possui complexidade O(n log n) em todos os casos.
# - Apresenta bom desempenho em listas grandes.
# - É estável.
# - Mantém desempenho previsível.
# - Funciona bem com dados em disco/streams (acesso sequencial).

# Desvantagens:
# - Necessita de memória adicional O(n).
# - Sua implementação é mais complexa.
# - Consome mais memória que algoritmos in-place.
