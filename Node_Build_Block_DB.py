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

import sqlite3
# import pyodbc


rpc_connection = AuthServiceProxy(node_main_net, timeout=120)

items = []

start_time = time.time()

# select the required blocks in the range function
for i in range(1, 1000):
    block_time = time.time()

    # TODO add exception hasndling for connectivity errors
    block_hash = rpc_connection.getblockhash(i)
    block_raw = rpc_connection.getblockheader(block_hash)

    t_block = tuple(value for value in block_raw.values())

    # to extract table headers
    # n_block = tuple(key for key in block_raw.keys())
    items.append(t_block)

    print("\nBlock ", i, " time - %.0f ms" % ((time.time() - block_time) * 1000))

# TODO exception handling for file errors
conn = sqlite3.connect(sql_file)
cursor = conn.cursor()
""" TO CREATE TABLE
cursor.execute('''CREATE TABLE Block_headers 
             ('hash', 'confirmations', 'height', 'version', 'versionHex', 'merkleroot', 'time', 'mediantime', 'nonce', 'bits', 'difficulty', 'chainwork', 'nTx', 'previousblockhash', 'nextblockhash')''')
"""
# FIXME 1st block cannot be inserted, there

for item in items:
    print("INSERT INTO Block_headers VALUES "+str(item))
    cursor.execute("INSERT INTO Block_headers VALUES "+str(item))


for row in cursor.execute('SELECT * FROM Block_headers'):
    print(row)


print("\nTotal time --- %.0d seconds" % (time.time() - start_time))

