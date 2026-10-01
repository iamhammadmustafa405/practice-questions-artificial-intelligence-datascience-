# 103:  Search in the file if the any word exists or not.

def search_word(file):
    word= input("Enter the word you want to find in the file: ")
    with open(file,"r") as f:
        data = f.read()
        if word in data:
            print("The Word is found.")
        else:
            print("No, there is no such word in this file")

search_word(r"C:\Hammad Mustafa\A Long Journey\AI\Artificial Intelligence (AI)\Python Programming\Chapter 10- Remaining Concepts\sample1.txt")