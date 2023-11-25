import random
import string
def main():
    char_letters,num_letter,spec_letters= (None, None, None)

    while char_letters !="exit":    
        char_letters = input("please enter: How many charachter[a-z,A-Z] letters?")
        if not char_letters.isnumeric() and char_letters !="exit":
            print("Invalid input:  Please enter an integer or type exit")
            continue     
        elif char_letters !="exit":
            char_letters_as_int = int(char_letters)
            break

    if char_letters != "exit":
        while num_letter !="exit":
            num_letter = input("please enter: How many numbers[0-9] ? ")
            if not num_letter.isnumeric() and num_letter !="exit":
                print("Invalid input:  Please enter an integer or type exit: ")
                continue     
            elif num_letter !="exit":
                num_letter_as_int = int(num_letter)
                break
        

    if num_letter != "exit" and char_letters != "exit":
        while spec_letters !="exit": 
            spec_letters = input("please enter: How many special charachters[$,^,#,...] ? ")
            if not spec_letters.isnumeric() and spec_letters != "exit":
                print("Invalid input:  Please enter an integer or type exit: ")
                continue     
            elif spec_letters !="exit":
                spec_letters_as_int = int(spec_letters)
                break

    if char_letters !="exit" and num_letter != "exit" and spec_letters != "exit":
        # Create a list of characters from a to z
        lowercase_letters = list(string.ascii_lowercase)
        # Create a list of characters from A to Z
        uppercase_letters = list(string.ascii_uppercase)
        # Combine the lowercase and uppercase letters into a single list

        all_letter = lowercase_letters + uppercase_letters
        random.shuffle(all_letter)

        password_list=[]
        for i in range(1,char_letters_as_int+1):
            password_list.append(random.choice(all_letter))


        for i in range(1,num_letter_as_int+1):
            password_list.append(random.choice(range(10)))

        # Create a list of special characters
        special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        for i in range(1,spec_letters_as_int+1):
            password_list.append(random.choice(special_characters))

        random.shuffle(password_list)
        passwd =""
        for char in password_list:
            passwd += str(char)
        print (passwd)    

if __name__ == "__main__":
    main()