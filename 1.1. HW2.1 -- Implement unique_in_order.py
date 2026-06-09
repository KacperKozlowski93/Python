

def unique_in_order(text):
    new_list_text = []
    for i in range(len(text)):
        if text[i] != text[i - 1]:
            new_list_text.append(text[i])

    return new_list_text


print(unique_in_order("1123455"))