# main
import os
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
    # print("main dict: ", main_dict)
    return main_dict


# Retrieves every path to every txt file in the folder corpus, organizes every path in a list.
def get_files_in_coprus():
    list_of_paths = []

    for filename in os.listdir("corpus"):
        if filename.endswith(".txt"):
            file_path = os.path.join(os.getcwd(), "corpus", filename)
            list_of_paths.append(file_path)
    # print("list of paths: ", list_of_paths)
    return list_of_paths


# Retrieves vowel frequence.
def get_vowel_frequence(main_dict):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    # print(vowel_list)

    vowel_dict = {k: v for k, v in main_dict.items() if k in vowel_list}
    # print("vowel dict: ", vowel_dict)
    return vowel_dict


# Retrieves vowel frequence of every language corpus.
def get_corpus_vowel_frequence(list_of_paths):

    for path in list_of_paths:
        with open(path, "r") as file:
            for document in file:
                x = get_letter_frequence(document)
                y = get_vowel_frequence(x)
            print(path, "letter freq: ", x)
            print(path, "vowel freq: ", y)


paths_in_list = get_files_in_coprus()
get_corpus_vowel_frequence(paths_in_list) 