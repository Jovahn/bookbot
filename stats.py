def get_book_text(f):
    #book_text = f.read()
    word_count = len(f.split()) 

    #print(f)
    final_word_count = (f"Found {word_count} total words") 
    return final_word_count

def character_count(f):
    #bk_text = f.read() 
    letters_in_book = list(f.lower())
    #print(letters_in_book)


    final_characters = {} 
    for q in letters_in_book:
        if q in final_characters:
            final_characters[q] += 1
        else:
            final_characters[q] = 1 
        #print(f"key = {q} : value = {final_characters[q]}")
        #if not in final_characters already, add it to the dict
        #else += 1 for that specific character
    return final_characters

def upgraded_char_list(char_list):
    final_list = []

    for w in char_list:
        holder = {}
        
        char_key = w
        char_value = char_list[w]
    
        holder["char"] = char_key
        holder["num"] = char_value

        final_list.append(holder)
        # you need to figure out how to separate the keys and values to
        # make a list of dictionaries with 2 key:value pairs each, which
        # are to look like this {char : 'a', count : 2344}
        # make "char" the new key and make the 'a' the new value
        # make "count" the new key and make 2344 the new value
        # and both of those are before you append it to the final list
        # 'w' is the key
        # char_list[w] is the value 

    #print(final_list) 
    return final_list

def give_key(z):
    return z["num"]