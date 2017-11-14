#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:00:45 2017

@author: tcs-user
"""

import mock
from tests import test_check
from tests import test_loss
from tests import test_gener_random
from tests import test_get_input
from tests import test_gener_init


test_check()
test_loss()
test_gener_random()
test_get_input()
test_gener_init()
print('All tests passed correctly')
