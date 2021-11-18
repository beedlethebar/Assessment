# item_made = input("what item are you making? ")
# print(item_made)
# print(item_made.strip())

def get_ingredients():

    ingredients = input("put in names of all ingredients separated by commas: ")
    items = ingredients.split(',')
    items = [item.strip() for item in items] # removing extra spaces from list items
    return(items)


get_ingredients()


# ingredients_list = ['Chickpeas'
#                     'Onion'
#                     'Parsley'
#                     'Cumin'
#                     'Ground Coriander'
#                     'salt'
#                     'chickpea flour']
# amounts_list = ['166'
#                 '40'
#                 '5'
#                 '2'
#                 '1'
#                 '3'
#                 '4']
# Units = ('kg', 'g')
# if user enters kilograms, times by 1000. If user enters grams, use as normal
