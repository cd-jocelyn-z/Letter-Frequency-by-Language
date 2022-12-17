# main
import os
import math
# Retrieves letter frequence.
def get_letter_frequence(text):
    text = ''.join(text.split())
    text = text.lower()
    total_char = len(text)

    main_dict = {key: 0 for key in text}

    for element in text:
        for key in main_dict:
            if element == key:
                main_dict[key] += 1

    main_dict.update((key, float(value) / float(total_char) * 100) for key, value in main_dict.items())
    return main_dict


# Retrieves every path to every txt file in the folder corpus, organizes every path in a list.
def get_files_in_coprus():
    list_of_paths = []

    for filename in os.listdir("corpus"):
        if filename.endswith(".txt"):
            file_path = os.path.join(os.getcwd(), "corpus", filename)
            list_of_paths.append(file_path)
   
    return list_of_paths


# Retrieves vowel frequence.
def get_vowel_frequence(main_dict):
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    vowel_dict = {k: v for k, v in main_dict.items() if k in vowel_list}
   
    return vowel_dict


# Retrieves vowel frequence of every language corpus.
def get_corpus_vowel_frequence(list_of_paths):

    for path in list_of_paths:
        with open(path, "r") as file:
            for document in file:
                letter_frequence_dict = get_letter_frequence(document)
                vowel_frequence_dict = get_vowel_frequence(letter_frequence_dict)
            return vowel_frequence_dict


#paths_in_list = get_files_in_coprus()
#print(get_corpus_vowel_frequence(paths_in_list))

def get_csv_file():
    list_of_csv_paths = []

    for filename in os.listdir("corpus"):
        if filename.ensdwith(".csv"):
            file_path = os.path.join(os.getcwd(),"corpus",filename)
            list_of_csv_paths.append(file_path)

    return list_of_csv_paths


#print(get_csv_file())

def lang_freq_dictionary():
    list_of_csv_paths = get_csv_file()

    for file_path in list_of_csv_paths:
        if file_path == "frequences.csv":
            with open(file_path, "r") as file:
                return file.read()


#print(lang_freq_dictionary())

def read_frequencies(freq_file):
    first_line = freq_file.readline().strip("\n")
    header = first_line.split(",")
    language_list = [element for element in header if element != "letter"]

    # initialise lang_dict dictionary
    lang_dict = {key:0 for key in header if key in language_list}
    remaining_lines = freq_file.read().split()
    en_dict = {}
    fr_dict = {}
    de_dict = {}
    es_dict = {}
    it_dict = {}
    for line in remaining_lines:
        item = line.split(",")

        # first column
        letter = item[0]
        # following columns correspond to the position of the language in lang_dict
        value_en = item[1]
        value_fr = item[2]
        value_de = item[3]
        value_es = item[4]
        value_it = item[5]
        # sub-dictionaries
        en_dict[letter] = value_en
        fr_dict[letter] = value_fr
        de_dict[letter] = value_de
        es_dict[letter] = value_es
        it_dict[letter] = value_it
        
    # update values of lang_dict
    lang_dict["en"] = en_dict
    lang_dict["fr"] = fr_dict
    lang_dict["de"] = de_dict
    lang_dict["es"] = es_dict
    lang_dict["it"] = it_dict
    
    return lang_dict

file = open("./corpus/frequences.csv","r")
# print(read_frequencies(file))

def dist_2d(p1,p2):
    distance = ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)

    return math.sqrt(distance)

# print(dist_2d([4,0], [0,3]))
# print(dist_2d([5,2], [1,5]))

def dist(p1,p2):
    distance = 0

    for index in range(len(p1)):
        distance += (p1[index] - p2[index]) ** 2

    return math.sqrt(distance)


# print(dist([4, 0, 3, 6, 1], [0, 3, 0, 5, 0]))


def frequencies_to_vector(lang_dict):
    vowels = ["a","e","i","o","u"]
    frequencies = []

    for vowel in vowels:
        if vowel in lang_dict:
            frequencies.append(lang_dict[vowel])

    return frequencies

file = open("./corpus/frequences.csv")
lg_freq =read_frequencies(file)
f_v = frequencies_to_vector(lg_freq["en"])
# print(f_v)