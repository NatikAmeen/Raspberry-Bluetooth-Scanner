import subprocess
import pandas as pd


scan = []
data_index = []
try:
	val = subprocess.Popen(["hcitool", "scan"], stdout=subprocess.PIPE).communicate()[0]
except IOError:
	print ("hcitool utility is not installed... try sudo apt-get install bluez")

val = val.split("\n")

for i in range(len(val)):
	if i == 0:
		pass
	else:
		scan.append(val[i].split("\t"))
print "Scanned & Available Bluetooth Devices are %s" % str(len(scan)-1)
data_columns = ["","ID","Name"]

for i in range(len(scan)):
	data_index.append("Device %s" % str(i+1))
# data_index = ["Device 1", "Device 2",""]
df = pd.DataFrame(scan, data_index, data_columns)
# df.columns("ID", "Name")
print df

df.to_csv("BT_Scanner.csv", sep="\t")

