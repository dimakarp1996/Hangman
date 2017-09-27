#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:05:42 2017

@author: tcs-user
"""

from Hangman import loss
assert loss(5,7)=='You won!'
assert loss(7,7)=='You lost!'
assert loss(9,7)=='You lost!'