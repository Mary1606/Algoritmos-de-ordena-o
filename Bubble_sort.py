import random

def bubbleSort(arr):
    n = len(arr)

    # Cada passada completa "empurra" o maior elemento restante para o final,
    # como uma bolha que sobe. Por isso são necessárias até n passadas.
    for i in range(n):
        trocou = False  # Flag: guarda se houve alguma troca nesta passada

        # Compara pares vizinhos. Os últimos i elementos já estão no lugar
        # certo (foram empurrados nas passadas anteriores), então não
        # precisam mais ser comparados: por isso o limite n - i - 1.
        for j in range(0, n - i - 1):
            # Se o par está fora de ordem, troca as posições.
            # O ">" estrito não troca iguais, o que mantém a estabilidade.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True

        # Se a passada inteira não trocou nada, a lista já está ordenada
        # e podemos parar antes (é isso que dá o melhor caso O(n)).
        if not trocou:
            break
    return arr

# ----- Programa principal: gera uma lista de teste e executa o algoritmo -----
lista = []

# Preenche a lista com 100000 números aleatórios
for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
# Mostra a lista original e a quantidade de elementos
print(f'A lista é: {lista}')
print(f'
Número de elementos da lista: {len(lista)} elementos')

# Ordena a lista e mostra o resultado
resultado = bubbleSort(lista)
print(f'Lista ordenada: {resultado}')

# ==================== BUBBLE SORT ====================

# - Melhor caso: O(n)  (somente com a flag "trocou", como implementado acima;
#                       sem ela o melhor caso também seria O(n²))
# - Pior caso: O(n²)
# - Médio caso: O(n²)
# - Memória extra: O(1)
# - Estável

# Vantagens:
# - Fácil de implementar e compreender.
# - Não necessita de memória adicional significativa (in-place).
# - É estável, mantendo a ordem relativa de elementos iguais.
# - Com a flag de parada antecipada, é eficiente para listas quase ordenadas.

# Desvantagens:
# - Possui complexidade O(n²) no caso médio e no pior caso.
# - Realiza muitas comparações e trocas.
# - É muito lento para listas grandes.
