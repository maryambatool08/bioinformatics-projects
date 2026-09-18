from utils import (
    validate_sequence,
    count_bases,
    gc_content,
    gc_content_window,
    find_motif,
    reverse_complement,
    melting_temp,
    restriction_sites,
)

def show_menu():
    print("---- DNA sequence analyzer ----")
    print()
    print("1- Base counts")
    print("2- GC content")
    print("3- GC content window")
    print("4- Find motif")
    print("5- Reverse complement")
    print("6- Melting temperature")
    print("7- Restriction sites")
    print("8- Exit")
    print()

show_menu()

def main():
    seq = input("Enter DNA sequence: ")
    try:
        seq = validate_sequence(seq)
    except ValueError as e:
        print(f"ERROR: {e}")
        return

    while True:
        show_menu()
        choice = input("choose an option (1-8): ")

        if choice == "1":
            counts = count_bases(seq)
            print(counts)

        elif choice == "2":
            print(gc_content(seq))

        elif choice == "3":
            window = int(input("Enter window size: "))
            print(gc_content_window(seq, window))

        elif choice == "4":
            motif = input("Enter motif: ")
            print(find_motif(seq, motif))

        elif choice == "5":
            print(reverse_complement(seq))

        elif choice == "6":
            print(melting_temp(seq))

        elif choice == "7":
            print(restriction_sites(seq))

        elif choice == "8":
            print("Thank you, Goodbye.")
            break

        else:
            print("Invalid choice. Try again")



if __name__ == "__main__":
    main()
