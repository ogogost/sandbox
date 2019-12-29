import random # пригодится для тасования колоды
# создаем колоду для игры
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

hand = []

hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())

game_hand = hand

print(hand)

for i in range(len(hand)):
    hand[i] = hand[i][1:3]
for i in range(len(hand)):
    if hand[i] == 'J' or hand[i] == 'Q' or hand[i] == 'K':
        hand[i] = 10

print('Очистка карт от масти:', hand)

def new(arg):
    hand2 = []  # временный список для подсчета очков, т.к. впрямую сумму не посчитать
    for i in range(len(arg)):  # убираем символ масти, для подсчета не нужен
        hand2[i] = arg[i][1:2]
    for i in range(len(arg)):  # заменяем картинки(кроме туза) на 10
        if arg[i] == 'J' or arg[i] == 'Q' or arg[i] == 'K':
            hand2[i] = 10
    print('hand2=', hand2)
    for i in range(len(hand2)):
        hand2[i] = int(hand2[i])
    counter = sum(hand2)
    hand2.clear()
    return counter

print('Новая функция - ',new(game_hand))