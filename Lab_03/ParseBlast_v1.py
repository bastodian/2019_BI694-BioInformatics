#!/usr/bin/env python

BLAST_Results = open('Acropora_genes.blastn', 'r')

for Line in BLAST_Results:
	if '#' not in Line:
		LineAsList = Line.rstrip().split('\t')
		PercentIdentity = LineAsList[2]
		if PercentIdentity >= float(95):
			Query = LineAsList[0]
			DbHit = LineAsList[1]
			Evalue = LineAsList[-2]
			print DbHit,',',Query,',',Evalue,',',PercentIdentity
		else:
			continue
	else:
		continue
		
BLAST_Results.close()
