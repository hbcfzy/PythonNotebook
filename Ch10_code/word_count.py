"""count words in files"""

def count_words(f_name):
    try:
        with open(f_name, encoding='UTF-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + f_name + " does not exist.")
    else:
        words = contents.split()
        print("The file " + f_name + " has about " + str(len(words)) + " words.")

f_name = 'alice.txt'
count_words(f_name)