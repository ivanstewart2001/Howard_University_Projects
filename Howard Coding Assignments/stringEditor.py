def isVowel(char):
    return char in 'aeiouAEIOU'

def remove_vowels(s):
    index = 0
    newString = ""
    while index < len(s):
        if not isVowel(s[index]):
            newString += s[index]
        index += 1
    return newString

def run():
    running = True
    user_input = ""

    while running:
        command = input("> ")

        if command == "h":
            print("h - show this help" )
            print("i - input a new string")
            print("p - print the current string")
            print("u - uppercase the current string")
            print("l - lowercase the current string")
            print("x - switch the case of each character in the current string")
            print("d - disemvowel the current string")
            print("q - quit this program")
        
        elif command == "i":
            user_input = input("New String: ")
            # if user_input != user_input:
            #     user_input = input("New String: ")

        elif command == "p":
            if user_input == "":
                print("You have to enter a string first!")
            else:
                print(user_input)
            
        elif command == "u":
            if user_input == "":
                print("You have to enter a string first!")
            else:
                user_input = user_input.upper()
            
        elif command == "l":
            if user_input == "":
                print("You have to enter a string first!")
            else:
                user_input = user_input.lower()

        elif command == "x":
            if user_input == "":
                print("You have to enter a string first!")
            else:
                user_input = user_input.swapcase()
            
        elif command == "d":
            if user_input == "":
                print("You have to enter a string first!")
            else:
                user_input = remove_vowels(user_input)

        elif command == "q":
            running = False
        
        else:
            print("Command not found! Type 'h' for valid commands.")
    

# Don't edit below this line.
if __name__ == "__main__":
    run()
    