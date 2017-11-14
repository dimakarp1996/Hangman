#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:52:21 2017

@author: tcs-user
"""
from Hangman import check, DICT


def test_check():
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(5):
        for word in DICT:
            for yes in alph:
                if yes not in word:
                    assert check(yes, '*****', word,
                                 i) == ('*****', word, i + 1)
        assert check('e', '*****', "hello", i) == ('*e***', "hello", i)
        assert check('e', '*****', "smell", i) == ('**e**', "smell", i)
        assert check('l', '**e**', "smell", i) == ('**ell', "smell", i)
        assert check('e', '*****', "apple", i) == ('****e', "apple", i)
        assert check('e', '*****', "phone", i) == ('****e', "phone", i)
        assert check('r', '*****', "brink", i) == ('*r***', "brink", i)
