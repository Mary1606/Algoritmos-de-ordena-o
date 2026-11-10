import random

def counting_sort(arr):
    # Lista vazia: max() e min() dariam erro, então retorna direto
    if not arr:
        return arr

    # Descobre o menor e o maior valor para saber a faixa de valores
    max_val = max(arr)
    min_val = min(arr)

    # Tamanho da faixa (k): quantos valores diferentes são possíveis
    range_of_elements = max_val - min_val + 1

    # count[i] vai guardar quantas vezes o valor (i + min_val) aparece.
    # Subtrair min_val faz o menor valor cair no índice 0 e permite
    # trabalhar com a lista mesmo que ela não comece em zero.
    count = [0] * range_of_elements
    output = [0] * len(arr)  # lista final ordenada

    # Passo 1: conta a ocorrência de cada valor
    for num in arr:
        count[num - min_val] += 1

    # Passo 2: soma acumulada. Depois dela, count[i] indica quantos
    # elementos são menores ou iguais ao valor i, ou seja, a posição
    # (contando de 1) onde a última ocorrência de i deve ficar.
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Passo 3: monta a saída. Percorre a lista original de trás para frente
    # para que, entre valores iguais, o último da entrada fique por último
    # na saída: é isso que torna o algoritmo estável.
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num  # coloca na posição final
        count[num - min_val] -= 1               # a próxima igual vai uma posição antes

    return output

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
resultado = counting_sort(lista)
print(f'Lista ordenada: {resultado}')

# ==================== COUNTING SORT ====================

# - Melhor caso: O(n + k)
# - Pior caso: O(n + k)
# - Médio caso: O(n + k)
#   (n = número de elementos, k = tamanho do intervalo max - min + 1)
# - Memória extra: O(n + k)  (array de contagem + array de saída)
# - Estável (neste código, por causa do laço em reverso)

# Vantagens:
# - Possui complexidade linear O(n + k).
# - Não realiza comparações entre os elementos.
# - É muito eficiente quando o intervalo de valores é pequeno.
# - É estável quando implementado com contagens acumuladas, como aqui.

# Desvantagens:
# - Necessita de memória adicional O(n + k).
# - Pode consumir muita memória quando o intervalo é grande.
# - Só funciona com inteiros (ou dados mapeáveis para índices inteiros).
# - Não é vantajoso quando k é muito maior que n.

# A counting sort é usada quando:
# - Os valores são inteiros em um intervalo pequeno, com muitas repetições.
# - A complexidade linear é necessária.
