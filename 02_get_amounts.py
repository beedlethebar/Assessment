my_ingredients_list = ['chickpeas', 'onion', 'coriander', ]


def get_amounts(ingredients_list):
    recipe_amounts = []

    for ingredient in ingredients_list:
        recipe_grams = 0.0
        unit_price = 0.0
        unit_grams = 0.0
        question = "enter amount of " + ingredient + " in recipe (in grams): "
        # recipe_amount = input("how much " + ingredient + " (enter in grams): ")
        valid = False
        while not valid:
            try:
                recipe_grams = float(input(question))
                valid = True
            except ValueError:
                print('please input a valid number')

        question = "enter unit cost for " + ingredient + " (in dollars): $"
        valid = False
        while not valid:
            try:
                unit_price = float(input(question))
                valid = True
            except ValueError:
                print('please input a valid number')
        question = "weight of " + ingredient + " unit (in grams): "
        valid = False
        while not valid:
            try:
                unit_grams = float(input(question))
                valid = True
            except ValueError:
                print('please input a valid number')
        recipe_amounts.append([ingredient, recipe_grams, unit_price, unit_grams])

    return recipe_amounts


print(get_amounts(my_ingredients_list))
