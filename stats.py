def count_words(text):
    words_list = text.split()
    return len(words_list)

def num_of_each_character(text):
    character_dic = {}
    lower_case_text = text.lower()
    for char in lower_case_text:
        if char in character_dic:
            character_dic[char] += 1
        else:
            character_dic[char] = 1
    return character_dic