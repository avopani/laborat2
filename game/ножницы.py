import random

def vi():
    choice = input("Введите 0 - камень, 1 - ножницы, 2 - бумага: ")
    return int(choice) if choice in ['0', '1', '2'] else None

def comp():
    return random.randint(0, 2)  # 0 - камень, 1 - ножницы, 2 - бумага

def ktoviigral(user, computer):
    if user == computer:
        return "Ничья!"
    elif (user == 0 and computer == 1) or\
        (user == 1 and computer == 2) or\
            (user == 2 and computer == 0):
        return "Вы выиграли!"
    else:
        return "Вы проиграли!"

def game():
    print("Камень-Ножницы-Бумага!")
    u = vi()
    while u is None:
        print("Неверный ввод. Пожалуйста, попробуйте снова.")
        u = vi()
    comput = comp()
    choices = ["камень", "ножницы", "бумага"]
    print(f"Вы: {choices[u]}, Компьютер: {choices[comput]}")
    print(ktoviigral(u, comput))
    
game()
