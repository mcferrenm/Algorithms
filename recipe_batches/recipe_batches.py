#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    min_batches = float("inf")
    current_batches = 0

    for i in recipe.keys():
        if i in ingredients:
            current_batches = ingredients[i] // recipe[i]

            if current_batches < min_batches:
                min_batches = current_batches
        else:
            return 0
            
    return min_batches
    # print(min_batches, current_batches, ingredients[i], recipe[i])


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
