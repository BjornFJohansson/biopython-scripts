#!/usr/bin/env python
# -*- coding: utf-8 -*-

ids   = [   "XP_002546225.1", 
            "XP_002421671.1", 
            "XP_718624.1", 
            "EEQ43196.1", 
            "EGW34547.1", 
            "EMG48936.1", 
            "CCE41856.1", 
            "XP_003866237.1", 
            "XP_001528007.1", 
            "CCX10916.1", 
            "XP_003302241.1", 
            "EUC42569.1", 
            "EKG15200.1", 
            "EMD95380.1", 
            "EOA84645.1", 
            "XP_001932248.1", 
            "EUC32592.1", ]
            

            
'''
from Bio import Entrez
Entrez.email = "bjornjobb@gmail.com"
handle = Entrez.esearch( db= "gene",
                         term=" ".join(ids[0:1]), 
                         retmax=20)                         
giList = Entrez.read(handle)['IdList']
handle.close()
'''
from Bio import Entrez
Entrez.email = "bjornjobb@gmail.com"
ids = [ '255722581', 
        '241957904', '68474502',
        '238879558', '344304298',
        '459371021', '354545130', 
        '448509847', '149247164', 
        '549049991', '330928395', 
        '576928945', '407922072', 
        '452002922', '482807712', 
        '189191818', '576918395']
from pprint import pprint
from Bio import SeqIO
ids = ['55417890', '10697187']
 
result = Entrez.read(Entrez.epost(db="gene", id=",".join(ids))) #, rettype="fasta", retmode="text"))

history_seqs = list(SeqIO.parse(Entrez.efetch(db="nucleotide", 
                                              rettype="fasta", 
                                              retmode="text", 
                                              webenv=result['WebEnv'], 
                                              query_key=result['QueryKey']), 'fasta'))


import sys;sys.exit()
batchSize    = 100
start=0

handle = Entrez.efetch(db="gene", 
                       rettype="gb", 
                       retstart=start, 
                       retmax=batchSize, 
                       webenv=webenv, 
                       query_key=query_key)

print handle.read()








for start in range( 0, len(ids), batchSize ):
  
    print start+1

    handle = Entrez.efetch(db="gene", 
                           rettype="gb", 
                           retstart=start, 
                           retmax=batchSize, 
                           webenv=webenv, 
                           query_key=query_key)

    print handle.read()


import sys;sys.exit()



# http://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EFetch
from Bio import Entrez
Entrez.email = "bjornjobb@gmail.com"

accs=ids
query  = " ".join(accs)
retmax=100
handle = Entrez.esearch( db="protein",term=query,retmax=retmax )
giList = Entrez.read(handle)['IdList']


#handle = Entrez.efetch(db="protein", id=ids, rettype="fasta", retmode="text")
handle = Entrez.epost(db="protein", id=",".join(giList), rettype="fasta", retmode="text")

result = Entrez.read(handle)
search_results=result


webenv,query_key  = search_results["WebEnv"], search_results["QueryKey"]

batchSize    = 100
db="protein"

from Bio import SeqIO

for start in range( 0, len(giList), batchSize ):
  
    print start+1

    handle = Entrez.efetch(db=db, 
                           rettype="gb", 
                           retstart=start, 
                           retmax=batchSize, 
                           webenv=webenv, 
                           query_key=query_key)

    with open("{}.gb".format(start+1), "w") as f:
        f.write(handle.read())
  
  
  #sequences = SeqIO.parse(handle)
  #output_handle = open("example.fasta", "w")
  #SeqIO.write(sequences, output_handle, "fasta")
  
  
  

  



'''
from Bio import Entrez
import time
Entrez.email ="eigtw59tyjrt403@gmail.com"
## We instead upload the list of ID beforehand 
gis=[166706892,431822405,431822402]
request = Entrez.epost("nucleotide",id=",".join(map(str,gis)))
result = Entrez.read(request)
webEnv = result["WebEnv"]
queryKey = result["QueryKey"]
handle = Entrez.efetch(db="nucleotide",retmode="xml", webenv=webEnv, query_key=queryKey)
for r in Entrez.parse(handle):
    # Grab the GI 
    try:
        gi=int([x for x in r['GBSeq_other-seqids'] if "gi" in x][0].split("|")[1])
    except ValueError:
        gi=None
    print ">GI ",gi," "+r["GBSeq_primary-accession"]+" "+r["GBSeq_definition"]+"\n"+r["GBSeq_sequence"][0:20]

'''

'''

import sys
from Bio import Entrez

#define email for entrez login
db           = "nuccore"
Entrez.email = "bjornjobb@gmail.com"
batchSize    = 100
retmax       = 10**9

#load accessions from arguments
if len(sys.argv[1:]) > 1:
  accs = sys.argv[1:]
else: #load accesions from stdin  
  accs = [ l.strip() for l in sys.stdin if l.strip() ]
#first get GI for query accesions
sys.stderr.write( "Fetching %s entries from GenBank: %s\n" % (len(accs), ", ".join(accs[:10])))
query  = " ".join(accs)
handle = Entrez.esearch( db=db,term=query,retmax=retmax )
giList = Entrez.read(handle)['IdList']
sys.stderr.write( "Found %s GI: %s\n" % (len(giList), ", ".join(giList[:10])))
#post NCBI query
search_handle     = Entrez.epost(db=db, id=",".join(giList))
search_results    = Entrez.read(search_handle)
webenv,query_key  = search_results["WebEnv"], search_results["QueryKey"] 
#fecth all results in batch of batchSize entries at once
for start in range( 0,len(giList), batchSize ):
  sys.stderr.write( " %9i" % (start+1,))
  #fetch entries in batch
  handle = Entrez.efetch(db=db, rettype="gb", retstart=start, retmax=batchSize, webenv=webenv, query_key=query_key)
  #print output to stdout
  sys.stdout.write(handle.read())


'''


