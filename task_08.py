#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 08 Code"""

from data import FRUIT

SHOPLIST = {
    'Comice Pear': 249,
    'Forelle Pear': 299,
    'Red Pear': 249,
    'Asian Pear': 299,
    'Local Asian Pear': 199,
    'Seckel Pear': 199,
    'Concord Grapes': 499,
    'Green Seedless Grapes': 399,
    }


def get_cost_per_item(shoplist):
    """Iterates through the list the return the total cost of each item.

    Args:
        shoplist(dict): A dictionary of items and their quantity.

    Returns:
        dict: A dictionary and the total cost for each item. 

    Examples:

        >>>get_cost_per_item(SHOPLIST)
        {'Forelle Pear': 894.010000001, 'Local Asian Pear': 396.01}

    """
    return {k: v * FRUIT[k] for k, v in shoplist.iteritems() if k in FRUIT}


def get_total_cost(shoplist):
    """Sums the total cost of all items.

    Args:
        shoplist(dict): A dictionary of items and their quantity.

    Returns:
        num(float): Returns the summed total cost of all items in dictionary.

    Examples:

        >>>get_total_cost(SHOPLIST)
        7902.0800000001

    """
    return sum(get_cost_per_item(shoplist).values())
