from Bio import SeqIO
import re

# http://www.biostars.org/p/66921/

# http://www.biostars.org/p/63506/

# https://paperpile.com/shared/qlNu3j

# https://paperpile.com/shared/kdaV1s


f=open("1.gb","r")

sequences = SeqIO.parse(f, "gb")

snf1 = re.compile("((M|V|L|I|F).R..S...(M|V|L|I|F))")


from prettytable import PrettyTable

x = PrettyTable(["Accession", "Organism", "start", "seq", "end"])

for s in sequences:        
    ms = list(snf1.finditer(s.seq.tostring().upper()))
    if ms:
        #x.add_row([s.id, s.annotations["source"], ms[0].start(), ms[0].group(0), ms[0].end()])
        for m in ms[1:]:        
            pass
            #x.add_row(['---"---', '---"---', m.start(), m.group(0), m.end()])            
    else:
        y=[x for x in s.features if x.type=="CDS"].pop().qualifiers["coded_by"]
        print y
        #import sys; sys.exit()       
        #x.add_row([s.id, s.annotations["source"],a,"",""])

f.close()

#print x
