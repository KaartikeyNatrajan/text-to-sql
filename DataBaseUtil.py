from __future__ import unicode_literals, print_function, division
from io import open
import unicodedata
import string
import re
import random
import records
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
from lib.table import Table
from lib.query import Query

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class DataBaseUtil:
    def __init__(self, name):
        table_map = {} # key is table_id, value is list of columns
        operators = {

        }

    

def test():
    details = {"sel": 5, "conds": [[3, 0, "SOUTH AUSTRALIA"]], "agg": 0}
    teststr = Query(details["sel"], details["agg"], details["conds"])
    print (teststr);

    db = records.Database('sqlite:///data/train.db')
    conn = db.get_connection()

    table = Table.from_db(conn, "1-1000181-1")
    print (table)
    print (table.query_str(teststr))

    table_data = {"id": "1-1000181-1", "header": [
    "State/territory", "Text/background colour", "Format", "Current slogan", "Current series", "Notes"
    ],
    "types": ["text", "text", "text", "text", "text", "text"], "rows": [["Australian Capital Territory", "blue/white", "Yaa\u00b7nna", "ACT \u00b7 CELEBRATION OF A CENTURY 2013", "YIL\u00b700A", "Slogan screenprinted on plate"], ["New South Wales", "black/yellow", "aa\u00b7nn\u00b7aa", "NEW SOUTH WALES", "BX\u00b799\u00b7HI", "No slogan on current series"], ["New South Wales", "black/white", "aaa\u00b7nna", "NSW", "CPX\u00b712A", "Optional white slimline series"], ["Northern Territory", "ochre/white", "Ca\u00b7nn\u00b7aa", "NT \u00b7 OUTBACK AUSTRALIA", "CB\u00b706\u00b7ZZ", "New series began in June 2011"], ["Queensland", "maroon/white", "nnn\u00b7aaa", "QUEENSLAND \u00b7 SUNSHINE STATE", "999\u00b7TLG", "Slogan embossed on plate"], ["South Australia", "black/white", "Snnn\u00b7aaa", "SOUTH AUSTRALIA", "S000\u00b7AZD", "No slogan on current series"], ["Victoria", "blue/white", "aaa\u00b7nnn", "VICTORIA - THE PLACE TO BE", "ZZZ\u00b7562", "Current series will be exhausted this year"]], "name": "table_1000181_1"}

    table_data = {
        "id" : "1-1000181-1", "header": [
            "State/territory", "Text/background colour", "Format", "Current slogan", "Current series", "Notes"
        ],
        "types" : [],
        "rows" : []
    }

    t = Table(table_data["id"], table_data["header"], table_data["types"], table_data["rows"])
    print (t)
    print (t.query_str(teststr))

test()
    # agg_str = header[query.sel_index]
    # agg_op = Query.agg_ops[query.agg_index]
    # if agg_op:
    #     agg_str = '{}({})'.format(agg_op, agg_str)
    # where_str = ' AND '.join(['{} {} {}'.format(self.header[i], Query.cond_ops[o], v) for i, o, v in query.conditions])
    # return 'SELECT {} FROM {} WHERE {}'.format(agg_str, self.name, where_str)
