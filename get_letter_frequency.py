def get_letter_frequence(text):

    # step 1: remove spaces
    text = ''.join(text.split())
    #print(text)

    # step 2: retrieve total charactes in the text
    total_char = len(text)
    #print(total_char)

    # step 3: create dictionary
    my_dict = {key: 0 for key in text}

    # step 4: count the frequency of each letter in text, then update its value in the dictionary
    for element in text:
        for key in my_dict:
            if element == key:
                my_dict[key] += 1
    #print(my_dict)


    # step 5: calculate the percentage of frequency of each letter :
    # using dictionary update() and item() methods
    my_dict.update((key, float(value) / float(total_char) * 100) for key, value in my_dict.items())
    print(my_dict)

get_letter_frequence('Hey bob')