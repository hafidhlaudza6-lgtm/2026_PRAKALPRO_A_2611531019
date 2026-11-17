# Name: Hafidh Laudza Mikhrad
# Nim: 2611531019
# Question 3

text = "Hafidh Laudza Mikhrad"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)