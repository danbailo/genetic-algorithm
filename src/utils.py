import json
import os

def get_graph(file):
	with open(file, "r") as file:
		data = json.load(file)
	return data