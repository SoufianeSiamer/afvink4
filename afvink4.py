def main():
    bestand = "Mus_musculus.GRCm38.pep.all.fa"

    headers, seqs = lees_inhoud(bestand)

    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:", headers[i])
        # check_is_dna = is_dna(seqs[i])
        ###    knipt(seqs[i])
        # else:
        # print("Sequentie is geen DNA. Er is iets fout gegaan.")


def lees_inhoud(bestands_naam):
    """
    Een functie die het volledige bestand inleest en deze scheid op headers en
    sequenties. Het resultaat zijn twee lijsten.
    """

    headers = []
    seqs = []
    try:
        bestand = open(bestands_naam)
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
        if ">" not in headers:
            print("dit is geen fasta bestand")
    except FileNotFoundError:
        print('Het bestand is niet gevonden')

    return headers, seqs

def is_eiwitsequentie():
