from Bio import SeqIO
import re

# http://www.biostars.org/p/66921/

# http://www.biostars.org/p/63506/

# https://paperpile.com/shared/qlNu3j

# https://paperpile.com/shared/kdaV1s


f=open("1.gb","r")

sequences = SeqIO.parse(f, "gb")

snf1 = re.compile("(M|V|L|I|F).R..S...(M|V|L|I|F)")


from prettytable import PrettyTable

x = PrettyTable(["Accession", "Organism", "start", "seq", "end"])

for s in sequences:
    row=[s.id, s.annotations["source"]]    
    m = snf1.search(s.seq.tostring().upper())
    if m:
        print m
        row.extend([m.start(), m.group(0), m.end()])
    else:
        row.extend(["","NO MATCH!",""])
    x.add_row(row)
    break

f.close()

print x
