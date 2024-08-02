from fake_math import divide as fake_divide
from true_math import divide as true_divide

first_number = 10
second_number = 0

print('Результаты деления:')
print('Из fake_math:', fake_divide(first_number, second_number))
print('Из true_math:', true_divide(first_number, second_number))
