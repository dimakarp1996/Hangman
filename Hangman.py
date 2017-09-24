# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:15:34 2017

@author: DK
"""
import random
random.seed(0)
i = random.randint(0, 4)
DICT = ['hello', 'apple', 'orange', 'smell', 'brink']
print("GUESS a LETTER:")
LETTER = DICT[i]
N = len(LETTER)
GUESS = '*'*N

ATTEMPTS = 0
while ATTEMPTS < N:
    INP = input()
    INP = INP[0]
    if INP in LETTER:
        for j in range(N):
            if LETTER[j] == INP:
                GUESS = GUESS[:j]+INP+GUESS[j+1:]
        print('Hit!')
        print('The word: '+GUESS)
        if GUESS == LETTER:
            print('You won!')
            break
    else:
        ATTEMPTS += 1
        print('Nussed, mistake %d out of %d'% (ATTEMPTS, N))
if ATTEMPTS >= N:
    print('You lost!')
