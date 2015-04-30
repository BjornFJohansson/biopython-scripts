#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://armchairbiology.blogspot.pt/2013/02/surely-this-has-been-done-already.html
#http://seqanswers.com/forums/archive/index.php/t-26189.html

from pprint import pprint
from Bio import Entrez
Entrez.email = "bjornjobb@gmail.com"

'''
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

accs = []

for gi in gis:
    r =  Entrez.read( Entrez.elink(dbfrom = "protein", id = gi, linkname="protein_nuccore") )    
    nt_accs = [link["Id"] for link in r[0]['LinkSetDb'][0]['Link']]   
    docsums = [Entrez.read(Entrez.efetch(   db='nucleotide',
                                            id=acc,
                                            rettype='docsum',
                                            retmode='xml')) for acc in nt_accs]    
    Lengths = [(x[0]["Length"],x[0]["Gi"],) for x in docsums]    
    accs.append( str(sorted(Lengths)[0][1]) )
    

'''

accs = [str(x) for x in [255722580, 241957903, 68474501, 
92090995, 344303403, 459371019, 354544723, 448509846, 
149247163, 549049989, 330928394, 576928943, 407922027, 
452002070, 482807555, 189191817, 576918390]]

accs = ["255722580", "241957903"]

result = Entrez.read(Entrez.epost(db="nucleotide", id=",".join(accs)))


handle = Entrez.efetch( db="nucleotide", 
                        rettype="gb", 
                        retmode="text",
                        retmax= len(accs),
                        webenv=result['WebEnv'], 
                        query_key=result['QueryKey'])
                                      

pprint(handle.read())





'''
   [{'Status': 'live', 'Comment': '  ',
    'Caption': 'XM_002546179',
      'Title': 'Candida tropicalis MYA-3404 acetyl-CoA carboxylase, mRNA',
  CreateDate': '2009/08/11', 
      'Extra': 'gi|255722580|ref|XM_002546179.1||gnl|REF_WGS:AAFN|mrna_CTRT_01007[255722580]',
      'TaxId': 294747, 
 'ReplacedBy': '', 
      u'Item': [], 
     'Length': 6825, 
      'Flags': 512, 
 'UpdateDate': '2009/08/11', 
        u'Id': '255722580', 
         'Gi': 255722580}]
'''



#with open("ACC_genes_wo_SNF1_site.txt", "w") as f:
#    f.write(handle.read())



