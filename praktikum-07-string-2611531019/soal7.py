# Name: Hafidh Laudza Mikhrad
# Nim: 2611531019
# Question 7

name = "hafidh laudza mikhrad"
nim = "2611531019"

username = name.split()[0] + nim[-3:]
intake = "20" + nim[:2]
lebar_kartu = 30
garis = "=" * lebar_kartu

print(garis)
print("STUDENT CARD".center(lebar_kartu))
print(garis)
print(f"{'NAME':<10}: {name.title()}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username' :<10} : {username}")
print(f"{'intake' :<10} : {intake}")
print(garis)