# Genetic Algorithm to solve the Travelling Salesman Problem.

from itertools import combinations, permutations, zip_longest
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
				while len(chromosome) < self.len_individual:
					random_number = random.randrange(self.len_individual)
					if random_number not in chromosome:
						chromosome.append(random_number)
			individuals[i] = (chromosome,[None, None])
		return individuals

	def get_fitness(self, individuals, distancies):		
		for individual in individuals:
			fitness = 0
			for i in range(self.len_individual-1):
				city_u = individuals[individual][0][i]
				city_v = individuals[individual][0][i+1]
				cities = (city_u, city_v)
				if (city_u, city_v) not in distancies:
					cities = (city_v, city_u)
				fitness += distancies[cities]
			individuals[individual][1][0] = fitness
		return individuals

	def roulette_method(self, individuals): #seletion
		individuals_values = list(individuals.values())
		summation = sum(list(map(lambda gene: gene[1][0], individuals_values)))		
		
		inverse_chances = list(map(lambda gene: 1-(gene[1][0]/summation), individuals_values))
		chances = list(map(lambda chance: chance/sum(inverse_chances), inverse_chances))

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
				slice_point = random.randrange(self.len_individual)
				
				new_c_a = c_a[1][0][:slice_point]
				saw_c_b = False
				while True:
					if not saw_c_b:
						for gene in c_b[1][0][slice_point:]:
							if gene not in new_c_a:
								new_c_a.append(gene)
						saw_c_b = True

					if len(new_c_a) != 6:
						for gene in c_b[1][0]:
							if gene not in new_c_a:
								new_c_a.append(gene)
					else: break
				new_c_a = (new_c_a, [None, None])

				new_c_b = c_b[1][0][:slice_point]
				saw_c_a = False
				while True:
					if not saw_c_a:
						for gene in c_b[1][0][slice_point:]:
							if gene not in new_c_b:
								new_c_b.append(gene)
						saw_c_a = True

					if len(new_c_b) != 6:
						for gene in c_b[1][0]:
							if gene not in new_c_b:
								new_c_b.append(gene)
					else: break
				new_c_b = (new_c_b, [None, None])				

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
			if rate_mutation >= random.random():
				a, b = random.sample(list(range(self.len_individual)), k = 2)
				new_chromosome = chromosome[0].copy()
				temp_a = new_chromosome[a]
				temp_b = new_chromosome[b]
				new_chromosome[a], new_chromosome[b] = temp_b, temp_a
				did_mutation = True
			if did_mutation:
				individuals[individual] = [new_chromosome, [None, None]]
				did_mutation = False
		return individuals