# 104 Write a Program to find in which line of the file the word "learning" occur first. print -1 if not found.

# def check_for_line(file,word):
#     with open(file, "r") as f:
#         line_count= 1
#         for line in f:
#             if word in line:
#                 print(f"The Word is found at line {line_count}") 
#                 break                                                # Iterating through the file line by line using loop.
#             line_count += 1
#         else:
#             print(-1)

# check_for_line(r"C:\Hammad Mustafa\A Long Journey\AI\Artificial Intelligence (AI)\Python Programming\Chapter 10- Remaining Concepts\sample1.txt","hello")




# # 2nd Method:
def check_for_line(file,word):
    with open(file, "r") as f:
        data= True
        line_no =1
        while data:
            data = f.readline()
            if(word in data):
                print(f"The Word is found at line {line_no}")
                break
            line_no +=1
    return -1

check_for_line(r"C:\Hammad Mustafa\A Long Journey\AI\Artificial Intelligence (AI)\Python Programming\Chapter 10- Remaining Concepts\sample1.txt","hello")