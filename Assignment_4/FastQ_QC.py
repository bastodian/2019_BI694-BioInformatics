#!/usr/bin/env python

from Bio Import SeqIO
from sys import argv

Fastq = argv[1]
OutFile = argv[2]

GoodSeqs = []
for rec in SeqIO.parse(Fastq, "fastq"):
	PhredScores = rec.letter_annotations['phred_quality']
	if sum(PhredScores) / len(PhredScores) >= int(20):
		GoodSeqs.append(rec)
		
SeqIO.write(GoodSeqs, OutFile, "fastq")
