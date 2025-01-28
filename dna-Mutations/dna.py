from collections import Counter

def generate_one_mutation_sequences(s):
    """
    Generate all possible sequences that are one mutation away from s.
    """
    mutations = []
    bases = {'A', 'C', 'G', 'T'}
    for i in range(len(s)):
        for base in bases:
            if base != s[i]:  # Only mutate if the base is different
                mutated = s[:i] + base + s[i+1:]
                mutations.append(mutated)
    return set(mutations)

def find_repeated_one_mutation_sequences(s, t):
    """
    Find the number of repeated sequences in t that are one mutation away from s.
    """
    k = len(s)
    one_mutation_sequences = generate_one_mutation_sequences(s)
    
    # Extract all substrings of length k from t
    substring_counts = Counter(t[i:i+k] for i in range(len(t) - k + 1))
    
    # Find the sequences that are mutated versions of s and are repeated
    repeated_count = 0
    repeated_sequences = []
    
    for seq, count in substring_counts.items():
        if seq in one_mutation_sequences and count > 1:
            repeated_count += 1
            repeated_sequences.append(seq)
    
    return repeated_count, repeated_sequences

# Example usage
if __name__ == "__main__":
    s = "TGTCTTG"
    t = "TGCTGCTGTTGTGCTGCTGTTGTTCTGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTGCTGCTGTTGTTCTGGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTTCTGATGCTGACTAGCATGCTAGTGCTGGTGCTGCTGTTGTTCTGGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTGCTGCTGTTTGAGAGCTTGGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTATCTGCATCGTGACATCTTGTATCTGCTGGTGCTGCTGTTGTTCTGGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTGCTGCTGTTGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTATCTGCATCGTATGAGAGCTTGTCCTAGTGCTGGTGCTGCTGTTGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTATGCTGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTGCTGCTGTTGTTCTGATGCTGACTAGCATGCTAGCTAGTGCTGGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTGTATCTGCATCGTATCTCTTATGACGTTGTGCTGCTGTTGTTG"
    
    result_count, result_sequences = find_repeated_one_mutation_sequences(s, t)
    print("Number of repeated mutated sequences:", result_count)
    print("Repeated mutated sequences:", result_sequences)
