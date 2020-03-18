from core import Genetic_Algorithm

if __name__ == "__main__":
	n_individuals = 10
	len_individual = 10
	epochs = 1000
	rate_recombination = 0.5
	rate_mutation = 0.01

	genetic_algorithm = Genetic_Algorithm(n_individuals, len_individual)

	print("First set")
	individuals = genetic_algorithm.initialize_set(len_individual)
	first = genetic_algorithm.get_fitness(individuals)
	for individual, chromosome in first.items():
		print(f"{chromosome}")
	first = list(first.values())
	summation = sum(list(map(lambda gene: gene[1], first)))
	print(summation)


	for epoch in range(epochs):
		# print(f"\nEpoch {epoch+1}")
		individuals = genetic_algorithm.get_fitness(individuals)
		individuals = genetic_algorithm.roulette_method(individuals)
		individuals = genetic_algorithm.recombination(individuals, rate_recombination)
		individuals = genetic_algorithm.mutation(individuals, rate_mutation)
	print()

	print("Last set")
	last = genetic_algorithm.get_fitness(individuals)
	for individual, chromosome in last.items():
		print(f"{chromosome[:2]}")
	last = list(last.values())
	summation = sum(list(map(lambda gene: gene[1], last)))
	print(summation)		