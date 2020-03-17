from core import Genetic_Algorithm

if __name__ == "__main__":
	n_individuals = 10
	epochs = 100

	genetic_algorithm = Genetic_Algorithm(n_individuals, epochs)

	individuals = genetic_algorithm.initialize_set(10)

	print(*individuals.items(), sep="\n")

	print(list(individuals.values())[0][1])

	print(sum(list(map(lambda gene: gene[1], list(individuals.values())))))