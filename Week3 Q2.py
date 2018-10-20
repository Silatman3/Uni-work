"""
Week 3 Q2
|   Number of Sweets    |   Number of Pupils    |   Sweets per pupil    |   Sweets leftover     |
|           35          |           15          |           2           |           5           |
|           47          |           16          |           2           |           15          |
|           59          |           17          |           3           |           8           |
|           71          |           18          |           3           |           17          |

"""

number_of_pupils = int (input('Enter number of pupils: '))
number_of_sweets = int (input('Enter number of sweets: '))

sweets_per_pupil = (number_of_sweets)//(number_of_pupils)
print(sweets_per_pupil)

sweets_leftover = (number_of_sweets)-((number_of_pupils)*(sweets_per_pupil))
print(sweets_leftover)