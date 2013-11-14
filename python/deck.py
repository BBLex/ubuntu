#!/usr/bin/python

import random

DECK = {}
for number in range(1,14):
    for card in ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS']:
        DECK['%d%s' % (number, card[0])] = {'value': number, 'suite': '%s' % card}
 
print len(DECK)

left = random.choice(list(DECK.keys()))
print '┌──┐\n│ 2♠│\n└──┘'

del DECK [left]
print len(DECK)

right = random.choice(list(DECK.keys()))
print right
del DECK [right]
print len(DECK)
