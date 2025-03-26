
import json
import os
import requests
import food

HEADERS={
    "Content-Type": "application/json",
    "x-api-key" : os.environ["API_KEY"]
}

recipe=food.food()
recipe.Get_recipe_based_on_ingredients("banana,apple,honey")





