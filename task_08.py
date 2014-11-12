#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 08 Code"""

from data import FRUIT

SHOPLIST ={
    'Comice Pear': 249,
    'Forelle Pear': 299,
    'Red Pear': 249,
    'Asian Pear': 299,
    'Local Asian Pear': 199,
    'Seckel Pear': 199,
    'Concord Grapes': 499,
    'Green Seedless Grapes': 399,
    }

def get_cost_per_item(SHOPLIST):
    return {k: v * FRUIT[k] for k, v in SHOPLIST.iteritems() if k in FRUIT}

def get_total_cost(SHOPLIST):
    return sum(get_cost_per_item(SHOPLIST).values())
