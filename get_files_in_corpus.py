# Component 2 of main: Retrieves every path to every txt file in the folder corpus, organizes every path in a list.
import os

def get_files_in_coprus():
    list_of_paths = []
    for filename in os.listdir("corpus"):
        # Populate the list of paths with the path of each text in corpus.
        if filename.endswith(".txt"):
            file_path = os.path.join(os.getcwd(), "corpus", filename)
            list_of_paths.append(file_path)
    #print(list_of_paths)
    return list_of_paths


get_files_in_coprus()