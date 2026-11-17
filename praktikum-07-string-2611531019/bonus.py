# Name : Hafidh Laudza Mikhrad
# NIM : 2611531019
# question bonus

teks = input("Masukkan kalimat: ")

bersih = ""
for huruf in teks.lower():
    if huruf.isalnum():
        bersih = bersih + huruf

depan = 0
belakang = len(bersih) - 1
beda = 0

while depan < belakang:
    if bersih[depan] != bersih[belakang]:
        bedda = beda + 1
    depan = depan + 1
    belakang = belakang - 1

if beda == 0:
    print("Palindrome")
else:
    print("not a Palindrome")