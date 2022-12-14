# Component 7 of main: language prediction

# 7.1 of main
def frequencies_to_vector(lang_dict):
    vowels = ["a","e","i","o","u"]
    frequencies = []

    for vowel in vowels:
        if vowel in lang_dict:
            frequencies.append(lang_dict[vowel])

    return frequencies

file = open("./corpus/frequences.csv")
lg_freqs = read_frequencies(file) 
f_v=frequencies_to_vector(lg_freqs[’en’])
print(f_v) # affichera [8.167, 12.702, 6.966, 7.507, 2.758]

# Component 7.2 of main
