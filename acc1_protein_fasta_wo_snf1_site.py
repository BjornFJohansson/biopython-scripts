#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://armchairbiology.blogspot.pt/2013/02/surely-this-has-been-done-already.html
#http://seqanswers.com/forums/archive/index.php/t-26189.html

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

handle = Entrez.epost(db="protein", id=",".join(gis))
results = Entrez.read(handle)

from Bio import SeqIO

handle = Entrez.efetch(db="protein", 
                       rettype="fasta", 
                       webenv=results["WebEnv"], 
                       query_key=results["QueryKey"])

with open("1.fasta", "w") as f:
    f.write(handle.read())
