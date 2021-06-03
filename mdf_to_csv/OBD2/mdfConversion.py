from asammdf import MDF

from datetime import datetime
import glob, sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

logfiles=glob.glob("31CB1F25_00000022_00000002.mf4")

DBC=glob.glob("CSS-Electronics-OBD2-v1.3.dbc")

#reading the MDF file 
mdf=MDF.concatenate(logfiles)

#save the binary file for the mf4 
mdf.save('concatenated',overwrite=True)

#Export the mf4 contents to the csv
mdf.export("csv",filename="concatenated")

#extracting the ASCII value file for the CAN log 
mdf_scaled=mdf.extract_can_logging(DBC)

#saving the binary file for the dbc file
mdf_scaled.save("scaled",overwrite=True)

#saving the csv file for dbc
mdf_scaled.export("csv",filename="scaled")

#for signal in mdf.select(['CAN_DataFrame.BusChannel']):
    #signal.plot()

#reading the signals from the dbc file and plotting 
with MDF(r'scaled.mf4') as mdf_file:
    mdf_file.get('S1_PID_11_ThrottlePosition').plot() #S1_PID_0D_VehicleSpeed,S1_PID_11_ThrottlePosition