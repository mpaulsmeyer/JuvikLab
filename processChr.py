#!/usr/bin/env python
inFILE = open("/Users/mnpaul47/Desktop/combinedData.txt", "r")
outFILE = open("/Users/mnpaul47/Desktop/itemizedData.txt", "w")

#list of anthocyanins in maize
compounds = ["AFZ-Pg35DG",\
"anth-CY",\
"anth-PG",\
"C3DMG",\
"C3G",\
"C3MG",\
"CAT-C35DG",\
"CAT-C35DMG",\
"Pg3DMG",\
"Pg3G",\
"Pg3MG",\
"Pn3DMG",\
"Pn3G",\
"Pn3MG",\
"ukn-?-1",\
"ukn-cond-1",\
"ukn-cy-1",\
"ukn-cy-2",\
"ukn-cy-3",\
"ukn-husk-1",\
"ukn-pg-1",\
"ukn-pg-2",\
"ukn-pg-3",\
"ukn-pg-4",\
"ukn-pgmg-2",\
"ukn-pgmg-3"]

#enzyme assays
# compounds = ["C3DMG",\
# "C3G",\
# "C3MG",\
# "D3DMG",\
# "D3G",\
# "D3MG",\
# "Pg3DMG",\
# "Pg3G",\
# "Pg3MG",\
# "Pn3DMG",\
# "Pn3G"]

sample = {}
for line in inFILE:
	line = line.strip('\n')
	line = line.split("\t")
	if line[3][-2:]==".D":
		ID = line[3]
		sample[ID] = {}
inFILE.close()

inFILE = open("/Users/mnpaul47/Desktop/combinedData.txt", "r")
for line in inFILE:
	line = line.strip('\n')
	line = line.split("\t")
	if line[3][-2:]==".D":
		ID = line[3]
	if (line[1] != "Sample Name") & (line[2] != "NA") & (line[0] != "") & (line[1]!="Injection Data File Name"):
		sample[ID]["Date"] = line[2].split(" ")[0]
		if line[4] != "NA":
			sample[ID][line[4]] = float(line[7])
	if line[5] == "Sum":
		sample[ID]["Total"] = float(line[7])
inFILE.close()

outFILE.write("ID\tDate\t")
for i in compounds:
	outFILE.write("{}\t".format(i))
outFILE.write("Total\n")

for ID in sample:
	tmp = [ID]
	tmp.append(sample[ID]["Date"])
	for i in compounds:
		if i in sample[ID]:
			tmp.append(sample[ID][i])
		else:
			sample[ID][i] = 0
			tmp.append(sample[ID][i])
	tmp.append(sample[ID]["Total"])
	for j in tmp:
		outFILE.write("{}\t".format(j))
	outFILE.write("\n")
outFILE.close()