#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
from Bio import Entrez
Entrez.email = "bjornjobb@gmail.com"

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
            

gis = Entrez.read( Entrez.esearch( db="protein",term=" ".join(ids), retmax=100 ) )['IdList']




nt_acc = Entrez.read(Entrez.elink(dbfrom="protein", id="255722581", linkname="protein_nuccore"))



pprint(nt_acc[0])

lnks = [link["Id"] for link in nt_acc[0]['LinkSetDb'][0]['Link']]

nt_records = [Entrez.read(Entrez.efetch(db='nucleotide',id=acc,rettype='gb',retmode='xml')) for acc in lnks]

for record in nt_records:
    print record[0]['GBSeq_primary-accession'], record[0]['GBSeq_other-seqids'], record[0]['GBSeq_length']



