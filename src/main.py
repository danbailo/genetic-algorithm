from core import Genetic_Algorithm

if __name__ == "__main__":
	n_individuals = 10
	len_individual = 10
	epochs = 100
	rate_recombination = 0.6
	rate_mutation = 0.01

	genetic_algorithm = Genetic_Algorithm(n_individuals, len_individual)

	individuals = genetic_algorithm.initialize_set()
	individuals = genetic_algorithm.get_fitness(individuals)

	print(f"\nFirst Set - Fitness: {sum(list(map(lambda gene: gene[1][0], list(individuals.values()))))}")
	for individual, chromosome in individuals.items():
		print(f"{chromosome[0]}")	
		pass

	for _ in range(epochs):
		individuals = genetic_algorithm.roulette_method(individuals)

		# individuals = genetic_algorithm.get_fitness(individuals)

		individuals = genetic_algorithm.recombination(individuals, rate_recombination)
		individuals = genetic_algorithm.get_fitness(individuals)

		individuals = genetic_algorithm.mutation(individuals, rate_mutation)

	print(f"\nNew Set - Fitness: {sum(list(map(lambda gene: gene[1][0], list(individuals.values()))))}")
	for individual, chromosome in individuals.items():
		print(f"{chromosome[0]}")	