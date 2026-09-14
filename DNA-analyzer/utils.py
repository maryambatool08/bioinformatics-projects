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

if __name__ == "__main__":
    for test_seq in ["atgc", "  gc at gc", "ATXGC", ""]:
        try:
            print(validate_sequence(test_seq))
        except ValueError as e:
            print (f"Error: {e}")

            print(count_bases("ATGCGCTAGC"))
            print(count_bases(""))
            print(gc_content("ATGCTGCG"))
            print(gc_content_window("ATGCGATCGATCGATCGTAGCTAGCTAGCTAGGCTAACGATCG",5))