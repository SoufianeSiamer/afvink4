import re
import time


def lees_inhoud():
    """
    Een functie die het volledige bestand inleest en deze scheid op headers en
    sequenties. Het resultaat zijn twee lijsten.
    """
    bestand = "Mus_musculus.GRCm38.dna.toplevel.fa"
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


def regluar(seqs):
    start = time.time()
    for i in range(len(seqs)):
        m = re.search(r'[^ATCG]', seqs[i])
        if m:
            print("er is een verkeerde nucleotide gevonden")
            print(m.group())
        else:
            print("het is DNA")
    einde = time.time()
    print(einde - start)


def ita(seqs):
    """
    Deze functie zoekt doormiddel van iteratie of het DNA puur is.
    Het houdt ook de tijd bij
    """
    print("------------------------------------------------")
    start2 = time.time()
    verif = seqs.count("A") + seqs.count("T") \
        + seqs.count("G") + seqs.count("C")
    # telt de lengte van het bestand.
    verif2 = len(seqs)

    if verif == verif2:
        print("het is weer dnaa")
    else:
        print("het is geen dna")

    einde2 = time.time()
    print(einde2 - start2)


def main():
    headers, seqs = lees_inhoud()
    regluar(seqs)
    ita(seqs)


main()
