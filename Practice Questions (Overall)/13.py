# # Given the string s = 'the quick brown fox jumps over the lazy dog', write code that: (a) counts the
# number of vowels, (b) counts words longer than 3 letters, (c) capitalises the first letter of every
# word and prints the result.

s = 'the quick brown fox jumps over the lazy dog'

vowel= ["a","e","i","o","u"]
count = 0
# a
for letter in s:
    for i  in vowel:
        if letter == i:
            count+=1


#b
count_letter= 0
for i in s.split(" "):
    if len(i) > 3:
        count_letter +=1



#c
capital = s.title()



# result printing

print(f"The Number of Vowels in the String are: {count}")
print(f"Number of Words longer than 3 are: {count_letter}")
print(f"Capitalized String is: {capital}")