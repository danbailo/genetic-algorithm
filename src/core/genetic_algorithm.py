# Genetic Algorithm to solve the Travelling Salesman Problem.

from itertools import combinations
import random

class Genetic_Algorithm:
	def __init__(self, n_individuals, nodes, initial):
		self.n_individuals = n_individuals
		self.nodes = nodes
		self.initial = initial
		self.population = list(self.nodes)
		self.population.remove(self.initial)

	def initialize_set(self):
		individuals = []
		while len(individuals) != self.n_individuals:
			individuals.append((random.sample(self.population, k=len(self.population))))
		return individuals

	def get_fitness(self, individuals, distancies):	
		fitness = []	
		for individual in individuals:
			fit = 0
			new_individual = [self.initial] + individual + [self.initial]
			for i in range(len(self.population)+1):
				city_u = new_individual[i]
				city_v = new_individual[i+1]
				cities = (city_u, city_v)
				if (city_u, city_v) not in distancies:
					cities = (city_v, city_u)					
				fit += distancies[cities]
			fitness.append((individual, fit))
		return fitness

	def roulette_method(self, individuals): #seletion
		fitness = sum(list(map(lambda fit: fit[1], individuals)))
		p = [fit[1]/fitness for fit in individuals]

		new_individuals = []
		while len(new_individuals) < len(individuals):	
			sum_ = 0.0			
			random_number = random.random()
			for i in range(len(p)):
				sum_ += p[i]
				if random_number < sum_:
					new_individuals.append(individuals[i][0])
					break
		return new_individuals

	def recombination(self, individuals, rate_recombination):
		count_combination = 0
		did_combination = False

		new_individuals = []

		while len(new_individuals) < len(individuals):
			for chromosome in individuals:
				for combination in combinations(individuals, 2):
					if not did_combination:
						if rate_recombination >= random.random(): #crossover
							if count_combination == 2:
								did_combination = True
								continue

							c_a, c_b = combination

							slice_point = random.randint(1, len(self.population)-1)
							# slice_point_b = random.randint(1, len(self.population)-1)

							c_a_sliced = c_a[0][:slice_point]
							c_b_sliced = c_b[0][:slice_point]
							
							saw_c_b = False
							while True:
								if not saw_c_b:
									for gene in c_b_sliced:
										if gene not in c_a_sliced:
											c_a_sliced.append(gene)
									saw_c_b = True					

								if len(c_a_sliced) < len(self.population):
									for gene in c_b[0]:
										if gene not in c_a_sliced:
											c_a_sliced.append(gene)
								else: break

							saw_c_a = False
							while True:
								if not saw_c_a:
									for gene in c_a_sliced:
										if gene not in c_b_sliced:
											c_b_sliced.append(gene)
									saw_c_a = True					

								if len(c_b_sliced) < len(self.population):
									for gene in c_a[0]:
										if gene not in c_b_sliced:
											c_b_sliced.append(gene)
								else: break	

							new_individuals.append(c_a_sliced)
							new_individuals.append(c_b_sliced)
							count_combination += 1
					else:
						break
				if len(new_individuals) == len(individuals): break
				new_individuals.append(chromosome[0])
		return new_individuals

	def mutation(self, individuals, rate_mutation):		
		did_mutation = False
		temp = list(range(len(self.population)))
		for i in range(len(individuals)):			
			if rate_mutation >= random.random():
				a, b = random.sample(temp, k = 2)
				new_chromosome = individuals[i][0].copy()
				temp_a = new_chromosome[a]
				temp_b = new_chromosome[b]
				new_chromosome[a], new_chromosome[b] = temp_b, temp_a
				did_mutation = True
			if did_mutation:
				individuals[i] = new_chromosome
				did_mutation = False
			else:
				individuals[i] = individuals[i][0]
		return individuals		