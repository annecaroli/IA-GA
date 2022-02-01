"""
Algoritmo Genético
Anne e Mellyssa
Inteligência Artificial 2021/2
"""
import numpy
from numpy.random import randint
import math
import random


# decodifica cromossomo binario
def decode(bounds, n_bits, bitstring):
    min = bounds[0]
    max = bounds[1]

    # converte bin -> real
    chars = ''.join([str(s) for s in bitstring])
    # converte str -> int
    integer = int(chars, 2)
    decoded = min + (max - min) * integer / 2 ** n_bits - 1
    return decoded


# funcao objetivo
def objective_function(x):
    return math.cos(x) * x + 2


# torneio por selecao
def tournament_selection(pop):
    selected = []
    for i in range(len(pop)):
        # seleciona 2 posições de individuos aleatoriamente
        pos_element_1 = randint(len(pop))
        pos_element_2 = randint(len(pop))
        # seleciona o que tem melhor aptidão entre eles
        if pop[pos_element_1][1] < pop[pos_element_2][1]:
            selected.append(pop[pos_element_1])
        else:
            selected.append(pop[pos_element_2])
    return selected


# realiza crossover entre dois cromossomos
def crossover(parent1, parent2, r_cross, r_mut):
    children1, children2 = parent1, parent2
    if random.random() < r_cross:
        # calcula ponto onde será realizado crossover
        pt = randint(1, len(parent1) - 2)
        # troca cauda dos pais e filhos são gerados
        children1 = mutation(parent1[:pt] + parent2[pt:], r_mut)
        children2 = mutation(parent2[:pt] + parent1[pt:], r_mut)
    return [children1, children2]


# realiza mutacao
def mutation(cromossomo, r_mut):
    for i in range(len(cromossomo)):
        # avalia se faz mutação
        if random.random() <= r_mut:
            # print("acontece mutação!")
            cromossomo[i] = 1 - cromossomo[i]
    return cromossomo


# avalia aptidão do cromossomo
def evaluate_population(bounds, n_bits, init_population):
    parents = []
    for elem in init_population:
        # converte a cromossomo pai de binário para real
        p = decode(bounds, n_bits, elem)
        # realiza avalição do cromossomo pai
        s = objective_function(p)
        tuple_result = (elem, s)
        parents.append(tuple_result)
    return parents


# algoritmo genetico
def genetic_algorithm(bounds, n_bits, n_iteration, n_population, crossover_rate, mutation_rate):
    # gera população inicial
    init_population = [[random.randint(0, 1) for _ in range(n_bits)] for i in range(n_population)]
    # guarda a melhor solução, que no momento eh a solução do primeiro elemento da lista
    best, best_eval = init_population[0][0], objective_function(decode(bounds, n_bits, init_population[0]))

    for gen in range(n_iteration):
        # realiza avaliação da população inicial
        parents = evaluate_population(bounds, n_bits, init_population)
        # print(parents)

        # procura pela melhor solução, minimo da função
        for i in range(len(parents)):
            if parents[i][1] < best_eval:
                best, best_eval = parents[i][0], parents[i][1]
                # print("Best ", best_eval)

        # seleciona os individuos mais aptos atraves de seleção por torneio
        selected = tournament_selection(parents)

        # cria proxima geração
        children_lst = []
        for i in range(int(n_population/2)):
            children = []
            # get selected parents in pairs
            parent1, parent2 = random.choice(selected)[0], random.choice(selected)[0]
            # print("pais selecionados ", parent1, objective_function(decode(bounds, n_bits, parent1)), parent2,
            # objective_function(decode(bounds, n_bits, parent2)))

            # realiza crossover e mutacao
            children = crossover(parent1, parent2, crossover_rate, mutation_rate)
            # print("filhos gerados ",  children[0], objective_function(decode(bounds, n_bits, children[0])),
            #      children[1], objective_function(decode(bounds, n_bits, children[1])))

            for chd in children:
                children_lst.append(chd)
        # substitui populacao
        init_population = children_lst
    return best_eval


if __name__ == '__main__':
    # variaveis
    bounds = [-20.0, 20.0]
    n_iteration = 10
    n_bits = 16
    n_population = 10
    crossover_rate = 0.6
    mutation_rate = 0.01

    average = []

    print("Iniciando algoritmo genético\n")
    for gen in [10, 20]:
        lst_result = []
        for i in range(gen):
            result = genetic_algorithm(bounds, n_bits, n_iteration, n_population, crossover_rate, mutation_rate)
            lst_result.append(result)
        average.append(numpy.mean(lst_result))
    print("Resultados")
    print("Media 10 gerações {}".format(average[0]))
    print("Media 20 gerações {}".format(average[1]))

    print("Fim algoritmo genético\n")
