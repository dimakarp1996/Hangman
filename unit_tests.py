# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 00:04:52 2017

@author: DK
"""
import mock
from Hangman import check,loss,DICT,get_input,generate_random,generate_init
def test_check():
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(5):
        for word in DICT:
            for yes in alph:
                if yes not in word:
                    assert check(yes, '*****', word, i) == ('*****', word, i+1)
        assert check('e', '*****', "hello", i) == ('*e***', "hello", i)
        assert check('e', '*****', "smell", i) == ('**e**', "smell", i)
        assert check('l', '**e**', "smell", i) == ('**ell', "smell", i)
        assert check('e', '*****', "apple", i) == ('****e', "apple", i)
        assert check('e', '*****', "phone", i) == ('****e', "phone", i)
        assert check('r', '*****', "brink", i) == ('*r***', "brink", i)

def test_loss():
    assert loss(5, 7) == 'You won!'
    assert loss(7, 7) == 'You lost!'
    assert loss(9, 7) == 'You lost!'
def test_generate_random():
    c=generate_random()
    assert c>=0 and c<=4
def test_get_input():
    with mock.patch('__builtin__.raw_input', side_effect='jjjj'):
        assert get_input() == 'j'
def test_generate_init():
    for i in range(5):       
        letter, length, guess, attempts = generate_init(i)
        assert letter == DICT[i]
        assert length == len(letter)
        assert guess == '*'*length
        assert attempts == 0
test_check()
test_loss()
test_generate_random()
test_get_input()
test_generate_init()
print('All tests passed correctly')
