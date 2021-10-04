

#total cost of food
cost_of_food = int(input("Enter the total cost of food: "))

#adding 10% sales tax
total_food = (cost_of_food*.10) + cost_of_food

# letting user know the total cost of food after adding 10% sales tax
print(f'Okay, the total cost of food including 10% sales tax is $ {total_food}')

#asking number of peopel splitting bill
num_people = int(input("Now enter how many people splitting the bill: "))

#asking the percentage of tip to add to bill
percentage_tip = float(input("How much percentage do you want to add?: "))

#converting the number to a decimal
percentage_decimal = percentage_tip/100

#making sure the decimal is created
# print(f'percentage decimal: {percentage_decimal}')

#doing the math to add the total cose of food and the amount of % to tip
including_tip = total_food + (total_food*percentage_decimal)

#making sure of the number of the food cost and including tip
# print(f'including tip : {including_tip}')

#finding the amount each person should pay
each_person_pay = including_tip / num_people

#desired output
print(f'The total bill including tip is $ {including_tip}.  Each person ({num_people}) should pay ${each_person_pay}')
