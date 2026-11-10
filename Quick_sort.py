import random

def quick_sort(array):
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(array) <= 1:
        return array

    pivô = array[-1]  # Escolhe o último elemento como pivô

    # Particiona o restante da lista em relação ao pivô.
    # Iguais ao pivô vão para "menores" (ficam antes dele, na mesma ordem
    # em que apareciam), o que mantém esta versão estável.
    menores = [x for x in array[:-1] if x <= pivô]
    maiores = [x for x in array[:-1] if x > pivô]

    # Ordena cada lado recursivamente e junta: menores + pivô + maiores.
    # O pivô já está na posição final, pois tudo à esquerda é menor
    # ou igual e tudo à direita é maior.
    return quick_sort(menores) + [pivô] + quick_sort(maiores)

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
resultado = quick_sort(lista)
print(f'A lista ordenada é: {resultado}')

# ==================== QUICK SORT ====================

# - Melhor caso: O(n log n)
# - Médio caso: O(n log n)
# - Pior caso: O(n²)  (pivô sempre o menor/maior valor: lista já ordenada,
#                      invertida ou com muitos valores repetidos)
# - Memória extra: O(n) NESTA implementação (cria listas novas a cada chamada);
#                  a versão in-place usa apenas O(log n) de pilha
# - Estabilidade: ESTA implementação é estável (elementos iguais ao pivô vão
#                 para "menores", mantendo a ordem original). A versão
#                 tradicional in-place NÃO é estável.

# Vantagens:
# - Possui complexidade média O(n log n).
# - Geralmente apresenta excelente desempenho prático (boa localidade de cache).
# - A versão in-place usa pouca memória adicional.
# - É eficiente para grandes listas.

# Desvantagens:
# - Pode atingir O(n²) no pior caso.
# - A versão tradicional in-place não é estável.
# - A escolha inadequada do pivô (como o último elemento) pode prejudicar o desempenho.
# - No pior caso a recursão fica muito profunda e pode causar RecursionError em Python.
# - Exige atenção ao particionamento e às chamadas recursivas.

# O Quick Sort é usado quando:
# - Precisa-se de um algoritmo de uso geral com ótimo desempenho médio.
# - O pior caso pode ser evitado (pivô aleatório ou mediana de três).
