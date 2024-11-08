def count_values(words_list):
    words_list_dict = {}
    for i in words_list:
        c = words_list.count(i)
        words_list_dict.setdefault(i,c)
    return words_list_dict


line_list = []
def line(line):
    if not line:
        return line
    elif line:
        line_list.append(line[0])
        for i in range(1, len(line)-1):
            if line[i] != line_list[-1]:
             line_list.append(line[i])
        return ''.join(line_list)



def unique_elms(list_one, list_two):
    set_one = set(list_one)
    set_two = set(list_two)
    unique_elms = set_one^set_two
    return list(unique_elms)

