from random import choice

from Employees import Employees
from Money import salary


def calculate_salary(Employees):
    p_1 = choice(Employees)
    p_2 = choice(list(salary.values()))
    print(f'В этом месяце сотрудник {p_1} получает зарплату {p_2}')

#print(calculate_salary(Employees))
