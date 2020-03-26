from core import Genetic_Algorithm
from utils import get_graph

if __name__ == "__main__":
	data = get_graph("input/graph.json")

	#preparing data
	data_encoded = {}
	index = 0
	for node in data["nodes"]:
		data_encoded[node] = index
		index += 1

	#get distance
	distancies = {}
	for edge in data["edges"]:
		city1, city2, value = edge
		distancies[data_encoded[city1], data_encoded[city2]] = value

	n_individuals = 10
	nodes = data_encoded.values()

	node_initial = "Campo Grande"
	initial = data_encoded[node_initial]

	epochs = 100
	rate_recombination = 0.7
	rate_mutation = 0.03

	genetic_algorithm = Genetic_Algorithm(n_individuals, nodes, initial)

	#First gen
	individuals = genetic_algorithm.initialize_set()
	individuals = genetic_algorithm.get_fitness(individuals, distancies)
	min_ = float("inf")
	for chromosome in individuals:
		if min_ > 1/chromosome[1]:
			best_chromosome = chromosome
			min_ = 1/chromosome[1]
	

	decoded_solution = []

	first_gen = [initial] + best_chromosome[0] + [initial]
	for gene in first_gen:
		for k,v in data_encoded.items():
			if gene == v:
				decoded_solution.append(k)

	print(f"\nFirst gen: {first_gen} - cost: {round(min_)}")
	print(f"Decoded solution: {decoded_solution}")

	best_index = None

	for i in range(epochs):

		individuals = genetic_algorithm.roulette_method(individuals)
		individuals = genetic_algorithm.get_fitness(individuals, distancies)

		individuals = genetic_algorithm.recombination(individuals, rate_recombination)
		individuals = genetic_algorithm.get_fitness(individuals, distancies)
			
		individuals = genetic_algorithm.mutation(individuals, rate_recombination)
		individuals = genetic_algorithm.get_fitness(individuals, distancies)

		for chromosome in individuals:
			if min_ > 1/chromosome[1]:
				best_index = i
				best_chromosome = chromosome
				min_ = 1/chromosome[1]

	decoded_solution = []

	best_gen = [initial] + best_chromosome[0] + [initial]
	for gene in best_gen:
		for k,v in data_encoded.items():
			if gene == v:
				decoded_solution.append(k)

	print(f"\nBest gen at epoch {best_index}: {best_gen} - cost: {round(min_)}")
	print(f"Decoded solution: {decoded_solution}")