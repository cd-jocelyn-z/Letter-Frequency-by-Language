# Component 5 of main: reading csv file: creating a dictionary of every language with values containing a dictionary of letter frequence (found in corpus)

def read_frequencies(freq_file):
    # print(freq_file.read())

    # initiating lang_dict keys, which contains the titles of each column in the csv file
    first_line = freq_file.readline().strip('\n')  # remove \n at the end of line
    header = first_line.split(",")
    # print(header)

    # create language list
    language_list = []
    for element in header:
        if element != "letter":
            language_list.append(element)
    # print(language_list)

    # create language dictionary, key is language and value is 0
    lang_dict = {key: 0 for key in header if key in language_list}
    # print(lang_dict)

    # lines after first read line, which contains the letter and its frequence in each language in seperate columns.
    remaining_lines = freq_file.read().split()
    # print(remaining_lines)

    # sub-dictionaries which will be values of lang_dict dictionary
    en_dict = {}
    fr_dict = {}
    de_dict = {}
    es_dict = {}
    it_dict = {}
    for line in remaining_lines:
        item = line.split(",")

        # first column provides the key(letter) of each sub-dictionary
        letter = item[0]

        # following columns correspond to language position in lang_dict dictionary
        value_en = item[1]
        value_fr = item[2]
        value_de = item[3]
        value_es = item[4]
        value_it = item[5]

        # adding values to keys of each sub-dictionary
        en_dict[letter] = value_en
        fr_dict[letter] = value_fr
        de_dict[letter] = value_de
        es_dict[letter] = value_es
        it_dict[letter] = value_it

    # print(en_dict)
    # print(fr_dict)

    # update the values of the lang_dict with sub-dictionaries
    lang_dict["en"] = en_dict
    lang_dict["fr"] = fr_dict
    lang_dict["de"] = de_dict
    lang_dict["es"] = es_dict
    lang_dict["it"] = it_dict
    print(lang_dict)


file = open("./corpus/frequences.csv", "r")
read_frequencies(file)