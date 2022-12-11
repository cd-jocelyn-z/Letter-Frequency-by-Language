import os
# Creates dictionary of letters and calculates frequency of appearance in text.
def get_letter_frequence(text):
    text = ''.join(text.split())
    total_char = len(text)

    my_dict = {key: 0 for key in text}

    for element in text:
        for key in my_dict:
            if element == key:
                my_dict[key] += 1

    my_dict.update((key, float(value) / float(total_char) * 100) for key, value in my_dict.items())
    print(my_dict)


get_letter_frequence('hey bob')


# Retrieves all the paths to a txt file in corpus and adds them to a list.
def get_files_in_coprus():
    list_of_paths = []

    for filename in os.listdir("corpus"):
        if filename.endswith(".txt"):
            file_path = os.path.join(os.getcwd(), "corpus", filename)
            list_of_paths.append(file_path)

    print(list_of_paths)


get_files_in_coprus()