from asammdf import MDF
from mdfreader import mdf 


mdf = MDF('82BF2791_00002501_00002066.mf4')
#speed = mdf.get('CAN_DataFrame.CAN_DataFrame.BusChannel')
#speed.plot()

with MDF(r'82BF2791_00002501_00002066.mf4') as mdf_file:
	mdf_file.export(fmt='csv', filename='filename.csv')
	# speed= mdf_file.get('timestamps')
	# speed.plot()

for signal in mdf_file.select(['CAN_DataFrame.CAN_DataFrame.BusChannel']):
   signal.plot()
