# Component 4 of main: Retrieves vowel frequence of every language corpus.
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