import pandas as pd
import pymysql
import os
import sys,csv
import argparse
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


parser = argparse.ArgumentParser()
#Default localhost for the host server
parser.add_argument('--ip_address', default='localhost', help='IP of the host server')

#Database username
parser.add_argument('--user_name', default="souravkc")

#Password for the database of the username
parser.add_argument('--password', default="pass123")

#Database to be used under same username and database
parser.add_argument('--database', default="ObdDatabase")
args = parser.parse_args()

file_path = os.getcwd()
file_name = "scaled.ChannelGroup_6_OBD2_0x7E8.csv"
actual_file_path = file_path + '/' + file_name
mydb = pymysql.connect(host=args.ip_address,
    user=args.user_name,
    passwd=args.password,
    db=args.database)
cursor = mydb.cursor()
csv_data = pd.read_csv(actual_file_path)


'''
timestamps = list(csv_data.timestamps)
CAN_DataFrame_BusChannel = list(csv_data.CAN_DataFrame_BusChannel)
CAN_DataFrame_IDE = list(csv_data.CAN_DataFrame_IDE)
CAN_DataFrame_DLC = list(csv_data.CAN_DataFrame_DLC)
CAN_DataFrame_DataLength = list(csv_data.CAN_DataFrame_DataLength)
CAN_DataFrame_Dir = list(csv_data.CAN_DataFrame_Dir)
CAN_DataFrame_EDL = list(csv_data.CAN_DataFrame_EDL)
CAN_DataFrame_BRS = list(csv_data.CAN_DataFrame_BRS)
CAN_DataFrame_ID = list(csv_data.CAN_DataFrame_ID)
CAN_DataFrame_DataBytes = list(csv_data.CAN_DataFrame_DataBytes)
'''


timestamps = list(csv_data.timestamps)
VehicleSpeed = list(csv_data.S1_PID_0D_VehicleSpeed)

#CAN_DataFrame_BusChannel,CAN_DataFrame_IDE,CAN_DataFrame_DLC,CAN_DataFrame_DataLength,CAN_DataFrame_Dir,CAN_DataFrame_EDL,CAN_DataFrame_BRS,CAN_DataFrame_ID,CAN_DataFrame_DataBytes):
for time,speed in zip(timestamps,VehicleSpeed):
    query = "INSERT INTO obds1pidtable VALUES (%s, %s);" #table_name

    val = (time,speed)
    # print(val)
    cursor.execute(query,val)
    
#close the connection to the database.
mydb.commit()
cursor.close()

fig = px.line(csv_data, x = timestamps, y = VehicleSpeed, title='ObdDatabase_S1_PID_11_ThrottlePosition')
# fig.show()
