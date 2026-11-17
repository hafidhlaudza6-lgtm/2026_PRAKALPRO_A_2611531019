# Name: Hafidh Laudza Mikhrad
# Nim: 2611531019
# Question 6

# Pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# Masalah
full_name = input("Name: ")
nim = input("NIM: ")
 
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

clean = full_name.strip() + " " + nim[-3:]
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

username = first.lower() + nim[-3:]
print(username)