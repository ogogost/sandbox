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
hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())
hand.append(cards.pop())

print(hand)

for i in range(len(hand)):
    hand[i] = hand[i][1:3]
for i in range(len(hand)):
    if hand[i] == 'J' or hand[i] == 'Q' or hand[i] == 'K':
        hand[i] = 10

print(hand)

