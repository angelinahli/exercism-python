def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError
    
    hamming_count = 0
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            hamming_count += 1
    return hamming_count
