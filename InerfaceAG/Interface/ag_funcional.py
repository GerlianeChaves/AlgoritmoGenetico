# -*- coding: utf-8 -*-
"""AG_funcional.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HWzH99KLSJ7FaNZO3MQuQ-tBJQIjFOQK
"""

#população combinada MESCLADA
import random
from itertools import permutations

# Função para calcular o custo total de uma rota
def calc_custo(caminho, distancias):
    custo = sum(distancias[caminho[i] - 1][caminho[i + 1] - 1] for i in range(len(caminho) - 1))
    custo += distancias[caminho[-1] - 1][caminho[0] - 1]
    return custo

# Função para gerar a população inicial com indivíduos únicos
def gerar_populacao_inicial(ncidades):
    cidades = list(range(1, ncidades + 1))
    populacao = set(permutations(cidades))  # Usando set para garantir unicidade
    return [list(individuo) for individuo in populacao]

# Função para gerar novos indivíduos com mutação e garantir unicidade
def mutacao(individuo, populacao_atual):
    while True:
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]

        # Verificar se o indivíduo já está na população atual
        if individuo not in populacao_atual:
            return individuo

# Função para combinar a população inicial e a população atual
def mesclar_populacoes(populacao_inicial, populacao_atual, distancias):
    # Seleciona 50% dos melhores indivíduos da população inicial
    melhores_inicial = sorted(populacao_inicial, key=lambda ind: calc_custo(ind, distancias))[:len(populacao_inicial) // 2]

    # Seleciona 50% dos melhores indivíduos da população atual
    melhores_atual = sorted(populacao_atual, key=lambda ind: calc_custo(ind, distancias))[:len(populacao_atual) // 2]

    # Mescla os melhores de ambas as populações
    return melhores_inicial + melhores_atual

# Algoritmo Genético para o Caixeiro Viajante
def ag_caixeiroviajante(distancias, geracoes=10):
    ncidades = len(distancias)
    populacao_inicial = gerar_populacao_inicial(ncidades)

    print("\nPopulação Inicial (em ordem crescente de custo):")
    populacao_inicial = sorted(populacao_inicial, key=lambda ind: calc_custo(ind, distancias))
    for ind in populacao_inicial:
        print(f"Caminho: {ind}, Custo: {calc_custo(ind, distancias)}")

    populacao_atual = []
    for geracao in range(geracoes):
        print(f"\nGeração {geracao + 1}:")

        # Aplicar mutação para gerar a população atual
        populacao_atual = []
        for individuo in populacao_inicial:
            novo_individuo = mutacao(individuo[:], populacao_atual)
            populacao_atual.append(novo_individuo)

        print("\nPopulação Atual (após mutação):")
        populacao_atual = sorted(populacao_atual, key=lambda ind: calc_custo(ind, distancias))
        for ind in populacao_atual:
            print(f"Caminho: {ind}, Custo: {calc_custo(ind, distancias)}")

        # Mesclar a população inicial e a população atual
        populacao_combinada = mesclar_populacoes(populacao_inicial, populacao_atual, distancias)

        print("\nPopulação Combinada (50% Inicial + 50% Atual):")
        populacao_combinada = sorted(populacao_combinada, key=lambda ind: calc_custo(ind, distancias))
        for ind in populacao_combinada:
            print(f"Caminho: {ind}, Custo: {calc_custo(ind, distancias)}")

        # A próxima geração será os melhores selecionados da população combinada
        populacao_inicial = populacao_combinada

    melhor = min(populacao_inicial, key=lambda ind: calc_custo(ind, distancias))
    return melhor, calc_custo(melhor, distancias)

# Entrada de dados
if __name__ == '__main__':
    ncidades = int(input('Quantas cidades serão visitadas? '))
    distancias = [[0] * ncidades for _ in range(ncidades)]
    for i in range(ncidades):
        for j in range(i + 1, ncidades):
            km = float(input(f'Informe a distancia entre a cidade {i + 1} e {j + 1}: '))
            distancias[i][j] = distancias[j][i] = km

    print('\nMatriz de distâncias:')
    for linha in distancias:
        print(linha)

    melhor_caminho, custo = ag_caixeiroviajante(distancias)
    print(f'\nMelhor Caminho Final: {melhor_caminho}')
    print(f'Custo Total: {custo}')

