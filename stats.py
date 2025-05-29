def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(filepath):
    count = 0
    with open(filepath) as f:
        file_contents = f.read()
        words_split = file_contents.split()
        for i in words_split:
            count += 1
    return count

def char_count(filepath):
    split_list = []
    count_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
        for l in file_contents:
            split_list.append(l.lower())
        for i in split_list:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
    return count_dict

def d_list(d):
    list_of_d = []
    for key in d:
        value = d[key]
        new_d = {"char": key, "num": value}
        list_of_d.append(new_d)
    list_of_d.sort(reverse=True, key=sort_on)
    return list_of_d

def sort_on(d):
    return d["num"]   
    