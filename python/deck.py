#!/usr/bin/python

import random

DECK = {}
for number in range(1,14):
    for card in ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS']:
        DECK['%d%s' % (number, card[0])] = {'value': number, 'suite': '%s' % card}
 
print len(DECK)

x = random.choice(list(DECK.keys()))
print x

