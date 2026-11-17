# Name: Hafidh Laudza Mikhrad
# Nim: 2611531019
# Question 4

phone = "082611531019"
masked = phone[:4] + "*" * len(phone[5:-2]) + phone[-3:]
print(masked)