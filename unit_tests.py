#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:00:45 2017

@author: tcs-user
"""

import mock
import test_check
import test_loss
import test_gener_random
import test_get_input
import test_gener_init

test_check()
test_loss()
test_gener_random()
test_get_input()
test_gener_init()
print('All tests passed correctly')
