from util.DataConversionUtil import DataConversionUtil
from util.LanguageUtil import prepareData
x = DataConversionUtil()
x.stringify_sql_data()
input_lang, output_lang, pairs = prepareData("en", "sql")
print (pairs[:10])
# print (input_lang.word2count)
# print (input_lang.word2index)
# print (prepareData("en", "sql"))