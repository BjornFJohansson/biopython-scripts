#!/usr/bin/python
#

# http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG12
# http://article.gmane.org/gmane.comp.python.bio.general/7974/match=elink
# http://article.gmane.org/gmane.comp.python.bio.general/4495/match=elink
#
#

CodonsDict = {  'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'CTT': 0, 
                'CTC': 0, 'CTA': 0, 'CTG': 0, 'ATT': 0, 'ATC': 0, 
                'ATA': 0, 'ATG': 0, 'GTT': 0, 'GTC': 0, 'GTA': 0, 
                'GTG': 0, 'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0, 
                'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'AAT': 0, 
                'AAC': 0, 'AAA': 0, 'AAG': 0, 'GAT': 0, 'GAC': 0, 
                'GAA': 0, 'GAG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0, 
                'TCG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0, 
                'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0, 'GCT': 0, 
                'GCC': 0, 'GCA': 0, 'GCG': 0, 'TGT': 0, 'TGC': 0, 
                'TGA': 0, 'TGG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0, 
                'CGG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0, 
                'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0}
                


cai_table = '''
UUU 26.1(170666)  UCU 23.5(153557)  UAU 18.8(122728)  UGU  8.1( 52903)
UUC 18.4(120510)  UCC 14.2( 92923)  UAC 14.8( 96596)  UGC  4.8( 31095)
UUA 26.2(170884)  UCA 18.7(122028)  UAA  1.1(  6913)  UGA  0.7(  4447)
UUG 27.2(177573)  UCG  8.6( 55951)  UAG  0.5(  3312)  UGG 10.4( 67789)

CUU 12.3( 80076)  CCU 13.5( 88263)  CAU 13.6( 89007)  CGU  6.4( 41791)
CUC  5.4( 35545)  CCC  6.8( 44309)  CAC  7.8( 50785)  CGC  2.6( 16993)
CUA 13.4( 87619)  CCA 18.3(119641)  CAA 27.3(178251)  CGA  3.0( 19562)
CUG 10.5( 68494)  CCG  5.3( 34597)  CAG 12.1( 79121)  CGG  1.7( 11351)

AUU 30.1(196893)  ACU 20.3(132522)  AAU 35.7(233124)  AGU 14.2( 92466)
AUC 17.2(112176)  ACC 12.7( 83207)  AAC 24.8(162199)  AGC  9.8( 63726)
AUA 17.8(116254)  ACA 17.8(116084)  AAA 41.9(273618)  AGA 21.3(139081)
AUG 20.9(136805)  ACG  8.0( 52045)  AAG 30.8(201361)  AGG  9.2( 60289)

GUU 22.1(144243)  GCU 21.2(138358)  GAU 37.6(245641)  GGU 23.9(156109)
GUC 11.8( 76947)  GCC 12.6( 82357)  GAC 20.2(132048)  GGC  9.8( 63903)
GUA 11.8( 76927)  GCA 16.2(105910)  GAA 45.6(297944)  GGA 10.9( 71216)
GUG 10.8( 70337)  GCG  6.2( 40358)  GAG 19.2(125717)  GGG  6.0( 39359)
'''

index={}

for codon in CodonsDict.keys():
    DNA_codon = codon.replace("T","U")
    i = cai_table.find( DNA_codon )    
    index[codon] = float(cai_table[i+4:i+8])/100

from Bio.SeqUtils.CodonUsage import CodonAdaptationIndex
from Bio.SeqUtils.CodonUsageIndices import SharpEcoliIndex
from pprint import pprint

cai = CodonAdaptationIndex()

cai.set_cai_index(index)

from Bio import SeqIO

genes = list(SeqIO.parse("genes.fasta", "fasta"))

from Bio.SeqUtils import GC

for g in genes:
    print g.id, cai.cai_for_gene( g.seq.tostring() ), GC(g.seq.tostring())



'''
YNR016C 0.20911070449 40.838555655
gi|255722581|ref|XP_002546225.1| 0.226966783311 38.2857142857
gi|241957904|ref|XP_002421671.1| 0.222513610817 37.4607447286
gi|549049991|emb|CCX10916.1| 0.152049928761 54.2791827404
gi|576918395|gb|EUC32592.1| 0.148528956767 55.4438128553
gi|238879558|gb|EEQ43196.1| 0.224132275312 36.9571596244
gi|149247164|ref|XP_001528007.1| 0.202196952275 42.2781878709
gi|330928395|ref|XP_003302241.1| 0.148355188053 55.1900584795
gi|344304298|gb|EGW34547.1| 0.22691991237 38.1188118812
gi|189191818|ref|XP_001932248.1| 0.149314482725 54.9415204678
gi|452002922|gb|EMD95380.1| 0.14944197232 55.3563620463
gi|482807712|gb|EOA84645.1| 0.143459650139 57.1971357592
gi|576928945|gb|EUC42569.1| 0.149338956564 55.225185833
gi|68474502|ref|XP_718624.1| 0.224452297446 36.8691314554
gi|407922072|gb|EKG15200.1| 0.142659853196 58.3113456464




                                        cai             gc
YNR016C                                 0.20911070449   40.838555655
gi|255722581|ref|XP_002546225.1|        0.226966783311  38.2857142857
gi|241957904|ref|XP_002421671.1|        0.222513610817  37.4607447286
gi|238879558|gb|EEQ43196.1|             0.224132275312  36.9571596244
gi|149247164|ref|XP_001528007.1|        0.202196952275  42.2781878709
gi|344304298|gb|EGW34547.1|             0.22691991237   38.1188118812
gi|68474502|ref|XP_718624.1|            0.224452297446  36.8691314554


'''

