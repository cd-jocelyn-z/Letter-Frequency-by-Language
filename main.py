def get_letter_frequence(text):
    # step 1: remove spaces
    text = ''.join(text.split())
    print(text)

    # step 2: create dictionary
    my_dict = {key: 0 for key in text}

    # step 3: count the frequency of each letter in text, then increment its value in the dictionary
    for element in text:
        for key in my_dict:
            if element == key:
                my_dict[key] += 1
    #print(my_dict)

    # step 4: retrieve how many charactes are in the text
    total_char = len(text)
    #print(total_char)

    # step 5: calculate the percentage of frequency of each letter :
    # using update() and item() methods with dictionary
    my_dict.update((key, float(value) / float(total_char) * 100) for key, value in my_dict.items())
    print(my_dict)


get_letter_frequence('hey bob')