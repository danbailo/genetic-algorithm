from itertools import combinations
import random

# random.seed(1)

class Genetic_Algorithm:
	def __init__(self, n_individuals, len_individual):
		self.n_individuals = n_individuals
		self.len_individual = len_individual

	def initialize_set(self):
		individuals = {}
		for i in range(self.n_individuals):
			chromosome = []
			for _ in range(self.len_individual):
				chromosome.append(random.randint(0,1))
			individuals[i] = (chromosome,[None, None])
		return individuals

	def get_fitness(self, individuals):		
		for individual in individuals:
			fitness = 0
			for i in range(self.len_individual):
				if individuals[individual][0][i] == 1: fitness += 1
			individuals[individual][1][0] = fitness
		return individuals

	def roulette_method(self, individuals): #seletion
		individuals_values = list(individuals.values())
		summation = sum(list(map(lambda gene: gene[1][0], individuals_values)))
		chances = list(map(lambda gene: gene[1][0]/summation, individuals_values))

		for individual, chance in zip(individuals, chances):
			individuals[individual][1][1] = chance

		new_individuals = {}
		i = 0
		while len(new_individuals) != len(individuals):			
			for individual, chromosome in individuals.items():
				if chromosome[1][1] >= random.random():
					new_individuals[i] = (chromosome[0],[chromosome[1][0], None])
			i += 1
		return new_individuals

	def recombination(self, individuals, rate_recombination):
		count_combination = 0
		did_combination = False
		for combination in list(combinations(list(individuals.items()), 2)):
			if rate_recombination >= random.random() and count_combination < 2: #crossover						
				c_a, c_b = combination
				index_c_a = c_a[0]
				index_c_b = c_b[0]
				slice_point = random.randint(0, self.len_individual)
				new_c_a = (c_a[1][0][:slice_point] + c_b[1][0][slice_point:], [None, None])
				new_c_b = (c_b[1][0][:slice_point] + c_a[1][0][slice_point:], [None, None])
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
			for i in range(self.len_individual):				
				if rate_mutation >= random.random():
					if chromosome[0][i] == 0:
						gene = 1
						new_fitness = chromosome[1][0] + 1
					else:
						gene = 0
						new_fitness = chromosome[1][0] - 1

					new_chromosome = chromosome[0].copy(), [new_fitness, None]
					new_chromosome[0][i] = gene
					did_mutation = True
			if did_mutation:
				individuals[individual] = new_chromosome
				did_mutation = False
		return individuals