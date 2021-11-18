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




# input = input("enter weight: ")
print(get_weight_grams('enter weight: '))
# myString = 'abcd'
# print(myString.endswith('cd'))
