import random
from decouple import config


def play_game():
    initial_money = int(config('MY_MONEY', default=1000))
    money = initial_money

    while True:
        print(f"Ваш текущий капитал: {money}$")
        try:
            bet = int(input("Сделайте вашу ставку: "))
            if bet <= 0:
                raise ValueError("Ставка должна быть числом.")
        except ValueError as e:
            print(e)
            continue

        selected_slot = int(input("Выберите слот от 1 до 10: "))

        winning_slot = random.randint(1, 10)
        print(f"Выпавший номер: {winning_slot}")

        if selected_slot == winning_slot:
            money += bet * 2
            print(f"Вы выиграли! Ваш текущий капитал: {money}$")
        else:
            money -= bet
            print(f"Проигрыш! Ваш текущий капитал: {money}$")

        if money <= 0:
            print("У вас закончились деньги.")
            break

        play_again = input("Хотите сыграть еще? (да/нет): ")
        if play_again.lower() == "да" or "lf":
            continue
        else:
            print('Игра окончена.')
            break

    if money > initial_money:
        print("Вы в выигрыше!")
    elif money < initial_money:
        print("Вы в проигрыше.")
    else:
        print("Вы остались при своих.")
