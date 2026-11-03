attempt = 1
correct_pin = "1234"
MAX_ATTEMPTS = 3

while pin != correct_pin and attempt <= MAX_ATTEMPTS:
    pin = input("Enter your PIN:")
    if pin == correct_pin:
        print("Access granted")
    else:
        print("Incorrect PIN")
        attempt += 1
        print("Account locked")