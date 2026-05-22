'''file=open("practice.py","r")
line=file.readlines()
file.close()

n=int(input("how many lines from the end?"))
last_lines=line[-n:]

for lines in last_lines:
    print(lines,end='')


# Defining a user-defined exception
class PasswordTooShortError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Function to check password length
def check_password(password):
    if len(password) < 6:
        raise PasswordTooShortError("Password must be at least 6 characters long!")
    else:
        print("Password accepted.")

# Example usage
try:
    pwd = input("Enter your password: ")
    check_password(pwd)
except PasswordTooShortError as e:
    print("Error:", e)

lines = [
    "Hello\n",
    "Good Morning!!\n",
    "I am writting python code.\n"
]

file= open("example.txt", "w") 
file.writelines(lines)

print("Lines written to example.txt")

file = open("example.txt", "r")
print(file.read())
file.close()


try:
    # 2. FileNotFoundError
    print("\n2. FileNotFoundError example:")
    file= open("nonexistentfile.txt", "r") 
    file.read()

except FileNotFoundError:
    print("Error: File not found!")
    
try:
    # 3. ValueError
    print("\n3. ValueError example:")
    int("abc")

except ValueError:
    print("Error: Invalid integer!")
'''

names = ['alice', 'bob', 'andrew', 'anna', 'Charlie', 'alex']
a_names = []
name=names.startswith('a')
names.append(name)
print(names)
