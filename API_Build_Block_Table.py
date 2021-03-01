# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:58:51 2021

@author: Dino Silva
"""

import requests
import json
import time
from openpyxl import load_workbook


# GET /api/blocks/tip/height	Returns the height of the last block.
def get_last_block_height():

    resp = requests.get("https://mempool.space/api/blocks/tip/height")
    if resp.status_code != 200:
        print("API Error")
    else:
        return int(resp.text)


# GET /api/block-height/:height	Returns the hash of the block currently at :height.
start_time = time.time()
items = []


def get_block_info(start=0, end=11):
    values = []
    block_info = []
    for block in range(start,end):

        block_time = time.time()

        resp = requests.get("https://mempool.space/api/block-height/"+str(block))

        if resp.status_code != 200:
            print("API Error getting block ", block)
        else:

            block_hash = resp.text

            """    
            https://mempool.space/api/block/000000000000000015dc777b3ff2611091336355d3f0ee9766a2cf3be8e4b1ce
            returns:
                {"id":"000000000000000015dc777b3ff2611091336355d3f0ee9766a2cf3be8e4b1ce","height":363366,
                 "version":2,"timestamp":1435766771,"tx_count":494,"size":286494,"weight":1145976,
                 "merkle_root":"9d3cb87bf05ebae366b4262ed5f768ce8c62fc385c3886c9cb097647b04b686c",
                 "previousblockhash":"000000000000000010c545b6fa3ef1f7cf45a2a8760b1ee9f2e89673218207ce",
                 "mediantime":1435763435,"nonce":2892644888,"bits":404111758,"difficulty":49402014931}
            """

            resp = requests.get("https://mempool.space/api/block/"+block_hash)

            if resp.status_code != 200:
                print("API Error getting block hash", block_hash)
            else:

                # convert Json to dict type
                block_raw = json.loads(resp.text)

                # items = [key for key in block_raw]
                # sheet.append(items) only used once to get all field names

                values = [value for value in block_raw.values()]
                sheet.append(values)

        print("block - ", block, "/", end-1, "took %.0f seconds" % (time.time() - block_time))
    return None


if __name__ == '__main__':
    workbook = load_workbook(filename="Block info.xlsx")
    sheet = workbook.active

    get_block_info()

    workbook.save(filename="Block info.xlsx")

    print("Total time --- %.0d seconds ---" % (time.time() - start_time))
