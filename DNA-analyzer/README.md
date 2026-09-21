# DNA Sequence Analyzer

A Python command-line tool for analyzing DNA sequences. It validates input, computes GC content, finds motifs, and more.

## Features

- Input validation (A, T, C, G, N only)
- Base composition (counts + percentages)
- GC content (overall + sliding window)
- Motif finder with ambiguous base support (N)
- Reverse complement
- Melting temperature (Wallace rule)
- Restriction enzyme site detection
- FASTA file input support

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maryambatool08/bioinformatics-projects.git
   cd bioinformatics-projects/DNA-analyzer
   ``` 

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```                              

## Usage

Run the CLI:

```bash
python dna_analyzer.py
```


## Tech Stack

- **Python 3** — core language
- **pytest** — unit testing framework
- **Git** — version control
- **GitHub** — code hosting

## Running Tests

The project includes 25 tests covering all 8 functions.

```bash
python -m pytest test_dna.py -v
```

## Author

**Maryam Batool**
- GitHub: [@maryambatool08](https://github.com/maryambatool08)
- Repository: [bioinformatics-projects](https://github.com/maryambatool08/bioinformatics-projects)