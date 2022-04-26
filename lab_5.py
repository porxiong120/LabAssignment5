"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
then from the text file, we create a list of strings from each lines in the text file.
Then, we create a dictionary from the list.
Once the text file has been read into memory, we close the file.
 
We then define a function for translating which involves splitting the user input (sentence) into an
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]
 
once we have the array of strings representing the user's input sentence, we
look through each words, find the key matching the word and returns back the value tied to that word
in our dictionary.
 
After each word is translated, we then
Print out the translated sentence to the user.
"""

 
"""
main():
    set sentence = input()
    set dictionary = create_dictinary()
    translate(sentence, dictionary)
 
translate(sentence, dictionary):
    words = each of the word in the sentence
    for each words, translate the word
    print translated sentence to user
 
create_dictionary():
    read in textese.txt
    create list = each line from file
    close the file
    create a dictionary off of the list
    return the dictionary
 
main()
"""

 
def main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictinary("textese.txt")
    translate(sentence, dictionary)
 
def create_dictinary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])
 
def translate(sentence, dictionary):
    words = sentence.split()
    for word in words:
        print(dictionary.get(word, word), " ", end="")
 
main()