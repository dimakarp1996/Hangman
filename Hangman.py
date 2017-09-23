# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:15:34 2017

@author: DK
"""
import random
random.seed(0)
i=random.randint(0,4)
dict=['hello','apple','orange','smell','brink']
print("Guess a letter:")
letter=dict[i]
N=len(letter)
guess='*'*N

num_attempts=0
while(num_attempts<N):
    inp=input()
    inp=inp[0]
    if inp in letter:
        for j in range(N):
            if letter[j]==inp:
                guess=guess[:j]+inp+guess[j+1:]
        print('Hit!')
        print('The word: '+guess)
        if guess==letter:
            print('You won!')
            break
    else:
        num_attempts+=1
        print('Nussed, mistake %d out of %d'% (num_attempts,N))
if num_attempts>=N:
    print('You lost!')
