#Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

times = 0
while True:
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    if username != "python" or password != "rules":
        print("Your Username or Password is wrong! Enter the username and password again.")
        times = times + 1
        #continue
        if times >= 5:
            print("Your Access Denied.")
            break
    elif username == "python" and password == "rules":
        print("Welcome!")
        break

