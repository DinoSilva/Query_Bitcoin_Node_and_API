# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 2021

@author: Dino Silva
"""

# import all node configurations to main_net variable
from conf import *

import time

# https://github.com/jgarzik/python-bitcoinrpc
from bitcoinrpc.authproxy import AuthServiceProxy

from openpyxl import load_workbook

rpc_connection = AuthServiceProxy(node_main_net, timeout=120)

items = []

start_time = time.time()

# select the required blocks in the range function
for i in range(100, 1000):
    block_time = time.time()

    # TODO add exception handling for connectivity errors
    block_hash = rpc_connection.getblockhash(i)
    block_raw = rpc_connection.getblockheader(block_hash)

    # items = [value for value in block_raw.values()]
    items.append([value for value in block_raw.values()])

    print("\nBlock ", i, " time - %.0f ms" % ((time.time() - block_time) * 1000))

# TODO exception handling for file errors
workbook = load_workbook(filename=xls_name)
sheet = workbook.active
for item in items:
    sheet.append(item)
workbook.save(filename=xls_name)

print("\nTotal time --- %.0d seconds" % (time.time() - start_time))
