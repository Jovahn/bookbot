import sys
from stats import get_book_text
from stats import character_count
from stats import upgraded_char_list
from stats import give_key

def main():
    stable_sys_argv = sys.argv
    if len(stable_sys_argv) == 2: 
        with open(stable_sys_argv[1]) as f:
            #can only read once without doing something screwy
            total_book_string = f.read()
            complete_word_count = get_book_text(total_book_string)
            complete_char_count = character_count(total_book_string)

            #print(complete_word_count)
            #print(complete_char_count) 
            u_list = upgraded_char_list(complete_char_count)
            u_list.sort(reverse = True, key = give_key)

            print("============ BOOKBOT ============\n")
            print(f"Analyzing book found at {stable_sys_argv[1]}\n")
            print("----------- Word Count ----------\n")
            print(f"{complete_word_count}\n")
            print("--------- Character Count -------\n")
            for s in u_list:
                #char_tester = s["char"]
                if(s["char"].isalpha() == True):
                    current_char = s["char"]
                    current_num = s["num"]
                    print(f"{current_char}: {current_num}")
            
            print("============= END ===============\n") 
    else:   
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()