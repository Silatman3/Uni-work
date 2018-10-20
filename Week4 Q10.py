from statistics import mean


first_sweet = float(input('Enter the price of the first sweet:    '))
second_sweet = float(input('Enter the price of the second sweet:   '))
third_sweet = float(input('Enter the price of the third sweet:    '))
fourth_sweet = float(input('Enter the price of the fourth sweet:   '))
fifth_sweet = float(input('Enter the price of the fifth sweet:    '))
print()

total_price = first_sweet + second_sweet + third_sweet + fourth_sweet + fifth_sweet
print('Total price:     ', + total_price)

average_price = (first_sweet, second_sweet, third_sweet, fourth_sweet, fifth_sweet)
print('Average price:   ', mean(average_price))

highest_price = max(average_price)
print('Highest price:   ', highest_price)

lowest_price = min(average_price)
print('Lowest price:    ', lowest_price)
