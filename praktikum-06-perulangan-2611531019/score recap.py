PASS_SCORE = 60

n = int(input("Number of students: "))
while n < 1:
    print("Invalid student count!")
    n = int(input("Number of students: "))

total = 0       
passed = 0      
highest = 0     

for i in range(n):
    score = int(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))

    total += score

    if score >= PASS_SCORE:
        passed += 1

    if score > highest:
        highest = score

average = total / n

print(f"Total score: {total}, Average score: {round(average, 2)}")   
print(f"Passed: {passed}")                                          
print(f"Highest score: {highest}")                                  