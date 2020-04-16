#!/usr/bin/python

import math

def recipe_batches(recipe, pantry):
  """Return an int

  How many batches of the recipe can
  be made with ingredients in the pantry?
  """

  max_batches = -1

  # The minimum ingredients are listed in the recipe dictionary, so we need to walk through it once.
  for ingredient in recipe:
    if ingredient in pantry:
      # print(ingredient, '->', recipe[ingredient], pantry[ingredient])

      if max_batches == -1: # First pass. Start calculating max dishes from scratch.
        max_batches = pantry[ingredient]//recipe[ingredient]
      else:
        max_batches =  min(max_batches, (pantry[ingredient]//recipe[ingredient]))

    else: # Insufficient ingredients. Exit.
      # print(ingredient, '->', recipe[ingredient], "None")
      return 0

  return max_batches

if __name__ == '__main__':
  # Test example
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
    batches=recipe_batches(recipe, ingredients), ingredients=ingredients))