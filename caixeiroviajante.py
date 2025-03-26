import math

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Função para calcular o custo de uma solução (soma das distâncias)
def calculate_cost(route, coordinates):
    n = len(route)
    cost = 0
    for i in range(n - 1):
        cost += euclidean_distance(coordinates[route[i] - 1], coordinates[route[i + 1] - 1])
    cost += euclidean_distance(coordinates[route[-1] - 1], coordinates[route[0] - 1])  # Retorno à cidade inicial
    return cost

# Implementação do algoritmo de pesquisa local
def local_search(coordinates, initial_solution, max_cycles):
    solglobal = initial_solution
    custoSG = calculate_cost(solglobal, coordinates)
    nciclos = max_cycles

    while nciclos > 0:
        nciclos -= 1
        mcl = custoSG
        rsl = solglobal[:]

        for i in range(len(solglobal) - 1):
            # Gera uma solução local trocando duas cidades consecutivas
            sollocal = solglobal[:]
            sollocal[i], sollocal[i + 1] = sollocal[i + 1], sollocal[i]
            aux = calculate_cost(sollocal, coordinates)

            # Atualiza o menor custo local
            if aux < mcl:
                mcl = aux
                rsl = sollocal

        # Atualiza a solução global se houve melhora
        if mcl < custoSG:
            custoSG = mcl
            solglobal = rsl
        else:
            break

    return solglobal, custoSG

# Exemplo de uso
if __name__ == "__main__":
    # Coordenadas das cidades (pode substituir por outras)
    cities = [
        (0, 0),  # Cidade 1
        (1, 3),  # Cidade 2
        (4, 3),  # Cidade 3
        (6, 1),  # Cidade 4
        (3, 0),  # Cidade 5
        (2, 2),  # Cidade 6
        (5, 5)   # Cidade 7
    ]

    # Solução inicial definida
    initial_solution = [1, 2, 3, 4, 5, 6, 7]
    max_cycles = 100

    # Executa o algoritmo
    best_solution, best_cost = local_search(cities, initial_solution, max_cycles)

    print("Melhor solução encontrada:", best_solution)
    print("Custo total da solução:", best_cost)
