#!/usr/bin/python3.2

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) - get_length(dna2) > 0 


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    res = 0
    for i in dna:
        if i == nucleotide:
            res += 1
    return res



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    res = dna1.find(dna2)
    if res == -1:
        return False
    else:
        return True


def is_valid_sequence(dna):
    """ (str) -> bool

     Return True if and only if the DNA sequence is valid 
     (that is, it contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('AFDATCGGC')
    False
    """
    res = True

    for i in dna:
        if i not in 'AGCT':
            res = False
            break
        else:
            continue

    return res

def insert_sequence(dna1, dna2, index):
    """(str, str, int) -> str

    Return the DNA sequence obtained by inserting the second
    DNA sequence into the first DNA sequence at the given index.

    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    """

    res = ''
    len1 = get_length(dna1)
    len2 = get_length(dna2)

    if index == 0:
        res = dna2 + dna1
    elif index == len1:
        res = dna1 + dna2
    else:
        for i in range(index):
            res += dna1[i]

        for item in dna2:
            res += item

        for i in range(index, len1):
            res += dna1[i]

    return res


def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement.

    >>>get_complement('A')
    T
    >>>get_complement('C')
    G
    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'


def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is 
    complementary to the given DNA sequence.

    >>> get_complementary_sequence('ATCG')
    TAGC
    """

    res = ''

    for i in dna:
        res += get_complement(i)

    return res











