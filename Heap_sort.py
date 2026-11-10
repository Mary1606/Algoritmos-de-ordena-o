import random

def heapify(arr, n, i):
    # Garante que a subárvore com raiz em i seja um max-heap
    # (cada pai é maior ou igual aos seus filhos).
    # n é o tamanho atual do heap; elementos além de n já estão ordenados.
    maior = i
    esquerda = 2 * i + 1   # índice do filho esquerdo na representação em vetor
    direita = 2 * i + 2    # índice do filho direito

    # Verifica se o filho esquerdo existe e é maior que o maior atual
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    # Verifica se o filho direito existe e é maior que o maior atual
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    # Se o maior não é a raiz, troca e continua descendo,
    # pois a troca pode ter quebrado o heap na subárvore de baixo
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)


def heap_sort(arr):
    n = len(arr)

    # Fase 1: construir o max-heap
    # (começa no último nó que tem filhos e vai até a raiz).
    # Os nós folha já são heaps válidos, então não precisam de heapify.
    # Ao fim desta fase, arr[0] é o maior elemento da lista.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Fase 2: extrair o maior elemento um a um
    for fim in range(n - 1, 0, -1):
        arr[0], arr[fim] = arr[fim], arr[0]  # move o maior para o final
        heapify(arr, fim, 0)                 # reconstrói o heap reduzido
        # (o tamanho do heap agora é "fim": a posição fim já está definitiva)

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
resultado = heap_sort(lista)
print(f'Lista ordenada: {resultado}')

# ==================== HEAP SORT ====================

# - Melhor caso: O(n log n)
# - Pior caso: O(n log n)
# - Médio caso: O(n log n)
# - Memória extra: O(log n) neste código (pilha de recursão do heapify);
#                  O(1) com um heapify iterativo
# - Não é estável

# Vantagens:
# - Possui complexidade O(n log n) em todos os casos.
# - Ordena in-place, sem necessidade de memória adicional significativa.
# - Apresenta desempenho consistente em listas grandes.
# - Não depende da organização inicial dos elementos.

# Desvantagens:
# - Não é estável.
# - Sua implementação é mais complexa.
# - Na prática costuma ser mais lento que o Quick Sort.
# - O padrão de acesso à memória (saltos entre pai e filhos) tem pouca
#   localidade de cache, o que prejudica o desempenho.

# Sistemas embarcados e sistemas preocupados com segurança, como o kernel do
# Linux, usam Heap Sort por causa do limite superior garantido de tempo
# O(n log n) e do uso mínimo de armazenamento auxiliar. Fora desses cenários,
# tem menos aplicações práticas que Quick Sort e Merge Sort.
