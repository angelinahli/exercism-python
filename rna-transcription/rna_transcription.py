def to_rna(dna):
    DNAtoRNA = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    new_dna = [DNAtoRNA.get(char, "") for char in dna]
    return "".join(new_dna)