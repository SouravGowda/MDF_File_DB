from asammdf import MDF, Signal
import numpy as np
import cantools

import pandas as pd


timestamps = np.array([1, 2, 3, 4, 5], dtype=np.float32)

s_uint8 = Signal(samples=np.array([0, 10, 25, 38, 49], dtype=np.uint8),
                 timestamps=timestamps,
                 name='Uint8_Signal',
                 unit='u1')

s_int32 = Signal(samples=np.array([-20, -10, 0, 10, 20], dtype=np.int32),
                 timestamps=timestamps,
                 name='Int32_Signal',
                 unit='i4')

s_float64 = Signal(samples=np.array([-20, -10, 0, 10, 20], dtype=np.float64),
                   timestamps=timestamps,
                   name='Float64_Signal',
                   unit='f8')

# create empty MDf version 4.00 file
with MDF(version='4.10') as mdf4:

    # append the 3 signals to the new file
    signals = [s_uint8, s_int32, s_float64]
    mdf4.append(signals, 'Creating the new MDF file')

    # save new file
    mdf4.save('my_new_file.mf4', overwrite=True)

    # get the float signal
    sig = mdf4.get('Float64_Signal')
    #print(sig)

    # filter some signals from the file
    mdf4 = mdf4.filter(['Int32_Signal', 'Uint8_Signal'])

    # save using zipped transpose deflate blocks
    #mdf4.save('out.mf4', compression=2, overwrite=True)


# reading the MDF file
with MDF(r'82BF2791_00002501_00002066.mf4') as mdf4:

    # filter some signals from the file
    mdf4 = mdf4.filter(['Timestamp','CAN_DataFrame.BusChannel','CAN_DataFrame.BRS'])

    # get the particular column 
    mdfcol = mdf4.get('CAN_DataFrame.BRS')
    #print(mdfcol)

    # saving the filtered columns
    #mdf4.save('out.mf4', compression=2, overwrite=True)

    #Saving the filtered or required columns in the new csv format
    mdf4.export(fmt='csv', filename='filteredMDF.csv')


#reading the dbc file for Messages and Signals
dbcfile = cantools.database.load_file('CSS-Electronics-SAE-J1939-DEMO.dbc')
#print(dbcfile)

    
#Converting the DBC file into xlsx using cantools
#using cammond line
#canconvert CSS-Electronics-SAE-J1939-DEMO.dbc dbccsv.xlsx

#List to append the DataFrame
list = []

#printing the dbc file and appending it to DataFrame
with open(dbcfile , 'r') as file:
    data = file.read()
    #print(data)
    #print(repr(data))

    #appending the dbc file data to empty List
    list.append(data)
    #print(list)

    #pushing the list into the DataFrame using pandas
    df = pd.DataFrame(list)
    #print(df)

    #storing the DataFrame into the CSV file
    df.to_csv("newcsv.csv", sep=' ', encoding='utf-8',index=True)
