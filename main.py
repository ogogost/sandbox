import random

# print('Добро пожаловать в игру БЛЭК ДЖЭК!')
# print(' Правила игры: Масти карты: ♥ - червы ♦ - бубны ♣ - трефы ♠ - пики ')
# print('Названия карт и их стоимость при подсчете: ')
# print('2 - 2, 3 - 3, 4 - 4, 5 - 5, 6 - 6, 7 - 7, 8 - 8,'
#       ,'\n','9 - 9, 10 - 10, J - 2, Q - 3, K - 4, A - 1 или 11')

# создаем колоду для игры
# создаем список номиналов карт в масти
street = []
for i in range(2, 11):
      street.append(i)
street.append('J')
street.append('Q')
street.append('K')
street.append('A')

# список мастей
suits = []
suits.append('♥')
suits.append('♦')
suits.append('♣')
suits.append('♠')

# создаем список карт и тасуем их
cards = []
for i in range(len(suits)):
    for j in range(len(street)):
        cards.append(str(suits[i]) + str(street[j]))

random.shuffle(cards)


# создаем стартовые условия для игры

round = 1
dealer_hand = []
gamer_hand = []
money_dealer = 1000
money_gamer = 1000
bank = 0
bid = 10
bid_gamer = bid
bid_dealer = bid

# добавляем первые карты в руки, делаются первые ставки

dealer_hand.append(cards.pop())
gamer_hand.append(cards.pop())
money_dealer = money_dealer - bid
money_gamer = money_gamer - bid
bank = bid_dealer + bid_gamer



"""
Функция отображения баланса игроков, банка и карт на руках игроков
"""
def status():
    print('BANK =', bank, 'Dealer balance=', money_dealer, 'Your balance=', money_gamer)
    print('Dealer`s cards:', dealer_hand)
    print('Your cards:', gamer_hand)

# создаю функцию для распечатки баланса денег
# def money_print():
#     print('BANK =', bank, 'Dealer balance=', money_dealer, 'Your balance=', money_gamer)
#
# создаю функицю отображения карт на руках игроков
# def cards_status():
#     print('Dealer`s cards:', dealer_hand)
#     print('Your cards:', gamer_hand)



"""
функция для подсчета очков на руках игрока/дилера
"""

def cards_count(hand):
    counter = 0
    counter_temp = 0
    aces = 0
    aces_factor = 0
    hand2 = hand.copy() # временный список для подсчета очков, т.к. впрямую сумму не посчитать
    for i in range(len(hand2)):
        hand2[i] = hand2[i][1:3] # убираем символ масти, для подсчета не нужен
        if hand2[i] == 'J' or hand2[i] == 'Q' or hand2[i] == 'K':
            hand2[i] = 10 # заменяем картинки(кроме туза) на 10
    aces = hand2.count('A') # считаем количество тузов в руке

    if aces >= 1: # если тузы есть
        hand3 = hand2.copy() # создаем новый список без тузов
        hand3.remove('A')
        for i in range(len(hand3)):
            hand3[i] = int(hand3[i])
        counter_without_aces = sum(hand3)
        if counter_without_aces > 11:
            aces_factor = 1
        else:
            aces_factor = 11
        counter = counter_without_aces + aces * aces_factor

    else: # если тузов нет, идет просто подсчет очков в руке
        for i in range(len(hand2)):
            hand2[i] = int(hand2[i])
        counter = sum(hand2)

    return counter


"""
ОСНОВНОЙ ЦИКЛ ИГРЫ
"""


while True:

    money_dealer = money_dealer - bid
    money_gamer = money_gamer - bid
    bank = bid_dealer + bid_gamer

    print ('Round No:', round)
    round += 1
    status()

    user_input = input('Type your choice, for example bid, more or stop: ')
    if user_input == 'bid':
        user_bid = int(input('Input your bid:'))
        money_gamer = money_gamer - user_bid
        bank = bank + user_bid
        gamer_hand.append(cards.pop())
        print('Your points:', cards_count(gamer_hand))
        if int(cards_count(gamer_hand)) > 21:
            print('You loose this round')

    elif user_input == 'more':
        gamer_hand.append(cards.pop())
        print('Your points:', cards_count(gamer_hand))

        if int(cards_count(gamer_hand)) > 21:
            print('You loose this round')


        continue



    elif user_input == 'exit' or 'quit':
        break

    elif user_input == 'stop': # игрок прекращает набор карт и передает ход дилеру

        flag = 1

        while flag == 1: # запускаем цикл набора карт дилером, играет компьютерная логика

            dealer_hand.append(cards.pop())

            print('Dealers points:', cards_count(dealer_hand))

            if cards_count(dealer_hand) < cards_count(gamer_hand) and cards_count(dealer_hand) < 20:
                continue
            else:
                flag = 0

        if cards_count(dealer_hand) > 21: # дилер проигрывает
                print('Dealer loose')




