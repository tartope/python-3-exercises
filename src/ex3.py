

def create_files(file_name):
    words_dict = {}
    with open(file_name, "r") as file:
        lines = file.read()
        words = lines.split()
        with open("../files/small-words.txt", "w") as small:
            for word in words:
                if len(word) < 3:
                    if word in words_dict:
                        words_dict[word] +=1
                    else:
                        words_dict[word] = 1
                        small.writelines(word + '\n')
        with open("../files/large-words.txt", "w") as large:
            for word in words:
                if len(word) >= 3:
                    if word in words_dict:
                        words_dict[word] += 1
                    else: 
                        words_dict[word] = 1
                        large.writelines(word + '\n')
    return len(words_dict.keys())



def ex3():
    total_words = create_files("../files/words.txt")
    print(f"Total words: {total_words}.")

ex3()