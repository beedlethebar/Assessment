def get_servings():
    valid = False
    while not valid:
        try:
            servings = float(input("how many servings does the recipe make? "))
            return servings
        except ValueError:
            print('please input a valid number')


def get_ingredients():

    ingredients = input("put in names of all ingredients separated by commas: ")
    items = ingredients.split(',')
    items = [item.strip() for item in items]  # removing extra spaces from list items
    return items


def get_weight_grams(question):

    valid = False
    while not valid:
        try:
            input_string = input(question)
            if input_string.endswith('kg'):
                grams = float(input_string[:-2])*1000
                return grams
            elif input_string.endswith('g'):
                grams = float(input_string[:-1])
                return grams
            elif input_string == "xxx":
                exit()


            else:
                print('please input a valid number(kg or g)or xxx to exit program')
        except ValueError:
            print('please input a valid number(kg or g)or xxx to exit program')
    # else:


def get_amounts(ingredients_list):
    recipe_amounts = []

    for ingredient in ingredients_list:
        recipe_grams = 0.0
        unit_price = 0.0
        unit_grams = 0.0
        cost_to_make = 0.0
        question = "enter amount of " + ingredient + " in recipe (in g or kg): "
        # recipe_amount = input("how much " + ingredient + " (enter in grams): ")
        recipe_grams = get_weight_grams(question)

        question = "enter unit cost for " + ingredient + " (in dollars): $"
        valid = False
        while not valid:
            try:
                unit_price = float(input(question))
                valid = True
            except ValueError:
                print('please input a valid number')
        question = "weight of " + ingredient + " unit (in g or kg): "
        unit_grams = get_weight_grams(question)
        # valid = False
        # while not valid:
        #     try:
        #         unit_grams = float(input(question))
        #         valid = True
        #     except ValueError:
        #         print('please input a valid number')
        cost_to_make = unit_price/unit_grams*recipe_grams
        recipe_amounts.append([ingredient, recipe_grams, unit_price, unit_grams, cost_to_make])

    return recipe_amounts


def print_table(amounts):
    total = 0.0
    print("Recipe amount:     item:               unit cost:      unit weight:      cost to make:")
    for item in amounts:
        item_name = item[0]
        recipe_amount = item[1]
        unit_cost = item[2]
        unit_amount = item[3]
        cost_to_make = item[4]

        # cost_to_make = unit_cost/unit_amount*recipe_amount
        # print(item[0] + " cost is " + str(cost_to_make))
        print("{:>13.0f}g     {:<20}${:<10.2f}{:>10}g            ${:.2f}".format(recipe_amount, item_name, unit_cost, unit_amount, cost_to_make))
        total += cost_to_make

    print("total:            ${:.2f}".format(total))
    print("cost per serving: ${:.2f}".format(total/servings))


item_made = input("what is the name of the recipe? ")
servings = get_servings()
my_ingredients = get_ingredients()
amounts_list = get_amounts(my_ingredients)
print_table(amounts_list)
