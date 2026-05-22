'''# Ask the user to enter a string
s = input("Enter a string: ")

# List of vowels
vowels = "AEIOU"

# Go through each character in the text
for char in s:
    # If the letter is a vowel, print it
    if char in vowels:
        print(char, end=" ")'''


'''
str = input("enter a string: ")
def is_palindrome(s):
    return s == s[::-1]

if is_palindrome(str):
    print(str,"is palindrome")
else:
    print(str,"is not palindrome")
'''
'''
str = "eye"
def rev_str(s):
    return s[::-1]

if rev_str(str) == str:
    print(str,"is palindrome")
else:
    print(str,"is not palindrome")
'''
'''
name = input("enter your name: ")
split_name = name.split()
print(split_name)

age = 24
formated_name = "my name is {} and I am {} years old".format(name,age)
print("formated name: ",formated_name)

print("upper: ",name.upper())

print("lower: ",name.lower())

print("isalnum: ",name.isalnum())

print("ends with: ",name.endswith("mar"))

print("starts with: ",name.startswith("rad"))
'''
'''
s = "python"

chars = list(s)

for i in range(len(chars)):
    for j in range(i + 1, len(chars)):
        if chars[i] > chars[j]:
            chars[i], chars[j] = chars[j], chars[i]

sorted_string = ''.join(chars)

print(sorted_string)
'''

'''#Pangram Checker
def is_pangram(sentence):
    sentence = sentence.lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter in sentence:
            return True
        return False

sentence = "rysb kaiqo knj suwk kxkl "
if is_pangram(sentence):
    print("It's a pangram sentence ")
else:
    print("It is not a pangram sentence ")'''
    
'''
def count_letter(word,letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

print(count_letter("programming", "p"))'''

'''
def StartEndsVowel(words):
    vowel = "aeiou"
    if words[0] in vowel and words[-1] in vowel:
        return True
    else:
        return False

print(StartEndsVowel("apple"))
print(StartEndsVowel("end"))
print(StartEndsVowel(" "))'''

'''def Eliminate_Letter(word, letter):
    return word.replace(letter, '')
print(Eliminate_Letter("programming","m"))'''
'''
def Eliminate_Letter(word, letter):
    result = ""
    for char in word:
        if char != letter:
            result += char
    return result
print(Eliminate_Letter("programming", "m"))'''
        

def Eliminate_Letter(word, letter):
    return word.replace(letter, '')

