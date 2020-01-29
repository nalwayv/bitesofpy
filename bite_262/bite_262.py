"""
Bite 262. GC content
"""
from collections import Counter

DNA_SEQUENCES = [
    (
        (  # from https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3
            "tagtgaaagatattcatttcgaaggccttcagcgtgtcgccgttggtgcggccctcctca"
            "gtatgccggtgcgcacaggcgacacggttaatgatgaagatatcagtaataccattcgcg"
            "ctctgtttgctaccggcaactttgaggatgttcgcgtccttcgtgatggtgatacccttc"
            "tggttcaggtaaaagaacgtccgaccattgccagcattactttctccggtaacaaatcgg"
            "tgaaagatgacatgctgaagcaaaacctcgaggcttctggtgtgcgtgtgggcgaatccc"
            "tcgatcgcaccaccattgccgatatcgagaaaggtctggaagacttctactacagcgtcg"
            "gtaaatatagcgccagcgtaaaagctgtcgtgaccccgctgccgcgcaaccgtgttgacc"
            "taaaactggtgttccaggaaggtgtgtcagctgaaatccagcaaattaacattgttggta"
            "accatgctttcaccaccgacgaactgatctctcatttccaactgcgtgacgaagtgccgt"
            "ggtggaacgtggtaggcgatcgtaaataccagaaacagaaactggcgggcgaccttgaaa"
            "ccctgcgcagctactatctggatcgcggttatgcccgtttcaacatcgactctacccagg"
            "tcagtctgacgccagataaaaaaggtatttacgtcacggtgaacatcaccgaaggcgatc"
            "agtacaagctttctggcgttgaagtgagcggcaaccttgccgggcactccgctgaaattg"
            "agcagctgactaagatcgagccgggtgagctgtataacggcaccaaagtgaccaagatgg"
            "aagatgacatcaaaaagcttctcggtcgctatggttatgcctatccgcgcgtacagtcga"
            "tgcccgaaattaacgatgccgacaaaaccgttaaattacgtgtgaacgttgatgcgggta"
            "accgtttctacgtgcgtaagatccgttttgaaggtaacgatacctcgaaagatgccgtcc"
            "tgcgtcgcgaaatgcgtcagatggaaggtgcatggctggggagcgatctggtcgatcagg"
            "gtaaggagcgtctgaatcgtctgggcttctttgaaactgtcgataccgatacccaacgtg"
            "ttccgggtagcccggaccaggttgatgtcgtctacaaggtaaaagagcgcaacaccggta"
            "gcttcaactttggtattggttacggtactgaaagtggcgtgagcttccaggctggtgtgc"),
        51.35,
    ),
    (
        (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
            "gttaatatttatgattcctgaaaagaaatcaatcgcaatcatgaaagaactaagcattgg"
            "aaatacaaagcaaatgctgatgattaatggagttgacgtgaaaaatccattgctgctttt"
            "tttacatggcgggccgggaacgccgcaaatcggatatgttagacattatcaaaaagagct"
            "ggaacagtattttacagtagttcattgggatcagagaggatcggggctttcttattctaa"
            "gcgaatttcgcatcactctatgacaataaatcacttcattaaagatacaatccaagtcac"
            "tcaatggcttttagctcatttttcaaaatcaaaactttacctagccggtcattcttgggg"
            "atcaatactggcgcttcatgtgctgcagcagcgtcctgatttattttacacgtattatgg"
            "aatcagccaggttgttaacccgcaagatgaagaatcaactgcttatcaacatattcgtga"
            "aatttccgaatcaaaaaaagccagcatattatctttccttacacgtttcattggtgctcc"
            "gccttggaagcaggatatccagcaccttatctatcggttttgtgttgagctaaccagggg"
            "aggattcactcaccgtcatcgtcaatctctcgctgtattatttcaaatgcttactggcaa"
            "tgagtatggagtgcggaacatgcacagcttccttaatggattgcgcttcagtaaaaaaca"
            "tttaactgatgagttgtaccggtttaatgcttttacatcagttccttctattaaagtacc"
            "gtgtgttttcatttcagggaaacatgacttaattgttcctgcagaaatatcgaaacagta"
            "ttatcaagaacttgaggcacctgaaaagcgctggtttcaatttgagaattcagctcacac"
            "cccgcatattgaggagccatcattattcgcgaacacattaagtcggcatgcacgacacca"
            "tttatgatagatccttgataaataagaaaaacccctgtataataaaaaaagtgtgcaaat"
            "catgcatattttaaataagtcttgcaacatgcgcctattttctgtataatggtgtatgtt"
            "ggtctttgactgcgatgaagtgagaggttgctgacacacccggccgctttgccatggcaa"
            "ggtgttcaggtttttctcacggagaactgtctaacgtgatgtaggcgaaaaggagggaaa"
            "ataatggcaaaacaaaaaattcgtattcgtttgaaagcatatgatcatagaatccttgat"),
        39.37,
    ),
    (
        (  # from https://www.ncbi.nlm.nih.gov/nuccore/CP010052.1
            # but all As removed, upper and lower case
            "gtttttttgttcctggtctcgctctggctgcttgg"
            "tcgctgctgtgtttgggttgcgtgtccttgctgctttt"
            "tttctggcgggccgggcgccgctcggttgttgctttcggct"
            "ggcgtttttcgtgttcttgggtcggggtcggggctttcttttct"
            "gcgtttcgctcctcttgcttccttcttgtctccgtcc"
            "tctggcttttgctctttttctcctttcctgccggtcttcttgggg"
            "tctctggcgcttctgtgctgcgcgcgtcctgtttttttccgttttgg"
            "tcgccggttgttcccgcgtGGtcctgctttcctttcgtg"
            "tttccgtcgccgcttttctttccttccgtttcttggtgctcc"
            "gccttgggcggttccgccctttcttcggttttgtgttggctccgggg"
            "ggttcctcccgtctcgtctctctcgctgttttttctgcttctggc"
            "tggttgggtgcggctgccgcttcctttggttgcgcttcgtc"
            "tttctgtggttgtccggttttgcttttctcgttccttctttgtcc"
            "gtgtgttttctttcgggCtgcttttgttcctgcgttcgcgt"),
        55.88,
    ),
]


def calculate_gc_content(sequence: str) -> float:
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    chars = []
    for char in sequence:
        cup = char.upper()
        if cup in ['A', 'G', 'C', 'T']:
            chars.append(cup)

    count = Counter(chars)

    a = count.get('A', 0)
    g = count.get('G', 0)
    c = count.get('C', 0)
    t = count.get('T', 0)

    n1 = g + c
    n2 = a + c + g + t

    return round(n1 / n2 * 100, 2)


if __name__ == "__main__":
    for dna, expected in DNA_SEQUENCES:
        result = calculate_gc_content(dna)
        print(result == expected)
