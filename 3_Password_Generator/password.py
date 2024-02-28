# Using the sample function to generate extract random things from the string
# Syntax: random.sample(sequence, k)

import random
password_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-+<>?;:_={[]}|/<>,."
# print(len(password_string))

def generator(length):
    password = random.sample(password_string, k=length_input)
    final_password = "".join(password)
    print(f"Your password of length {length_input} is: {final_password}")
    return final_password

def password_saver(username, password):
    # To save the password in a text file, I'd used open() method in python in append mode
    # Syntax: open(file_name,mode)
    with open("saved_passwords.txt","a") as file:
        file.write(f"Username: {username}     ||     Password: {password}\n")

while True:
    length_input = input("\nEnter the length of the password: ")

    if length_input.isdigit():
        length_input = int(length_input)
        if length_input>=4 and length_input<=91:
            user_password = generator(length_input)
            save_option = input("\nDo you wanna save the password? (y/n) ")
            if save_option=='y':
                username = input("Enter the username for the password: ")
                password_saver(username,user_password)
                print("\n\nPassword saved successfully!")
                print("Check saved_passwords.txt file on your system to see the passwords!\n")

            elif save_option=='n':
                print("Password not saved")

            else:
                print("Invalid input!")
            break

        elif length_input>=92:
            print("Password Generation above 91 characters is not possible....")
            
        else:
            print("The length of password should be atleast 4")
            print("Cannot generate password less than 4 characters...")
    else:
        print("Please enter a valid input!")    
