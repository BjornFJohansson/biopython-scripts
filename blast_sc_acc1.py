
'''
http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec94

>>> from Bio.Blast import NCBIWWW
>>> from Bio import SeqIO
>>> record = SeqIO.read("m_cold.fasta", format="fasta")
>>> result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
This approach makes more sense if you have your sequence(s) in a non-FASTA file format which you can extract using Bio.SeqIO (see Chapter 5).

Whatever arguments you give the qblast() function, you should get back your results in a handle object (by default in XML format). The next step would be to parse the XML output into Python objects representing the search results (Section 7.3), but you might want to save a local copy of the output file first. I find this especially useful when debugging my code that extracts info from the BLAST results (because re-running the online search is slow and wastes the NCBI computer time).


We need to be a bit careful since we can use result_handle.read() to read the BLAST output only once – calling result_handle.read() again returns an empty string.

>>> save_file = open("my_blast.xml", "w")
>>> save_file.write(result_handle.read())
>>> save_file.close()
>>> result_handle.close()
After doing this, the results are in the file my_blast.xml and the original handle has had all its data extracted (so we closed it). However, the parse function of the BLAST parser (described in 7.3) takes a file-handle-like object, so we can just open the saved file for input:

>>> result_handle = open("my_blast.xml")
'''


# http://biopython.org/DIST/docs/api/Bio.Blast.NCBIWWW-pysrc.html#qblast
# http://www.ncbi.nlm.nih.gov/blast/Doc/node2.html


from Bio.Blast import NCBIWWW

result_handle = NCBIWWW.qblast("blastp", 
                               "nr", 
                               "AAA20073", 
                               hitlist_size=100, 
                               ncbi_gi=True, 
                               alignments = 1, 
                               expect=10.0)

with open("my_blast.xml", "w") as f:
    f.write(result_handle.read())
    
result_handle.close()

from Bio.Blast import NCBIXML

result_handle = open("my_blast.xml")

blast_record = NCBIXML.read(result_handle)

ids = []

for h in blast_record.alignments:
    ids.append(h.accession)

result_handle.close()


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


