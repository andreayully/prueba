import psycopg2 as pg
import pandas.io.sql as psql

coneccion = pg.connect("dbname=pandas_db user=yully")

dataframe = psql.frame_query("SELECT id_est, nota FROM est_nota", coneccion)