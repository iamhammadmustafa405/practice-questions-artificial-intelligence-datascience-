# 108: Write a program to count the number of words in a file.
def word_count(file):
    with open(file, "r") as f:

        data= f.read()
        words= data.split(" ")


        filtered_data= []
        for i in words:
            if "\n" not in i:
                filtered_data.append(i)
        

        for i in words:
            if "\n" in i:
                i = i.split("\n")
                filtered_data.extend(i)

        

        count= 0
        for i in filtered_data:
            count+=1
    print(f"There are {count} words in this file.")

word_count(r"C:\Hammad Mustafa\A Long Journey\AI\Artificial Intelligence (AI)\Python Programming\Chapter 10- Remaining Concepts\sample1.txt")



# 2nd Method:

# with open("words.txt", "r") as f:
#     data= f.read()
#     words= data.split()
#     count= len(words)
    
# print(f"There are {count} words in this file.")
