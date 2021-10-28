#!/usr/bin/env python
import argparse
inFILE = open("/Users/mnpaul47/Desktop/combinedData.txt", "r")

p = argparse.ArgumentParser()
p.add_argument('-p', '--peaks', required=True, type = str, help = "Choose condensed or acylation")
p.add_argument('-o', required=True, type = str, help = "Output")
# Parse the command line
args = p.parse_args()
outFILE = open(args.o, "w")

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
		sample[ID]["sum"] = 0.0
	if (line[1] != "Sample Name") & (line[2] != "NA") &\ (line[0] != "") & (line[1]!="Injection Data File Name"):
		sample[ID]["Date"] = line[2].split(" ")[0]		
		if(args.peaks == "condensed"):
			if (float(line[5]) < 3.2):
				sample[ID]["sum"] = sample[ID]["sum"] +\ float(line[7])
		if(args.peaks == "acylation"):
			if (float(line[5]) > 5.6):
				sample[ID]["sum"] = sample[ID]["sum"] +\ float(line[7])
inFILE.close()

for ID in sample:
	i = sample[ID]["Date"]
	j = sample[ID]["sum"]
	outFILE.write("{}\t{}\t{}".format(ID,i,j))
	outFILE.write("\n")
outFILE.close()