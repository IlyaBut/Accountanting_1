import random

from application.db.Interns import candidates


def get_employees(candidates):
    a_1 = random.choice(list(candidates.values()))
    my_str = ', '.join(a_1)
    print(f'{my_str}, результат стажировки удовлетворительный, вы приняты на работу!')


#print(get_employees(candidates))
