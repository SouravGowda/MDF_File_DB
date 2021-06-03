import pandas as pd
import pymysql
import os
import sys,csv
import argparse
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host="localhost",
  user="souravkc",
  passwd="pass123",
  database="JdbcDatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM jdbcEtable "
#adr = ("jdbcEtable", )

mycursor.execute(sql)

myresult = mycursor.fetchall()
print(myresult)
lst=[]
for x in myresult:
	lst.append(x)
#print(lst)

df = pd.DataFrame( [[ij for ij in i] for i in lst] )
#print(df)

#fig = px.line(df, x = df['0'], y = df['1'], title='JdbcDatabase_WheelBasedVehicleSpeed')
#fig.show()
