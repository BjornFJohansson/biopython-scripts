from Bio import SeqIO
import re

# http://www.biostars.org/p/66921/

# http://www.biostars.org/p/63506/

# https://paperpile.com/shared/qlNu3j

# https://paperpile.com/shared/kdaV1s


f=open("1.gb","r")

sequences = SeqIO.parse(f, "gb")

snf1 = re.compile("(M|V|L|I|F).R..S...(R|K|H)")


from prettytable import PrettyTable

x = PrettyTable(["Accession", "Organism", "start", "seq", "end"])

for s in sequences:
    row=[s.id, "organism"]    
    m = snf1.search(s.seq.tostring().upper())
    if m:
        row.extend([m.start(), m.group(0), m.end()])
    else:
        row.extend(["","NO MATCH!",""])
    x.add_row(row)

f.close()

print x



'''
CCX10916.1 Similar to Acetyl-CoA carboxylase; acc. no. P78820 [Pyronema omphalodes CBS 100304]

310 SGRDCSVQRR 320 

    tccggacgtgactgttccgttcagagacga P.omphalodes
    
    S  G  R  D  C  S  V  Q  R  R  
    F  G  R  D  C  S  V  Q  R  R
    *
    TTCGGTAGAGACTGTTCCGTTCAGAGACGT S.cerevisiae











