from itertools import combinations
import random

# random.seed(1)

class Genetic_Algorithm:
	def __init__(self, n_individuals, len_individual):
		self.n_individuals = n_individuals
		self.len_individual = len_individual

	def initialize_set(self, len_individual):
		individuals = {}
		for i in range(self.n_individuals):
			individual = []
			for _ in range(len_individual):
				individual.append(random.randint(0,1))
			individuals[i] = [individual]
		return individuals

	def get_fitness(self, individuals):		
		for individual, chromosome in individuals.items():
			fitness = 0
			for gene in chromosome[0]:
				if gene == 1: fitness += 1
			try:
				individuals[individual][1] = fitness
			except IndexError: #first iteration
				individuals[individual].append(fitness)
		return individuals

	def roulette_method(self, individuals):
		summation = sum(list(map(lambda gene: gene[1], list(individuals.values()))))
		for individual in individuals:
			chance = individuals[individual][1]/summation
			try:
				individuals[individual][2] = chance
			except IndexError: #first iteration
				individuals[individual].append(chance)

		new_individuals = {}
		temp = []
		i = 0
		while len(new_individuals) != len(individuals):			
			for individual, chromosome in individuals.items():
				if chromosome[2] >= random.random():
					new_individuals[i] = [chromosome[0]]
					temp.append(chromosome[0])
			i += 1

		return individuals

	def recombination(self, individuals, rate_recombination):
		count_combination = 0
		did_combination = False
		for combination in list(combinations(list(individuals.items()),2)):
			if rate_recombination >= random.random() and count_combination < 2: #crossover		
				c_a, c_b = combination
				index_c_a = c_a[0]
				index_c_b = c_b[0]
				slice_point = random.randint(0, len(c_a[1][0]))
				new_c_a = [c_a[1][0][:slice_point] + c_b[1][0][slice_point:]]
				new_c_b = [c_b[1][0][:slice_point] + c_a[1][0][slice_point:]]
				count_combination += 1
				did_combination = True

			if did_combination:
				individuals[index_c_a] = new_c_a
				individuals[index_c_b] = new_c_b
				did_combination = False

		return individuals

	def mutation(self, individuals, rate_mutation):		
		did_mutation = False
		for individual, chromosome in individuals.items():			
			for i in range(len(chromosome[0])):				
				if rate_mutation >= random.random():
					if chromosome[0][i] == 0:
						gene = 1
					else:
						gene = 0
					new_chromosome = chromosome.copy()
					new_chromosome[0][i] = gene
					did_mutation = True
			if did_mutation:
				individuals[individual] = new_chromosome
				did_mutation = False
		return individuals