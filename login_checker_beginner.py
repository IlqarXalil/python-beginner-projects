age = int(input("Enter your age:"))
password = "admin123"

if age >= 18:
    print("Access granted")
    age = True
else:
    print("Access denied")
    age = False

if age == True:
    password1 = input("Enter password:")

    if password1 == password:
        print("Hello, welcome!")
    else:
        print("Wrong password")