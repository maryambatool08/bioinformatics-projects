def validate_sequence(seq):
    seq = "".join(seq.split()).upper()

    if seq == "":
        raise ValueError("The sequence is empty.")

    valid_bases = set("ATGCN")
    for position , base in enumerate(seq, start=1):
        if base not in valid_bases:
            raise ValueError(f"Invalid base '{base}' at position {position}.")
    return seq

if __name__ == "__main__":
    for test_seq in ["atgc", "  gc at gc", "ATXGC", ""]:
        try:
            print(validate_sequence(test_seq))
        except ValueError as e:
            print (f"Error:{e}")

