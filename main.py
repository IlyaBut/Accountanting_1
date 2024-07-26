
from datetime import date
from Employees import Employees
from application.db.Interns import candidates
from application.db.Translator import get_translator
from application.db.people import get_employees
from application.sallary import calculate_salary

if __name__ == '__main__':
    dt_now = date.today()
    print(f'Сегодня {dt_now}')

    while True:
        command = input('Нужен перевод - ')
        if command == 'Да':
            print(get_translator())
        command = input('Введите команду: ')
        if command == 'Рассчитать заработную плату':
            print(calculate_salary(Employees))
        if command == 'Добавить сотрудника':
            print(get_employees(candidates))
            break
        else:
            print('Нет такой команды')
