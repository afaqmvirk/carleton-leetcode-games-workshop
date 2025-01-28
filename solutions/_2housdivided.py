from collections import Counter

def house_divided(s, t):
    # Helper function to generate all mutations of `s` with exactly one nucleotide difference
    def generate_mutations(s):
        mutations = set()
        nucleotides = {'A', 'T', 'C', 'G'}
        for i in range(len(s)):
            for nucleotide in nucleotides - {s[i]}:
                mutation = s[:i] + nucleotide + s[i+1:]
                mutations.add(mutation)
        return mutations

    # Generate all mutations of `s`
    mutations = generate_mutations(s)
    
    # Collect subsequences of `t` of the same length as `s`
    subsequences = [t[i:i+len(s)] for i in range(len(t) - len(s) + 1)]
    
    # Count occurrences of all subsequences in `t`
    subseq_counts = Counter(subsequences)
    
    # Filter mutations that appear more than once in `t`
    valid_mutations = [mut for mut in mutations if subseq_counts[mut] > 1]
    
    # Output the results
    valid_mutations.sort()
    return len(valid_mutations), valid_mutations

# Function to format and print the output as specified
def formatted_output(count, subsequences):
    print(count)
    for subseq in subsequences:
        print(subseq)

# Example input
s_example = "TGATG"
t_example = "TGCTGCTGTTGTTG"

# Run the function and display the result
result_count, result_list = house_divided(s_example, t_example)
formatted_output(result_count, result_list)
