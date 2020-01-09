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

# print(street)
# список мастей
suits = []
suits.append('♥')
suits.append('♦')
suits.append('♣')
suits.append('♠')
# print(suits)
# создаем список карт и тасуем их
cards = []
for i in range(len(suits)):
    for j in range(len(street)):
        cards.append(str(suits[i]) + str(street[j]))
# print(cards)
random.shuffle(cards)
# print(cards)

# создаем стартовые условия для игры

print('Game start. Round 1')
dealer_hand = []
gamer_hand = []
money_dealer = 1000
money_gamer = 1000
bank = 0
bid = 10

# добавляем первые карты в руки, делаются первые ставки

dealer_hand.append(cards.pop())
gamer_hand.append(cards.pop())
money_dealer = money_dealer - bid
money_gamer = money_gamer - bid
bank = bid * 2

# print(cards)

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

# функция для подсчета очков на руках игрока/дилера
def cards_count(hand):
    counter = 0
    hand2 = hand.copy() # временный список для подсчета очков, т.к. впрямую сумму не посчитать
    print(hand2)
    for i in range(len(hand2)): # убираем символ масти, для подсчета не нужен
        hand2[i] = hand2[i][1:3]
    for i in range(len(hand)): # заменяем картинки(кроме туза) на 10
        if hand2[i] == 'J' or hand2[i] == 'Q' or hand2[i] == 'K':
            hand2[i] = 10
    for i in range(len(hand2)):
        hand2[i] = int(hand2[i])
    counter = sum(hand2)
    return counter

status()

while True:
    user_input = input('Type your choice, for example bid, or stop: ')

    if user_input == 'bid':
        user_bid = int(input('Input your bid:'))
        money_gamer = money_gamer - user_bid
        bank = bank + user_bid
        gamer_hand.append(cards.pop())
        print(cards_count(gamer_hand))
        status()
        if int(cards_count(gamer_hand)) > 21:
            print('You loose this round')

    elif user_input == 'stop':
        dealer_hand.append(cards.pop())
        print(cards_count(dealer_hand))
        pass

