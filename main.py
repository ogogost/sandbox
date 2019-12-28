import random

print('Добро пожаловать в игру БЛЭК ДЖЭК!')
print(' Правила игры: Масти карты: ♥ - червы ♦ - бубны ♣ - трефы ♠ - пики ')
print('Названия карт и их стоимость при подсчете: ')
print('2 - 2, 3 - 3, 4 - 4, 5 - 5, 6 - 6, 7 - 7, 8 - 8,'
      ,'\n','9 - 9, 10 - 10, J - 2, Q - 3, K - 4, A - 1 или 11')

street = []
for i in range(2, 11):
      street.append(i)
street.append('J')
street.append('Q')
street.append('K')
street.append('A')

# print(street)

suits = []
suits.append('♥')
suits.append('♦')
suits.append('♣')
suits.append('♠')
# print(suits)

cards = []

for i in range(len(suits)):
    for j in range(len(street)):
        cards.append(str(suits[i]) + str(street[j]))

# print(cards)

random.shuffle(cards)
print(cards)


print('Game start. Round 1')
dealer_hand = []
gamer_hand = []
money_dealer = 1000
money_gamer = 1000
bank = 0
bid = 10

dealer_hand.append(cards.pop())
gamer_hand.append(cards.pop())
money_dealer = money_dealer - bid
money_gamer = money_gamer - bid
bank = bid * 2

# print(cards)
def money_print():
    print('BANK =', bank, 'Dealer balance=', money_dealer, 'Your balance=', money_gamer)

def cards_status():
    print('Dealer`s cards:', dealer_hand)
    print('Your cards:', gamer_hand)

def cards_count(hand):
    counter = 0

    for i in range(len(hand)):
        if hand[i][1] == 'J':
            hand[i][1] = 10
        elif hand[i][1] == 'Q':
            hand[i][1] = 10
        elif hand[i][1] == 'K':
            hand[i][1] = 10
        elif hand[i][1] == 'A':

    print(hand)

    print(counter)

cards_status()

while True:
    user_input = input('Your choice (bid ... ').split()
    user_command = user_input[0]
    user_bid = int(user_input[1])
    # if user_input[0] == 'bid' and user_input[1] == '':
    #     user_bid = bid
    #     money_print()

    if user_command == 'bid' and user_bid != 0:
        money_gamer = money_gamer - user_bid
        bank = bank + user_bid
        money_print()
        gamer_hand.append(cards.pop())
        cards_count(gamer_hand)
        cards_status()
    # elif user_command == 'pas':
