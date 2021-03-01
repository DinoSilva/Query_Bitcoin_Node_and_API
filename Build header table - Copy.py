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

#rpc_connection = AuthServiceProxy(node_main_net, timeout=120)
rpc_connection = AuthServiceProxy(node_main_net)


# TODO add code for file errors
workbook = load_workbook(filename="Block_headers_list.xlsx")
sheet = workbook.active

start_time = time.time()

# select the required blocks in the range function
for i in range(1, 100):
    block_time = time.time()

    # TODO add exception handling for connectivity errors
    block_hash = rpc_connection.getblockhash(i)
    block_raw = rpc_connection.getblockheader(block_hash)

    items = [value for value in block_raw.values()]

    sheet.append(items)

    print("\nBlock ", i, " time - %.0f ms" % ((time.time() - block_time) * 1000))

workbook.save(filename="Block_headers_list.xlsx")

print("Total time --- %.0d seconds" % (time.time() - start_time))
