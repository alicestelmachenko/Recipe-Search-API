import requests

def recipe_search(ingredient):
    app_id = '31ee714f'
    app_key = '1b1cb014f72af67c66fe03b66c89068b'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()
    return data['hits']


def get_ingredient_list(choice):
    app_id = '31ee714f'
    app_key = '1b1cb014f72af67c66fe03b66c89068b'
    ingredient_result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(choice, app_id, app_key)
    )
    data = ingredient_result.json()
    return [hit for hit in data['hits'] if hit['recipe']['label'] == choice]


def programme():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)

    print('These are the recipes you can make:')
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])


def choice():
    choice = input('What recipe do you want to make?: ')
    results_chosen = get_ingredient_list(choice)

    for item in results_chosen:
        print(item['recipe']['ingredientLines'])

        slist = (item['recipe']['ingredientLines'])

        with open('slist.txt', 'w+') as text_file:
            text_file.write("To buy: \n")
            for element in slist:
                text_file.write(element)
                text_file.write("\n")

    print('Your shopping list is ready in a text file')


programme()
choice()