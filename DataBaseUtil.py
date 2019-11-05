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

    def addSentence(self, sentence):
        for word in sentence.split(' '):
            self.addWord(word)

    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2count[word] = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2count[word] += 1


def readLangs():
    print("Reading lines...")


    lines_en = open('train_en.txt', encoding='utf-8').\
        read().strip().split('\n')

    lines_sql = open('train_sql.txt', encoding='utf-8').\
        read().strip().split('\n')


    # Split every line into pairs and normalize
    pairs = []
    for i in range(len(lines_en)):
    	tokens_en = normalizeString(lines_en[i])
    	tokens_sql = normalizeString(lines_sql[i])
    	pairs.append([tokens_en, tokens_sql])

    # Reverse pairs, make Lang instances
    input_lang = LanguageUtil(lang1)
    output_lang = LanguageUtil(lang2)	

    return input_lang, output_lang, pairs

def prepareData(lang1, lang2):
    # input_lang, output_lang, pairs = readLangs(lang1, lang2)
    # print("Read %s sentence pairs" % len(pairs))
    # print("Trimmed to %s sentence pairs" % len(pairs))
    # print("Counting words...")
    # for pair in pairs:
    #     input_lang.addSentence(pair[0])
    #     output_lang.addSentence(pair[1])
    # print("Counted words:")
    # print(input_lang.name, input_lang.n_words)
    # print(output_lang.name, output_lang.n_words)
    # return input_lang, output_lang, pairs
    readLangs()


# prepareData()
# print(random.choice(pairs))

def test():
    details = {"sel": 5, "conds": [[3, 0, "SOUTH AUSTRALIA"]], "agg": 0}
    teststr = Query(details["sel"], details["agg"], details["conds"])
    print (teststr);

    db = records.Database('sqlite:///D:/PersonalDocs/UMass/Study Material/NLP/project/WikiSQL/data/train.db')
    conn = db.get_connection()

    table = Table.from_db(conn, "1-1000181-1")
    print (table)
    print (table.query_str(teststr))

test()
    # agg_str = header[query.sel_index]
    # agg_op = Query.agg_ops[query.agg_index]
    # if agg_op:
    #     agg_str = '{}({})'.format(agg_op, agg_str)
    # where_str = ' AND '.join(['{} {} {}'.format(self.header[i], Query.cond_ops[o], v) for i, o, v in query.conditions])
    # return 'SELECT {} FROM {} WHERE {}'.format(agg_str, self.name, where_str)
