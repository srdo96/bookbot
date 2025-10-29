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

def sort_on(items):
    return items["num"]

def sort_dict(dict_of_char):
    list_of_dict = []
    for c in dict_of_char:
        new_dict = {"char": f"{c}", "num": dict_of_char[c]}
        list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
