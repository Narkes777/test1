from random import randint
import datetime
import random

now = datetime.datetime.now()
hour = now.hour
a = str(input())

if hour < 12:
    greeting = "Good morning! Welcome to our restaurant!"
elif hour < 18:
    greeting = "Good afternoon! Welcome to our restaurant!"
else:
    greeting = "Good evening! Welcome to our restaurant!"
        
if a == "Hi" or "Hello":
    print("{}!".format(greeting))
    
free_tables = random.sample(range(1, 11), 5)

for table in free_tables:
    print(f"Столик #{table} свободен")

menu = {
    'a' : {
        'Суп гороховый': 2000,
        'Борщ': 1000,
        'Крем-суп с грибами': 2500,
        'Лапша с курицей': 2100,
        'Минестроне': 2300,
    },
    'b' : {
        'Стейк': 5000,
        'Рыба-гриль': 2000,
        'Паста с морепродуктами': 3000,
        'Котлеты куриные': 2500,
        'Бифштекс': 2000,
    },
    'c' : {
        'Чизкейк': 3000,
        'Шоколадный мусс': 1500,
        'Тирамису': 2500,
        'Фруктовое мороженое': 2000,
        'Клубничный пирог': 1000,
    },
    'd' : {
        'Кофе': 500,
        'Чай': 200,
        'Какао': 500,
        'Горячий шоколад': 500,
        'Латте': 1000,
    },
    'e' : {
        'Мохито': 500,
        'Космополитен': 1000,
        'Маргарита': 1500,
        'Пиво': 2000,
        'Вино': 2000,
    },
}

total_cost = 0
  
while True:
    print("\nМеню:")
    for key, value in menu.items():
        print(f"{key}) {value}")

    choice = input("Выберите опцию (a-f): ")

    if choice in menu:
        if choice == 'a':
            print("Список первых блюд:")
            num = 1
            for i in menu['a']:
                print(f"{num}) {i} - {menu['a'][i]} тенге")
                num += 1
            first_choice = int(input("Сделайте выбор: "))
            dish_price = menu['a'][list(menu['a'].keys())[first_choice - 1]]
        elif choice == 'b':
            print("Список вторых блюд:")
            num = 1
            for i in menu['b']:
                print(f"{num}) {i} - {menu['b'][i]} тенге")
                num += 1
            first_choice = int(input("Сделайте выбор: "))
            dish_price = menu['b'][list(menu['b'].keys())[first_choice - 1]]
        elif choice == 'c':
            print("Список десертов:")
            num = 1
            for i in menu['c']:
                print(f"{num}) {i} - {menu['c'][i]} тенге")
                num += 1
            first_choice = int(input("Сделайте выбор: "))
            dish_price = menu['c'][list(menu['c'].keys())[first_choice - 1]]
        elif choice == 'd':
            print("Список напитков:")
            num = 1
            for i in menu['d']:
                print(f"{num}) {i} - {menu['d'][i]} тенге")
                num += 1
            first_choice = int(input("Сделайте выбор: "))
            dish_price = menu['d'][list(menu['d'].keys())[first_choice - 1]]
        elif choice == 'e':
            print("Список бара:")
            num = 1
            for i in menu['e']:
                print(f"{num}) {i} - {menu['e'][i]} тенге")
                num += 1
            first_choice = int(input("Сделайте выбор: "))
            dish_price = menu['e'][list(menu['e'].keys())[first_choice - 1]]
        elif choice == 'f':
            print("Вы сделали заказ.")
   
            total_cost *= 1.1  
            print(f"Общая сумма заказа: {total_cost:.2f} тенге (с обслуживанием 10%)")
            break

        
        total_cost += dish_price
    else:
        print("Некорректный выбор. Пожалуйста, выберите опцию от 'a' до 'f'.")
