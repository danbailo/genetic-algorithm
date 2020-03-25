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

	epochs = 10000
	rate_recombination = 0.7
	rate_mutation = 0.03	

	genetic_algorithm = Genetic_Algorithm(n_individuals, nodes, initial)
	individuals = genetic_algorithm.initialize_set()
	individuals = genetic_algorithm.get_fitness(individuals, distancies)	
	for chromosome in individuals:
		print(chromosome)
	print()


	for _ in range(epochs):
		individuals = genetic_algorithm.roulette_method(individuals)
		individuals = genetic_algorithm.get_fitness(individuals, distancies)
		for chromosome in individuals:
			print(chromosome)
		print()		
		exit()

		individuals = genetic_algorithm.recombination(individuals, rate_recombination)
		individuals = genetic_algorithm.get_fitness(individuals, distancies)

		individuals = genetic_algorithm.mutation(individuals, rate_recombination)
		individuals = genetic_algorithm.get_fitness(individuals, distancies)

	for chromosome in individuals:
		print(chromosome)
	print()		