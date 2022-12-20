import os
# Component 7 of main: language prediction

# Component 7.1 of main
def frequencies_to_vector(lang_dict):
    vowels = ["a","e","i","o","u"]

    frequencies = [lang_dict[vowel] for vowel in vowels if vowel in lang_dict]
    return frequencies

file = os.path.join(os.curdir,"corpus", "frequences.csv")
lg_freq = read_frequencies(file)
f_v = frequencies_to_vector(lg_freq["en"])
print(f_v) # affichera [8.167, 12.702, 6.966, 7.507, 2.758]

# Component 7.2 of main
