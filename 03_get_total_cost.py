servings = 2.5
amounts_list = [['Chickpeas', 166.0, 3.7, 500.0], ['Onion', 40.0, 2.49, 1000.0], ['Parsley', 5.0, 5.0, 8.0], ['Cumin', 2.0, 2.0, 30.0], ['Ground Coriander', 1.0, 2.3, 30.0], ['Salt', 3.0, 1.4, 1000.0], ['Chickpea Flour', 4.0, 10.0, 1000.0]]
total = 0.0
print("Recipe amount:     item:               unit cost:      unit weight:      cost to make:")
for item in amounts_list:
    item_name = item[0]
    recipe_amount = item[1]
    unit_cost = item[2]
    unit_amount = item[3]

    cost_to_make = unit_cost/unit_amount*recipe_amount
    # print(item[0] + " cost is " + str(cost_to_make))
    print("{:>13.0f}g     {:<20}${:<10.2f}{:>10}g            ${:.2f}".format(recipe_amount, item_name, unit_cost, unit_amount, cost_to_make))
    total += cost_to_make

print("total: ${:.2f}".format(total))
print("cost per serving: ${:.2f}".format(total/servings))
