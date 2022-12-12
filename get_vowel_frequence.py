# Component 3 of main: Retrieves vowel frequence in corpus
def get_vowel_frequence(main_dict):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    # print(vowel_list)

    vowel_dict = {k: v for k, v in main_dict.items() if k in vowel_list}
    # print("vowel dict: ", vowel_dict)
    return vowel_dict


#letter_dictionary = get_letter_frequence("Hey bob")
#get_vowel_frequence(letter_dictionary)