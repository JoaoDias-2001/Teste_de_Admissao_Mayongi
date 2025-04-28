# PROVA DE ADMISSÃO PARA ESTÁGIO - MAYONGI ANGOLA
# Resolução em Python

# Questão 1:
# A senha do cofre é um número de 4 dígitos.
# - Todos os dígitos são diferentes.
# - A soma é 10.
# - O último dígito é 0.

from itertools import permutations

def contar_senhas_possiveis():
    digitos = [1,2,3,4,5,6,7,8,9]
    combinacoes = []
    for p in permutations(digitos, 3):
        if sum(p) == 10:
            combinacoes.append(p)
    total_senhas = len(combinacoes) * 1  # Cada combinação gera 1 senha adicionando o 0 no final
    return total_senhas

# Resultado:
qtd_senhas = contar_senhas_possiveis()
print(f"Questão 1: Existem {qtd_senhas} senhas possíveis.")


# Questão 2:
# Encontrar o próximo número da sequência: 2, 6, 12, 20, 30, 42, ?

def proximo_na_sequencia(seq):
    diffs = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    proxima_dif = diffs[-1] + 2
    return seq[-1] + proxima_dif

# Resultado:
sequencia = [2, 6, 12, 20, 30, 42]
proximo = proximo_na_sequencia(sequencia)
print(f"Questão 2: O próximo número da sequência é {proximo}.")


# Questão 3:
# Somar os termos pares da sequência de Fibonacci até N

def soma_fibonacci_pares(N):
    a, b = 0, 2  # Termos pares iniciais: F(0)=0 e F(3)=2
    soma = 0
    while b <= N:
        soma += b
        a, b = b, 4*b + a  # Geração eficiente apenas de termos pares
    return soma

# Exemplo de uso:
N = 10**18
soma_pares = soma_fibonacci_pares(N)
print(f"Questão 3: A soma dos termos pares de Fibonacci até {N} é {soma_pares}.")


