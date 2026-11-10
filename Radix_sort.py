import random

def radix_sort(arr):
    # Funciona apenas com inteiros NÃO negativos
    if not arr:
        return arr

    # O maior número define quantos dígitos (passadas) serão necessários
    max_num = max(arr)
    exp = 1  # Representa a posição atual do dígito (1, 10, 100, ...)

    # Uma passada por dígito, do menos significativo para o mais significativo.
    # Continua enquanto o maior número ainda tiver dígito nesta posição.
    while max_num // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # Para dígitos de 0-9

        # Contagem de ocorrências de cada dígito.
        # (num // exp) % 10 extrai o dígito da posição atual
        # (ex.: 472 com exp=10 -> 47 % 10 = 7).
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        # Converte o count[] para posições reais (soma acumulada),
        # igual ao Counting Sort
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Constrói a saída da lista (em reverso para manter a estabilidade).
        # A estabilidade é essencial: a ordem obtida nos dígitos anteriores
        # precisa ser preservada entre números com o mesmo dígito atual.
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copia a saída para a lista arr[]
        for i in range(n):
            arr[i] = output[i]

        exp *= 10  # passa para o próximo dígito (dezenas, centenas...)
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
resultado = radix_sort(lista)
print(f'A lista ordenada é: {resultado}')

# ==================== RADIX SORT ====================

# - Melhor caso: O(d · (n + b))
# - Pior caso: O(d · (n + b))
# - Médio caso: O(d · (n + b))
#   (n = número de elementos, d = número de dígitos do maior valor,
#    b = base usada; aqui b = 10)
# - Memória extra: O(n + b)
# - Estável

# Vantagens:
# - Pode apresentar desempenho linear quando d é pequeno e constante.
# - Não realiza comparações diretas entre os elementos.
# - É eficiente para grandes quantidades de números com tamanho limitado.
# - Pode ordenar números inteiros de maneira eficiente.

# Desvantagens:
# - Necessita de memória adicional.
# - Depende da quantidade de dígitos e da base utilizada.
# - Sua implementação é mais complexa.
# - Precisa de um algoritmo auxiliar estável (aqui, o Counting Sort).
# - Esta implementação não aceita números negativos.

# A ordenação radix é usada quando há muitos inteiros (ou strings de tamanho
# fixo) com um número limitado de dígitos, mesmo que o intervalo de valores
# seja grande (onde o Counting Sort puro gastaria memória demais).
