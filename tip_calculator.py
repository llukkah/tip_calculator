#total cost of food
cost_of_food = float(input("Enter the total cost of food: "))

#calculating 10% sales tax
ten_tax = float((cost_of_food*.10))

# letting user know the 10% sales tax of the total cost of food
print(f'Okay, 10% sales tax of {cost_of_food} is $ {ten_tax}')

#asking number of peopel splitting bill
num_people = int(input("Now enter how many people splitting the bill: "))

#asking the percentage of tip to add to bill
percentage_tip = float(input("How much percentage do you want to add?: "))

#converting the number to a decimal
percentage_decimal = float(percentage_tip/100)

#making sure the decimal is created
# print(f'percentage decimal: {percentage_decimal}')

#calculating tip of food cost
tip_of_food = float(cost_of_food*percentage_decimal)

#making sure tip of food amount is correct
# print(f'tip of food: {tip_of_food}')

#doing the math to add the total cost of food, tax, and the amount of % to tip
including_tip = float(ten_tax + tip_of_food + cost_of_food)

#making sure of the number of the food cost and including tip
# print(f'including tip : {including_tip}')

#finding the amount each person should pay
each_person_pay = float(including_tip / num_people)

#desired output
print('')
print('________________________________________')
print(f'Cost of food : ${cost_of_food}')
print('+')
print(f'10% Sales Tax : ${ten_tax}')
print('+')
print(f'{percentage_tip}% Tip: ${tip_of_food}')
print('________________________________________')
print(f'The total bill is ${including_tip}.\n  Each person ({num_people}) should pay ${each_person_pay}')

