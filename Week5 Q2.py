number_of_students = int(input('Enter the number of students: '))
print(number_of_students)

number_of_computers_per_lab = int(input('Enter the number of computers in each lab: '))
print(number_of_computers_per_lab)

number_of_labs = number_of_students // number_of_computers_per_lab
print(number_of_labs)
if number_of_students % number_of_computers_per_lab != 0:
    number_of_labs += 1

print('There are ' + str(number_of_labs) + ' labs that are needed!')
