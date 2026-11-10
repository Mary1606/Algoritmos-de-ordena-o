import random

def selection_sort(arr):
    if not arr:
        return arr

    # A parte à esquerda de i está sempre ordenada e definitiva.
    # A cada passada, escolhe o menor elemento do restante e o coloca na posição i.
    for i in range(len(arr)):
        min_i = i  # índice do menor elemento encontrado até agora

        # Varre o restante da lista procurando um valor menor
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j

        # Uma única troca por passada (no máximo n-1 no total).
        # Como a troca é à distância, ela pode passar um elemento por cima
        # de um igual, e por isso o algoritmo não é estável.
        arr[i], arr[min_i] = arr[min_i], arr[i]
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
resultado = selection_sort(lista)
print(f'A lista ordenada é: {resultado}')

# ==================== SELECTION SORT ====================

# - Melhor caso: O(n²)
# - Pior caso: O(n²)
# - Médio caso: O(n²)
# - Memória extra: O(1)
# - Não é estável (a troca à distância pode inverter elementos iguais)

# Vantagens:
# - Fácil de implementar.
# - Realiza poucas trocas, no máximo n-1.
# - Não necessita de memória adicional significativa (in-place).
# - Possui desempenho previsível, independentemente da ordem inicial.

# Desvantagens:
# - Possui complexidade O(n²) em todos os casos.
# - Não é estável em sua implementação tradicional.
# - Não aproveita listas parcialmente ordenadas.
# - Não é indicado para grandes quantidades de elementos.

# A ordenação por seleção é usada quando:
# - Uma lista pequena deve ser organizada.
# - O custo de escrita/troca é alto (ela faz no máximo n-1 trocas).
# - Memória extra é um problema (é in-place).
