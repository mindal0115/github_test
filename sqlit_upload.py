import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'id':[1,2,3,4],
    'age':[3,4,5,6]
})

print(df)

q = '''

    create table if not exists test1(
        id int,
        age int
    );'''
cursor.execute(q)
conn.commit()

q = 'insert into test1 values(?,?);'
datas = df.items()
print(datas)
cursor.executemany(q,datas)
conn.commit()

df2 = pd.read_sql('select * from test1;',conn)
print(df2)