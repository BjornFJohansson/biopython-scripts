#!/usr/bin/python
#

# http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG12
# http://article.gmane.org/gmane.comp.python.bio.general/7974/match=elink
# http://article.gmane.org/gmane.comp.python.bio.general/4495/match=elink
#
# http://www.candidagenome.org/help/code_tables.shtml

from Bio import SeqIO

genes = list(SeqIO.parse("genes.fasta", "fasta"))

for g in genes:
    print g.description

prots_f_genes = [x.seq.translate() for x in genes]

prots_f_gb = list(SeqIO.parse("1.fasta", "fasta"))

print len(prots_f_genes)
print len(prots_f_gb)

for g in prots_f_gb:
    print g.description

'''
from Bio.SeqUtils.CodonUsage import CodonAdaptationIndex
from Bio.SeqUtils.CodonUsageIndices import SharpEcoliIndex
from pprint import pprint


cai = CodonAdaptationIndex()

i= SharpEcoliIndex

pprint(i)


cai.set_cai_index(i)
'''
