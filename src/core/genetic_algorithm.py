import numpy as np
import random

random.seed(1)

class Genetic_Algorithm:
	def __init__(self, n_individuals, epochs):
		self.n_individuals = n_individuals
		self.epochs = epochs

	def initialize_set(self, len_individual):
		individuals = {}
		for i in range(self.n_individuals):
			individual = []
			fitness = 0
			for _ in range(len_individual):
				gene = random.randint(0,1)
				individual.append(gene)
				if gene == 1: fitness += 1
			individuals[i] = (individual, fitness)
		return individuals

	def roulette_method(self, individual, individuals):
		summation = sum(individuals.values())
		return (individuals[individual]/summation)

	def linear_ranking_method(self, beta, individuals):
		ranking = np.zeros(len(individuals))
		i = 0
		n = len(individuals)
		for individual, value in individuals.items():
			rank = beta-2 * (beta-1) * ((i-1) / n-1)
			ranking[i] = (1/n) * rank
			i += 1
