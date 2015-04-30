#!/usr/bin/python
#

# http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG12
# http://article.gmane.org/gmane.comp.python.bio.general/7974/match=elink
# http://article.gmane.org/gmane.comp.python.bio.general/4495/match=elink
#
#
    

cai_table = '''

Gly	GGG	17673	6.05	0.12
Gly	GGA	32723	11.20	0.23
Gly	GGT	66198	22.66	0.46
Gly	GGC	28522	9.76	0.20
	
Glu	GAG	57046	19.52	0.30
Glu	GAA	133737	45.77	0.70
Asp	GAT	111276	38.08	0.65
Asp	GAC	59389	20.33	0.35
	
Val	GTG	31266	10.70	0.19
Val	GTA	35397	12.11	0.22
Val	GTT	62735	21.47	0.39
Val	GTC	32738	11.20	0.20
	
Ala	GCG	17988	6.16	0.11
Ala	GCA	47538	16.27	0.30
Ala	GCT	59300	20.29	0.37
Ala	GCC	35410	12.12	0.22
	
Arg	AGG	27561	9.43	0.21
Arg	AGA	61537	21.06	0.48
Ser	AGT	42657	14.60	0.16
Ser	AGC	29003	9.93	0.11
	
Lys	AAG	89004	30.46	0.42
Lys	AAA	125276	42.87	0.58
Asn	AAT	107428	36.77	0.60
Asn	AAC	72290	24.74	0.40
	
Met	ATG	60426	20.68	1.00
Ile	ATA	53518	18.32	0.28
Ile	ATT	88351	30.24	0.46
Ile	ATC	49535	16.95	0.26
	
Thr	ACG	23766	8.13	0.14
Thr	ACA	53147	18.19	0.31
Thr	ACT	59096	20.23	0.34
Thr	ACC	36395	12.46	0.21
	
Trp	TGG	30179	10.33	1.00
End	TGA	1863	0.64	0.31
Cys	TGT	22879	7.83	0.62
Cys	TGC	13811	4.73	0.38
	
End	TAG	1349	0.46	0.22
End	TAA	2798	0.96	0.47
Tyr	TAT	55965	19.15	0.57
Tyr	TAC	42551	14.56	0.43
	
Leu	TTG	77261	26.44	0.28
Leu	TTA	77615	26.56	0.28
Phe	TTT	76557	26.20	0.59
Phe	TTC	52201	17.87	0.41
	
Ser	TCG	25381	8.69	0.10
Ser	TCA	55725	19.07	0.21
Ser	TCT	68207	23.34	0.26
Ser	TCC	40972	14.02	0.16
	
Arg	CGG	5299	1.81	0.04
Arg	CGA	9050	3.10	0.07
Arg	CGT	18272	6.25	0.14
Arg	CGC	7644	2.62	0.06
	
Gln	CAG	36222	12.40	0.31
Gln	CAA	79131	27.08	0.69
His	CAT	40577	13.89	0.64
His	CAC	22559	7.72	0.36
	
Leu	CTG	31054	10.63	0.11
Leu	CTA	39440	13.50	0.14
Leu	CTT	35753	12.24	0.13
Leu	CTC	16086	5.51	0.06
	
Pro	CCG	15778	5.40	0.12
Pro	CCA	51993	17.79	0.41
Pro	CCT	39685	13.58	0.31
Pro	CCC	20139	6.89	0.16'''
import csv

index = {}
for aa, cn, n1,n2, f in csv.reader([x for x in cai_table.splitlines() if x.strip()], delimiter='\t'):
    index[cn] = float(n2)

from Bio.SeqUtils.CodonUsage import CodonAdaptationIndex
from Bio.SeqUtils.CodonUsageIndices import SharpEcoliIndex
from pprint import pprint


cai = CodonAdaptationIndex()

cai.set_cai_index(index)

from Bio import SeqIO

genes = list(SeqIO.parse("genes.fasta", "fasta"))

from Bio.SeqUtils import GC

for g in genes:
    print g.id, "         ",cai.cai_for_gene( g.seq.tostring() )#, GC(g.seq.tostring())


