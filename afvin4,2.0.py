import re

def lees_inhoud():
    """
    Een functie die het volledige bestand inleest en deze scheid op headers en
    sequenties. Het resultaat zijn twee lijsten.
    """
    bestand = "Mus_musculus.GRCm38.pep.all.fa"
    headers = []
    seqs = []
    try:
        bestand = open(bestand)
        seq = ""
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)
    except FileNotFoundError:
        print('Het bestand is niet gevonden')

    return headers, seqs


def eiwitzoeken(headers, seqs):
    cons1 = "MCNSSCMGGMNRR"
    cons2 = 'MCNSSCVGGMNRR'
    for i in range(len(headers)):
        if cons1 in seqs[i] or cons2 in seqs[i]:
            print("Header:", headers[i])
            print(seqs[i])
        else:
             "het consescus is niet gevonden"

def reg(headers,seqs):
    cons2 = r"MCNSSC[MV]GGMNRR"

    for i in range(len(seqs)):
        m = re.search(cons2, seqs[i])
        if m:
            print(headers[i], ('\n'), seqs[i])
def main():
    headers, seqs = lees_inhoud()
    eiwitzoeken(headers, seqs)
    reg(headers,seqs)


main()
