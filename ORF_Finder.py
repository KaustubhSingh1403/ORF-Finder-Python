"""
    The code below is to function as an ORF Finder.
    The questions are answered as such ->
    1. Name of ORF with maximum length.
    2. Length of that ORF.
    3. Location of the start codon.
    4. Location of the end codon.
    5. Direction of the ORF.
    6. Length of amino acid encoded.
"""

# The code begins here

min_length_of_orf = 300

def find_longest_orf(code):
    max_orf = ""
    max_length = 0
    for frame in range(3):
        n_code = code[frame : ]
        frames = ""
        for i in range(len(n_code)):
            if i % 3 == 0 and i != 0:
                frames += " "
            frames += n_code[i]

        n_code = frames
        for i in range(0, len(n_code)):
            nn_code = n_code[i : ]
            if "ATG" in nn_code:
                start = nn_code.index("ATG")
                end = min(nn_code.index("TAA"), min(nn_code.index("TAG"), nn_code.index("TGA")))
                if abs(start - end) > max_length and abs(start - end) >= min_length_of_orf and end > start:
                    max_length = abs(start - end)
                    max_orf = nn_code[start : end]
                i = end + 1

    code = code[::-1]
    for frame in range(3):
        n_code = code[frame : ]
        frames = ""
        for i in range(len(n_code)):
            if i % 3 == 0 and i != 0:
                frames += " "
            frames += n_code[i]

        n_code = frames
        for i in range(0, len(n_code)):
            nn_code = n_code[i : ]
            if "ATG" in nn_code:
                start = nn_code.index("ATG")
                end = min(nn_code.index("TAA"), min(nn_code.index("TAG"), nn_code.index("TGA")))
                if abs(start - end) > max_length and abs(start - end) >= min_length_of_orf and end > start:
                    max_length = abs(start - end)
                    max_orf = nn_code[start : end]
                i = end + 1

    return [max_length, max_orf]

# Accession Key = AH002877.2
code = "GTACTGTATTTTCATTCCTCTTAGTTATCTCCCTAAAAAGACTCTGAGTTCCTTGAACACAGGAAGGTGTTTTATTTGATTTTGTTATCCTCAGCATGTAGCAGTGTCTGACACACAGTAGGTGCTCTATCACTGTGAGAGGGATGGATGGATGGGTGGAGTTACAGATGGATAGAAGGATAGATGGAGGGATGGGTGGATGATGGATGGATAGATGGATGGAGGGGGGATGATGAATGGAGGGATAATGAGTGGATGAATGAGGGAATGGGTGGATGGATGGATGGAGGGATGGAGGAACAGATAGATAGATGGAGGGATGGGTGGGTGATGGATGGATAGATGGATGGAGGGAGGGATGATGAATGGAGGGATAATGAATGGATGAATGAGGGGATGGGTGGATGGATGAATGGAGGGATGATGGGTGGATGAATGAATTGAGGGATGGATGGATGAACACATGGATGGATGGATAGATGGATAGATGGAGGAACTGGTGGATTTTGGATGGATGGGTGGATGGATAGATGAATGAATGCCTGGATAGACAAAGAGATGATGGATAGATGAATAGATGAATTAAGGGATGTCGGATAGATGGAGGGATTGATAGATGTTGGATGGATGGGTGGTGGATGGATAGATGAGTGAATGCATGGATAGACAAAGAGATGATGGATGGATGAATTAAGGGATGACAGATGGATGGATGGATGAGTAACTGGATGGACAAGTGGATAAATGGATAGATGGTTGAATACCTGAATGGATTGAAGGAGGATGCATGGATGTAAGATAAGGCTAATCATCCTCCACTCTCTTTCTTTGCAAAACCATCCACCCATTTACTCAATAAACATTTATTCAGTTCAAACTTGGCACAAAGCACCATGTGAGGCCCAAGAGATACGTGGGTTAATAAAACAGAGCTCCTGCCCTCCTGAAAACTGCAAAGAAAGGGGCGTGGCTTCCTGAGTTCAAATCCCAACTCTGCCAGCGACTAGCTGTACATCAGTGATGTTTCCCTACTTTCTCTCAATTAAATAGGGATAATGTCAGTACCTATCACATTGGGAGGTCTTGCGGGGATTAAATGAGTTACCAAATGCCAAGTGTTTGGGACAGGGCCTGGCACCCAGCAAAGTCTCTTGTGAGTGCTGGCTGCTATTATCCTAATGGAGAAGATGGCATGAAAACCAGGAAATAGGATGCCCTTTGGGAAGCAATGCAACAGGAACTTACACAAAGAAAGGAAAGGAGGAAGCAATTAGTGGTGTCTCAAAGGAGTATGTCAAGAAAAACTTTTCAGAGGGAAACCTTTGAGCAGGGTCATGAAAACAGGAGTTCTCTAAGAGATTGTGGACTTGCCTGGGACCACCTGGCTATAAGCACAAAACCATCCGGTTCCTTTCTGTCACTTCTGGCGGGTGAGGGGTCTCTGGCAAAGGGGCAGAAGGTGCGTGAGAGGTTGCGAATGGCCAGGACTGTCCTGGGGCCAGCCGGGGCACCTGGTGGCCAAGCTTAGAAACATGACAGGTCCTCTTGGGAGGGCTGACCGCAGGGAGCGTTGGGTTTCAGGCTGCTGGCGTCGGCTTCTGTGGTGCCCTTTCTGTCGGCTATGAGAGTCCAGACAGTGCCCAACCTCCTCCCCTTCTTTCCACACGCACAACCACCCCACCCCCTGTGGCCTGAGCTGTCCTGCCTCGCCACAATGGCACCTGCCCTAAAATAGCTTCCCATGTGAGGGCTAGAGAAAGGAAAAGATTAGACCCTCCCTGGATGAGAGAGAGAAAGTGAAGGAGGGCAGGGGAGGGGGACAGCGAGCCATTGAGCGATCTTTGTCAAGCATCCCAGAAGGTATAAAAACGCCCTTGGGACCAGGCAGCCTCAAACCCCAGCTGTTGGGGCCAGGACACCCAGTGAGCCCATACTTGCTCTTTTTGTCTTCTTCAGACTGCGCCATGGGGCTCAGCGACGGGGAATGGCAGTTGGTGCTGAACGTCTGGGGGAAGGTGGAGGCTGACATCCCAGGCCATGGGCAGGAAGTCCTCATCAGGTAAAAGGAAGAGATTCCATTGCCCCTGCCACCCACACCCTAAGATCAAGGGTGTTCAGCTGCAAGGTGGAAAGTTTGCACGTGGGGTAGGTCAGTTGGCTGCATTAGTTAAGGGTGTTAGAACGGTCACTTGCTTTTTCTTTGCTTTTAAGTGTCAGGGATTGGACTCAGGAGAGGGAAAGGAGCCATTTCAGGCTGATGTCAGCAGCTGGAGGAAGCATGAGAATCAAACCTAGGATGCTCAGAGTCCACCAGGAAGAATTTTAGAATTATAGACAGTCAGAGTTAACAAGGGTCCTGAGAGATTTTGTACAGCCACCTCTCTTACAGGATGAGGACAAAAAGCGACTGAGAAGGGGAGGACATTTCCAGAGTCACAGCTCATTAAATGCTCTTAAAGTGTCAAGGTTAAGACATGCTCTTCAAGGGGAGACAGATCTGGTTCTAGACTTGGCTCTGCCACTGAGCCACTGGGTGACCTTTGGGAAGGTACNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGAATTCTGAGAATTGCTCAAACCCAGGAGGTGGAGGTTGCGGTGAGCAGAGATTGCACCACTGCACTCCAGCCTGGGCAACAGAGCCAGATTCCATCTCAAAAAAGAAAAACAAAAAACAAAAAAGCCATGAACTCATTTTCAGGTTGAGGAGCTCAGCATCCTGGTTGTGAAATACCCTCCTCATAAAACCCTGGGATGGAGACTACGGGGATCAGGTGCTTCCTTGTGACAACTTCTGGGCATGGTGGCTCAGGGCGCAAACTGGAGTGTGGCCACAATACATACTGTGTACTTTTACAAGGATGTCACAGAGCCTGGGTATCATAAAAGAGGAGCTTTTCAAGGAACTGAAACCATTAGACAGGAGAGAGAGCCCTGGGCAGACAGGGTTGCCCGTGCCAAACATTTCAGCTGTGGCACAAGGGAAAGGGTGGGAGTTATGAAACTGTTCCATTTTGGGTTTAGGTCTGGGCTCTGCCGCTAGCTAGCCAAGTGACCTTGGCCACTTATCTCTGTGGTCTTCCATGAGTAAAAGGCGGAAACTCACTCCTACCCAGAGGGCAGGTCTGACTCCCTTTAACCAGCACCCACCTGCTCACAGCAGGAAGGACTGAGGTCTAAAGCTGGAGGTGGGCAGGAAGGACTGAGGTCTAAAGCTGGAGGTGGGCAGGAAGGACCGAGGTCTAAAGCTGGAGGTGGGCAGGAAGGACCGAGGTCTAAAGCTGGAGGTGGCTGCTCAGAGTCCCAGCAGAGGCCTCTGGGGCACCTCACTGAGTGCCTGGCAGGAGTGGGTGCCTGTCTCAGGGCTGGGTTGAGTTGCTCCCACCAGGACCCTTCGTCATCTGCACAGTGAGGGGACTGGGAGGTTCAGAGAGTCACAGCTTGGGCTCAAAACAAGCAAGAGGTTTCTGAGTGTGAGGATTGCTCTGGAGTGGAATGGCCCTCACAGGTAGGAGTGAGCCTCCTGTAGCTAGAGGTATTTAAGCAGCTGAAGGACAATCCCTGGGCAGGAAGCTGCAGAGATGGTCGCAGCGTGGACTAGAACTGCTGTTTTGGTCACTCAGACCTCATTCCAGCCTGGCTTCTCTGGACAGCACCCCTGCAATAGTGAGCTGGTGACTTTACGCCTCAGAACCTCGGTTTCTACATCTGTAAAATGGGAATTATATGACACTCACTATGTGCCAGACACCCTGTTGGTACATAGCACACACTATCTCACTTAATCCTTCAAGTAGGGACAAGTTATCCCCATCCCTTATATGAGGAAGCTGAGGCACAGAGAGGTGAAGTGAATGGCCCAAGGTCACACAGCTGGGAAGACAGGGAGCTAAACTTGAACTCTAGTCTGGCTGCCCCCAGACCTCACACCGCACCTCCCATGCCGACTCCAGCCTTCCCTGTGCCCACAGGCTCTTTAAGGGTCACCCAGAGACTCTGGAGAAGTTTGACAAGTTCAAGCACCTGAAGTCAGAGGACGAGATGAAGGCATCTGAGGACTTAAAGAAGCATGGTGCCACTGTGCTCACCGCCCTGGGTGGCATCCTTAAGAAGAAGGGGCATCATGAGGCAGAGATTAAGCCCCTGGCACAGTCGCATGCCACCAAGCACAAGATCCCCGTGAAGTACCTGGAGGTAGGAGGCAGAGCCTGGGCAGGTGGGAGGATGCGGGGAAGGCCTCGGGTGGGGCAATGGGATCTGGGTTCGAGTCCAAGCTCAGCCACTAACTTGTGGGATGACCTATGCCACTCTTCTCTGTGCCCCAGGTTTCTCATTTGTAAAGGGGACTGCCACCCACTTTGCCTTCCTCCTGGGATTGTTGAGAATGAACACATTTAGCATTTTTAATTTAGTATGCCAAATTCACATCTTATTACCAAAGAGGAAAGGGAGAGGGGATATTGGGTGCAAAATTTGCATCCTCTCCATGGGTAGGTACCATTATCATATCCACTTGATAGATGGGGAAACTGAGGCTCACAGAGGTTAAGCAGCTTGTCCACGGTCACAGGAGGTGGATAATGGCAGAGCCAAGATTCAAACGCAGGTCTCTATTACTACAGAACCCCAGCCCCTAACTGCTGTGCCACTGGGAGTCTGGTACATGCAGGACTTATGTGGCAGGAGCTCAGCAAGTGGGGCTCAATTTGGGGTGGGGGTGACCAGCAGGCTGGCTCTATTGGTTCCAGCATCTTCACAGATGAAGAGACAGGACCTCGGTTTCCAGCACAAGCAATTGGTTTGAACCTCCTGAGATGGGTTGGAAAGTTGGGTGGATCAGGGTTGGGGGCAGGAGCCTGGGCTTCAGGTTGTGTGTCTATAACTGGTGGGAGGAGGCGATTTGGGGAGAGGAGGGAGCTGGGGATGAAGGACCACAGGGACAGGTGCATCCCCCGAGGGTAGAAACAGCAGGAAGTCTGGTGCAGCCATGAGGATTAGGATGTGGTGATAGCTACCCGCTGGGATGGGCCACAGTGAGCATTTGCTGCCATGCCTAGCACATGCATCCATCCTCAAAGTTGCCTCATGGCCAAAATGACTGCAAGAGCTCCAGCCAGCTCTTCTATATTCCCAACTGGAAGCAGGAGAAAGAGAGGAATGCTCTCTTTTGAGGAGTTTAAGGAGTCCCAGAAATCTCATCCAACAATTTTATTTACATCTCATTGGCCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGAGCTCTCACCTGGTTTCAGTGGGGTCTACATCCTGATGGAGTGGAGGGGGCTGTGAGTAAGAGCGTGGGCTCCGGAGCCGGCCCTCCTGGGTCCAAATGTCCCTTCCATTCAACCTCCCCTCGCCTCAGTTTCTGCATCTGTAAATCGAGGGCAGTTGTAGTATCTATCTCACAGTGGTTGTGGGGATCAAAGGGGTTCATCCGTGGAGATCACACAGACTCTCACCTGGTGCCTAGCAAGTGCTCAATACACGGTCCTGGAATAAAGAGAAGGTAGGAGGACAACTGACTCCCATCTGGCCCCTGGCTTGTCCCACCCTGGTGACCATTTTCTCTCCTCACCCTCCCTGCAGTTCATCTCGGAATGCATCATCCAGGTTCTGCAGAGCAAGCATCCCGGGGACTTTGGTGCTGATGCCGAGGGGGCCATGAACAAGGCCCTGGAGCTGTTCCGGAAGGACATGGCCTCCAACTACAAGGAGCTGGGCTTCCAGGGCTAGGCCCCTGCCGCTCCCACCCCCACCCATCTGGGCCCCGGGTTCAAGAGAGAGCGGGGTCTGATCTCGTGTAGCCATATAGAGTTTGCTTCTGAGTGTCTGCTTTGTTTAGTAGAGGTGGGCAGGAGGAGCTGAGGGGCTGGGGCTGGGGTGTTGAAGTTGGCTTTGCATGCCCAGCGATGCGCCTCCCTGTGGGATGTCATCACCCTGGGAACCGGGAGTGGCCCTTGGCTCACTGTGTTCTGCATGGTTTGGATCTGAATTAATTGTCCTTTCTTCTAAATCCCAACCGAACTTCTTCCAACCTCCAAACTGGCTGTAACCCCAAATCCAAGCCATTAACTACACCTGACAGTAGCAATTGTCTGATTAATCACTGGCCCCTTGAAGACAGCAGAATGTCCCTTTGCAATGAGGAGGAGATCTGGGCTGGGCGGGCCAGCTGGGGAAGCATTTGACTATCTGGAACTTGTGTGTGCCTCCTCAGGTATGGCAGTGACTCACCTGGTTTTAATAAAACAACCTGCAACATCTCAGTTTCTGCCTGGCATTTTTCATCTCCTAGAGTAAATGATGCCCCCACCAGCACCAGCATCAAGGAAGAAATGGGAGGAAGGCAGACCCTGGGCTTGTGTGTGCAGAGAGCCTCAGGAAAGAGGAGAAGGGGAGGAGGAAAGGCAGGAGGGTGAGAGGGACAGGAGCCCACCCTCCCTGGGCCACCGCTCAGAGGCAGGCCCAGTGCAGGGCATGGGGAAATGGAAGGGACAGGCTTGGCCCCAGCCTTGGGAGCACCTTCTCTTCGGGGGAGGTGGGAGGCAGCGAACAGACCTCTGCAATACGAGGAGAGAGTGACAGGTGCGCCAGGCTGTGGGAACCCAGAGGAGAGGGGAAGCCATCATCATCATGGCTGCAATACCTTCAGTAACGTGGGAAGGTCACCCTGCTAGTAAGTGGCAGAGCTGGGACTC"

# print("The length of the code is", len(code))

# frames = ""
# for i in range(len(code)):
#     if i % 3 == 0 and i != 0:
#         frames += " "
#     frames += code[i]

# frames = frames.split(" ")
# print(frames)

print(find_longest_orf(code))
