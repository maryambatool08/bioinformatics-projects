import pytest
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

def test_validate_lowercase():
    assert validate_sequence("atgctgc") == "ATGCTGC"

def test_validate_uppercase():
    assert validate_sequence("ATGCTGC") == "ATGCTGC"

def test_validate_withspaces():
    assert validate_sequence("atg c tgc") == "ATGCTGC"


def test_validate_empty_raises():
    with pytest.raises(ValueError):
        validate_sequence("")

def test_validate_invalid_bases_raises():
    with pytest.raises(ValueError):
        validate_sequence("ATGGX")

def test_count_normal_bases():
    result = count_bases("ATGCTGC")
    assert result == {"A": 1, "T": 2, "G": 2, "C": 2, "N": 0}

def test_count_bases_empty():
    result = count_bases("")
    assert result == {"A": 0, "T": 0, "G": 0, "C": 0, "N": 0}

def test_count_bases_same_base_A():
    result = count_bases("AAAAAA")
    assert result == {"A": 6, "T": 0, "G": 0, "C": 0, "N": 0}

def test_count_bases_N_base():
    result = count_bases("GCGCGCNGC")
    assert result == {"A": 0, "T": 0, "G": 4, "C": 4, "N": 1}

def test_count_bases_single():
    result = count_bases("T")
    assert result == {"A": 0, "T": 1, "G": 0, "C": 0, "N": 0}

def test_gc_content_full():
    assert gc_content("GCGC") == 100.0


def test_gc_content_zero():
    assert gc_content("ATAT") == 0.0


def test_gc_content_half():
    assert gc_content("ATGC") == 50.0

def test_gc_content_window_normal():           
    result = gc_content_window("ATGC", 2)       
    assert result == [0.0, 50.0, 100.0]         

def test_gc_content_window_too_large():
    with pytest.raises(ValueError):
        gc_content_window("ATG", 10)

def test_find_motif_normal():
    result = find_motif("ATGCATGC", "ATG")
    assert result == [1,5]

def test_find_motif_no_match():
    result = find_motif("ATGCATGC", "ABC")
    assert result == []

def test_find_motif_wildcard_N():
    result = find_motif("ATGCATGC", "ANG")
    assert result == [1,5]

def test_reverse_complement_normal():
    result = reverse_complement("ATGCTGC")
    assert result == "GCAGCAT"

def test_reverse_complement_with_same_bases():
    result = reverse_complement("AAAAA")
    assert result == "TTTTT"

def test_reverse_complement_with_N():
    result = reverse_complement("ATGCTGN")
    assert result == "NCAGCAT"

def test_melting_temp_with_all_validbases():
    result = melting_temp("ATGCTGC")
    assert result == 22

def test_melting_temp_with_gc_bases():
    result = melting_temp("GCGCCGGC")
    assert result == 32

def test_restriction_sites_with_sites_present():
    result = restriction_sites("AAAGAATTCAAAGGATCCAAA")
    assert result == {"EcoRI": [4], "BamHI": [13]}

def test_restriction_sites_with_no_sites():
    result = restriction_sites("AAAAAA")
    assert result == {}

