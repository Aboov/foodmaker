#imports
import json
import os
import requests

class food:
    def __init__(self):
        self.HEADERS = {
            "Content-Type": "application/json",
            "x-api-key": os.environ["API_KEY"]
        }

    def get_random_details(self):
        url = "https://api.spoonacular.com/recipes/random"
        params = {
            "includeNutrition": False,
            "number": 1

        }
        response = requests.get(url=url, params=params, headers=self.HEADERS)
        response = json.dumps(response.json())
        response = json.loads(response)
        print(response["recipes"][0]["title"])
        print(response["recipes"][0]["image"])
        print(response["recipes"][0]["sourceUrl"])
        print(f'cooking time is {response["recipes"][0]["readyInMinutes"]}')
        return f'the name of it is {response["recipes"][0]["title"]} and the image {response["recipes"][0]["image"]} and the url {response["recipes"][0]["sourceUrl"]}'

    def Get_recipe_based_on_ingredients(self,ingredients):

        url="https://api.spoonacular.com/recipes/findByIngredients"
        params={
            "ingredients":ingredients,
            "number":1,
            "ranking":2,
            "ignorePantry":True
        }
        response=requests.get(url=url,params=params,headers=self.HEADERS)
        response=json.dumps(response.json())
        response = json.loads(response)
        print(response)
        id=response[0]['id']
        keepgoing=True
        list_of_missing=[]
        i=0
        while (keepgoing):
            try:
                list_of_missing.append(response[0]["missedIngredients"][i]["name"])
            except:
                keepgoing=False
            else:
                i+=1
            #going and printing each item that is missing
        link=self.get_recipe_by_id(id)
        title=response[0]["title"]
        image=response[0]["image"]
        return f'the name of the recipe is {title} and you are missing {list_of_missing} and this is the link for it {link} and this is the image {image}'


    def get_recipe_by_id(self,id):
        response=requests.get(url=f"https://api.spoonacular.com/recipes/{id}/information",headers=self.HEADERS)
        response = json.dumps(response.json())
        response = json.loads(response)
        return response["sourceUrl"]

