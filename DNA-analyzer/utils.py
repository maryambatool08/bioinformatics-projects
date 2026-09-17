def validate_sequence(seq):
    seq = "".join(seq.split()).upper()

    if seq == "":
        raise ValueError("The sequence is empty.")

    valid_bases = set("ATGCN")
    for position , base in enumerate(seq, start=1):
        if base not in valid_bases:
            raise ValueError(f"Invalid base '{base}' at position {position}.")
    return seq

def count_bases(seq):
    counts = {"A": 0, "T":0, "G":0, "C":0, "N":0}
    for base in seq:
        counts[base] +=1
    return counts

def gc_content(seq):
    counts = count_bases(seq)
    gc = counts["G"] + counts["C"]
    total= len(seq)

    percentage = (gc/total) * 100
    return percentage

def gc_content_window(seq, window_size):
    if window_size > len(seq):
        raise ValueError("window size cannot be larger than the sequence")
    if window_size <= 0:
        raise ValueError("Window size must be greater than 0")

    results = []

    for i in range(len(seq) - window_size + 1):
        window = seq[i: i + window_size]

        gc = gc_content(window)

        results.append(gc)

    return results

def find_motif(seq, motif):
    motif = motif.upper()
    motif_length = len(motif)
    positions = []

    for i in range(len(seq) - motif_length +1):
        window = seq[i: i + motif_length]

        match = True
        for window_char , motif_char in zip(window, motif):
            if motif_char != "N" and window_char != motif_char:
                match = False
                break
        if match:
            positions.append(i + 1)

    return positions

def reverse_complement(seq):
    complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N"}
    reverse_seq = seq[::-1]

    result = "" 
    for base in reverse_seq:
        result += complement_dict[base]

    return result

def melting_temp(seq):
    counts = count_bases(seq)
    at_count = counts["A"] + counts["T"]
    gc_count = counts["G"] + counts["C"]
    tm = 2 * at_count + 4 * gc_count
    return tm

def restriction_sites(seq):
    sites = {
        "EcoRI": "GAATTC",
        "BamHI" : "GGATCC",
        "HindIII" : "AAGCTT",
        "NotI": "GCGGCCGC",
        "PstI": "CTGCAG",
    }
    results = {}
    for enzyme, pattern in sites.items(): 
        positions = find_motif(seq, pattern)
        if positions:
            results[enzyme] = positions

    return results
    
         
if __name__ == "__main__":
    for test_seq in ["atgc", "  gc at gc", "ATXGC", ""]:
        try:
            print(validate_sequence(test_seq))
        except ValueError as e:
            print(f"Error: {e}")

    print(count_bases("ATGCGCTAGC"))
    print(count_bases(""))
    print(gc_content("ATGCTGCG"))
    print(gc_content_window("ATGCGATCGATCGATCGTAGCTAGCTAGCTAGGCTAACGATCG",5))
    print(find_motif("ATGCGCCCGCTATGCGGCCGCC", "ATG"))
    print(find_motif("ATGC", "ANG"))
    print(reverse_complement("ATGC"))
    print(melting_temp("GCGCGCATGC"))
    print(restriction_sites("AAAGAATTCAAAGGATCCAAA"))