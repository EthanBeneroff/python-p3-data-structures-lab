spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_food_names = [x['name'] for x in spicy_foods]
    # spicy_food_names = [spicy_foods[index]['name'] for index in range(3)]
    return spicy_food_names

def get_spiciest_foods(spicy_foods):
    spiciest_food = [x for x in spicy_foods if x['heat_level'] > 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print(f'{x["name"]} ({x["cuisine"]}) | Heat Level: {"🌶" * x["heat_level"]}')
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine: return food

def print_spiciest_foods(spicy_foods):
    for x in spicy_foods:
        if x["heat_level"] > 5:
            print(f'{x["name"]} ({x["cuisine"]}) | Heat Level: {"🌶" * x["heat_level"]}')

def get_average_heat_level(spicy_foods):
    count = 0
    total = 0
    for x in spicy_foods:
        count +=1
        total = total+ x["heat_level"]
    return total/count


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
