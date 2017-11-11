# import juicy
# import json
import sys
from collections import defaultdict
import pandas as pd
#
# x = juicy.from_json_file("dataset2/review1.json")
# # print(sys.getsizeof(x))
# print("imported")
# # juicy.to_json_file(x, "dataset2/checkin2.json")
#
# # x = juicy.from_file("dataset2/tip2.json")
# # print("Done with from file")
# # print(sys.getsizeof(x))x

import pandas as pd
import sqlite3 as sql

conn = sql.connect("dataset/database.sqlite")
# x = pd.('attribute', conn, schema='sqlite3')
df = pd.read_sql_query("select * from checkin", conn)
print(sys.getsizeof(df))
print(df.shape)
print(df.date.unique())

