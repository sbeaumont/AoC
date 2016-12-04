DATA = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""

import pprint

# Load data
ingredients = {}
for line in DATA.split('\n'):
    name, props = line.split(':')
    properties = {}
    for prop in props.split(','):
        propname, value = prop.split()
        properties[propname] = int(value)
    ingredients[name] = properties
pprint.pprint(ingredients)

