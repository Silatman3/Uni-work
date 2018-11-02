from statistics import mean


first_sweet = input('Enter the price of the first sweet:    ')[:-1]
second_sweet = input('Enter the price of the second sweet:   ')[:-1]
third_sweet = input('Enter the price of the third sweet:    ')[:-1]
fourth_sweet = input('Enter the price of the fourth sweet:   ')[:-1]
fifth_sweet = input('Enter the price of the fifth sweet:    ')[:-1]
print()

first_sweet = int(first_sweet)
second_sweet = int(second_sweet)
third_sweet = int(third_sweet)
fourth_sweet = int(fourth_sweet)
fifth_sweet = int(fifth_sweet)

total_price = first_sweet + second_sweet + third_sweet + fourth_sweet + fifth_sweet
print('Total price: ', total_price)

average_price = (first_sweet, second_sweet, third_sweet, fourth_sweet, fifth_sweet)
print('Average price: ', mean(average_price))

highest_price = max(average_price)
print('Highest price: ', highest_price)

lowest_price = min(average_price)
print('Lowest price: ', lowest_price)
