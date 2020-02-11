import random

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
    print('Your cards:', gamer_hand, 'Dealer`s cards:', dealer_hand)
    print('Your points:', cards_count(gamer_hand), 'Dealers points:', cards_count(dealer_hand))

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
Dealers turn
"""

def dealer():

    dealer_hand.append(cards.pop())

    if (cards_count(dealer_hand) < cards_count(gamer_hand)) and (cards_count(dealer_hand) < 20):
        dealer()

    else:
        turn_dealer = 0
"""
ОСНОВНОЙ ЦИКЛ ИГРЫ
"""

game_over = 0 # по этой переменной будем вырубать цикл
while game_over != 1:

    money_dealer = money_dealer - bid
    money_gamer = money_gamer - bid
    bank = bid_dealer + bid_gamer

    print ('Round No:', round)
    round += 1
    status()

    user_input = input('Type your choice, for example bid, more or stop: ')

    if user_input == 'bid':
        bid_gamer = int(input('Input your bid:'))
        money_gamer = money_gamer - bid_gamer
        bank = bank + bid_gamer
        gamer_hand.append(cards.pop())
        if int(cards_count(gamer_hand)) > 21:
            print('You loose this round')

    elif user_input == 'more':
        gamer_hand.append(cards.pop())
        if int(cards_count(gamer_hand)) > 21:
            print('You loose this round')


        continue

    # elif user_input == 'exit' or 'quit':
    #     break

    elif user_input == 'stop': # игрок прекращает набор карт и передает ход дилеру

        turn_dealer = 1
        while turn_dealer == 1: # запускаем цикл набора карт дилером, играет компьютерная логика
            # print("error")

            dealer()

        if cards_count(dealer_hand) > 21: # дилер проигрывает
            print('Dealer loose')

        elif cards_count(dealer_hand) > cards_count(gamer_hand) and cards_count(dealer_hand) <= 21:
            print('Dealer win!')





