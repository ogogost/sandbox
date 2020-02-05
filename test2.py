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

data = ['mA', 'mK', 'm3']
data2 = ['m3', 'mA', 'm2']

print(cards_count(data))
print(cards_count(data2))