#!/usr/bin/env python3
"""
Tournament selection. Individuals used to generate the new population are
selected according to their fitness. Out of a tournament with TOURNAMENT_SIZE
participants, only the winner is selected (survival of the fittest).
For convenience, individuals are represented by a tuple (solution, fitness).
Prints best, worst and median fitness of individuals in the final population.

QUESTION: what happens when tournament size is smaller/larger?
QUESTION: do more generations or larger population improve the results?

"""
import string
import random

from copy import deepcopy
from operator import attrgetter
from collections import namedtuple

TARGET = "CHARLES DARWIN"
CHARACTERS = string.ascii_uppercase + " "

GENERATIONS = 50
POPULATION_SIZE = 100
TOURNAMENT_SIZE = 2
MUTATION_PROBABILITY = 0.9
MUTATION_RATE = 0.1

Individual = namedtuple("Individual", "solution fitness")


def evaluate(solution):
	return sum(1 for s,t in zip(solution, TARGET) if s != t)


def init():
	solution = [random.choice(CHARACTERS) for i in range(len(TARGET))]
	return Individual(solution, evaluate(solution))


def mutate(solution):
	for i in range(len(solution)):
		if random.random() < MUTATION_RATE:
			solution[i] = random.choice(CHARACTERS)


def select(population, k, tournament_size):
	chosen = []
	for i in range(k):
		candidates = random.sample(population, tournament_size)
		winner = min(candidates, key=attrgetter("fitness"))  # pick by fitness
		chosen.append(deepcopy(winner))  # append a copy, not a reference
	return chosen


def variate(population):
	for i in range(len(population)):
		if random.random() < MUTATION_PROBABILITY:
			mutate(population[i].solution)
	return population


population = [init() for i in range(POPULATION_SIZE)]

for i in range(GENERATIONS):
	chosen = select(population, len(population), TOURNAMENT_SIZE)
	population = variate(chosen)

	for i in range(len(population)):
		new_fitness = evaluate(population[i].solution)
		population[i] = population[i]._replace(fitness=new_fitness)

population.sort(key=attrgetter("fitness"))
params = population[0].fitness, population[-1].fitness, population[POPULATION_SIZE // 2].fitness
print("best={0}, worst={1}, median={2}".format(*params))

ITEMS_NAME = [
  "Mixed Fruit", "French Fries", "Side Salad",
  "Hot Wings", "Mozzarella Sticks", "Sampler Plate"
]
ITEMS_PRICE = [2.15, 2.75, 3.35, 3.55, 4.2, 5.8]


solution = ?


def init():
  return selection of 3 random items


def evaluate(solution, target_price):
  return abs(price_of_selected_items - target_price)


def mutate(solution):
  if random.random() > 0.5:
    solution.add(random_item)
  else:
    solution.subtract(random_item)


crossover = uniform_crossover