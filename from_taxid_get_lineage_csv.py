#This script will take a list of NCBI taxonomy IDs (one per line) and return a csv file
#where rows are different organisms and columns are taxonomic ranks.
#The input file is assumed to be called taxids.txt
# This script was written by Chris Owen clowen@email.gwu.edu

import sys, csv, time
from Bio import Entrez
 
def get_tax_data(taxid):
    """once we have the taxid, we can fetch the record"""
    search = Entrez.efetch(id = taxid, db = "taxonomy", retmode = "xml")
    return Entrez.read(search)
 
start = time.time()
bacteria_taxonomy = open('pathoscope_lineages.csv', 'w')
header = ['OTU', 'superkingdom', 'kingdom', 'phylum', 'class', 'order', 'suborder', 'family', 'subfamily', 'genus', 'subgenus', 'species', 'no rank']
w = csv.writer(bacteria_taxonomy)
w.writerow(header)
Entrez.email = "castronallar@gmail.com"
if not Entrez.email:
    print "you must add your email address"
    sys.exit(2)
lines = open("taxids.txt").read().splitlines()
for line in lines:
	search = Entrez.efetch(id = str(line), db = "taxonomy", retmode = "xml")
	data = Entrez.read(search)
	lineage = {d['Rank']:d['ScientificName'] for d in data[0]['LineageEx'] if d['Rank'] in ['superkingdom','kingdom','phylum','class','order','suborder','family','subfamily','genus','subgenus','species', 'no rank']}
	line = [str(line)]
	if 'superkingdom' in lineage:
		line.append(lineage['superkingdom'])
	else:
		line.append('NA')
	if 'kingdom' in lineage:
		line.append(lineage['kingdom'])
	else:
		line.append('NA')
	if 'phylum' in lineage:
		line.append(lineage['phylum'])
	else:
		line.append('NA')
	if 'class' in lineage:
		line.append(lineage['class'])
	else:
		line.append('NA')
	if 'order' in lineage:
		line.append(lineage['order'])
	else:
		line.append('NA')
	if 'suborder' in lineage:
		line.append(lineage['suborder'])
	else:
		line.append('NA')
	if 'family' in lineage:
		line.append(lineage['family'])
	else:
		line.append('NA')
	if 'subfamily' in lineage:
		line.append(lineage['subfamily'])
	else:
		line.append('NA')
	if 'genus' in lineage:
		line.append(lineage['genus'])
	else:
		line.append('NA')
	if 'subgenus' in lineage:
		line.append(lineage['subgenus'])
	else:
		line.append('NA')
	if 'species' in lineage:
		line.append(lineage['species'])
	else:
		line.append('NA')
	if 'no rank' in lineage:
		line.append(lineage['no rank'])
	else:
		line.append('NA')
	w.writerow(line)
bacteria_taxonomy.close()
print 'It took', time.time()-start, 'seconds'


