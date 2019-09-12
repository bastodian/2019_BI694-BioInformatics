#!/usr/bin/env python

import sys

BLAST_Results_File = sys.argv[1]

BLAST_Results = open(BLAST_Results_File, 'r')

for Line in BLAST_Results:
	if '#' not in Line:
		LineAsList = Line.rstrip().split('\t')
		PercentIdentity = LineAsList[2]
		if PercentIdentity >= float(95):
			Query = LineAsList[0]
			DbHit = LineAsList[1]
			Evalue = LineAsList[-2]
			sys.stdout.write('%s,%s,%s,%s\n' % (Query, DbHit, Evalue, PercentIdentity))
		else:
			continue
	else:
		continue

BLAST_Results.close()
