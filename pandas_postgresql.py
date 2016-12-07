import psycopg2
import pandas.io.sql as psql
import numpy as np

# coneccion = pg.connect("dbname=pandas_db user=yully")
#
# dataframe = psql.frame_query("SELECT id_est, nota FROM est_nota", coneccion)
# print(dataframe)

con = psycopg2.connect(dbname='pandas_db', host='localhost', user='yully', password='yully', port='5432')
cur = con.cursor()
cur.execute("SELECT * FROM 'est_nota';")
cur.fetchall()
cur.close()
con.close()

data = np.array(cur.fetchall())
print(data)