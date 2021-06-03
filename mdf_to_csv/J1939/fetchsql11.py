import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import mysql.connector
import pandas as pd

style.use('fivethirtyeight')

mydb = mysql.connector.connect(
  host="localhost",
  user="souravkc",
  passwd="pass123",
  database="JdbcDatabase"
)


fig = plt.figure(figsize=(8,5))
ax = plt.subplot2grid((1,1), (0,0))
plt.ion()
cursor = mydb.cursor()

def animate(i):

    df = pd.read_sql("SELECT * FROM jdbcEtable", mydb)
    y = df["timestamps"]
    x = df["EngineSpeed"]
    xs = []
    ys = []
    xs.append(x)
    ys.append(y)
    ax.clear()
    ax.plot(xs,ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
