import random

def pick_food():
    foods = ["noodles","rice","pizza"]
    food = random.choice(foods)
    return food

def pick_drink():
    drinks =  ("juice", "water", "cola")
    drink = random.choice(drinks)
    return drink

def show_meal(*costomers):
    for customer in costomers:
        drink = pick_drink()
        food = pick_food()
        print(customer, "get", drink, "and", food)

show_meal("I", "You", "Someone")