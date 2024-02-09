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