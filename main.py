
import json
import os
import requests

HEADERS={
    "Content-Type": "application/json",
    "x-api-key" : os.environ["API_KEY"]
}


def get_random_details():
    url = "https://api.spoonacular.com/recipes/random"
    params = {
        "includeNutrition": False,
        "number": 1

    }
    response=requests.get(url=url,params=params,headers=HEADERS)
    response=json.dumps(response.json())
    response = json.loads(response)
    print(response["recipes"][0]["title"])
    print(response["recipes"][0]["image"])
    print(response["recipes"][0]["sourceUrl"])
    print(f'cooking time is {response["recipes"][0]["readyInMinutes"]}')
    return f'the name of it is {response["recipes"][0]["title"]} and the image {response["recipes"][0]["image"]} and the url {response["recipes"][0]["sourceUrl"]}'
#get_random_details(response)

response2=[{'id': 662665, 'title': 'Swiss Bircher Muesli', 'image': 'https://img.spoonacular.com/recipes/662665-312x231.jpg', 'imageType': 'jpg', 'usedIngredientCount': 2, 'missedIngredientCount': 2, 'missedIngredients': [{'id': 42184, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 'unitShort': 'cup', 'aisle': 'Cereal', 'name': 'muesli', 'original': '1/2 cup muesli', 'originalName': 'muesli', 'meta': [], 'image': 'https://img.spoonacular.com/ingredients_100x100/granola.jpg'}, {'id': 1119, 'amount': 3.0, 'unit': 'tablespoons', 'unitLong': 'tablespoons', 'unitShort': 'Tbsp', 'aisle': 'Milk, Eggs, Other Dairy', 'name': 'vanilla yoghurt', 'original': '3 tablespoons of plain or vanilla yoghurt', 'originalName': 'plain or vanilla yoghurt', 'meta': ['plain'], 'extendedName': 'plain vanilla yoghurt', 'image': 'https://img.spoonacular.com/ingredients_100x100/vanilla-yogurt.png'}], 'usedIngredients': [{'id': 9003, 'amount': 1.0, 'unit': '', 'unitLong': '', 'unitShort': '', 'aisle': 'Produce', 'name': 'apple', 'original': '1 Apple', 'originalName': 'Apple', 'meta': [], 'image': 'https://img.spoonacular.com/ingredients_100x100/apple.jpg'}, {'id': 1077, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 'unitShort': 'cup', 'aisle': 'Milk, Eggs, Other Dairy', 'name': 'milk', 'original': '1/2 cup of Milk', 'originalName': 'Milk', 'meta': [], 'image': 'https://img.spoonacular.com/ingredients_100x100/milk.png'}], 'unusedIngredients': [{'id': 19296, 'amount': 1.0, 'unit': 'serving', 'unitLong': 'serving', 'unitShort': 'serving', 'aisle': 'Nut butters, Jams, and Honey', 'name': 'honey', 'original': 'honey', 'originalName': 'honey', 'meta': [], 'image': 'https://img.spoonacular.com/ingredients_100x100/honey.png'}], 'likes': 1}]

def make_ingredents_comma_seprated():
    ingredient=input("please enter an ingredient one at a time once you are done enter -1 \n")
    comma=""
    while ingredient != "-1":
        #need to deal with what if the ingredient is empty
        if comma=="": #checking if it's the first time
            comma+=ingredient
        else:
            comma+=f",{ingredient}"
        ingredient = input("")

    return comma

def Get_recipe_based_on_ingredents():

    url="https://api.spoonacular.com/recipes/findByIngredients"
    params={
        "ingredients": make_ingredents_comma_seprated(),
        "number":1,
        "ranking":2,
        "ignorePantry":True
    }
    response=requests.get(url=url,params=params,headers=HEADERS)
    response=json.dumps(response.json())
    response = json.loads(response)
    print(response[0]["title"])
    id=response[0]['id']
    keepgoing=True
    i=0
    while (keepgoing):
        try:
            print(response[0]["missedIngredients"][i]["name"])
        except:
            keepgoing=False
        else:
            i+=1
        #going and printing each item that is missing
    get_recipe_by_id(id)


def get_recipe_by_id(id):
    response=requests.get(url=f"https://api.spoonacular.com/recipes/{id}/information",headers=HEADERS)
    response = json.dumps(response.json())
    response = json.loads(response)
    print(response["sourceUrl"])


