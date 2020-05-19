"""
Checks if an input only has letters.
@param check_string The string to be checked.
@return True if the message doesn't contain only letters. 
"""   
def inputchecker(check_string):
    for x in check_string:
        if (96 < ord(x) < 123) == False:
            return True

"""
Encodes the text by the key
@param user_string The string to be encoded.
@param key Decides how much it will be moved.
@return True if the message doesn't contain only letters. 
"""
def encoder(text, key):
    text_list = list(map(str, text))
    key_list = list(map(str, key))

    # new list made by assigning a new ascii value
    new_text_list = [ord(x) - 97 for x in text_list]
    new_key_list = [ord(y) - 97 for y in key_list]

    # calculates the ascii of letters and generates the string
    formula(new_text_list, new_key_list)
    

"""
Provides a formula for encoded text
@param text The string to be encoded.
@param key Decides how much it will be moved.
@return None 
"""     
def formula(text, key):
    encoded_list = []
    final_list = []
    for i in range(len(text)):
        
        # adding an element to the list
        encoded_list.append((text[i] + key[i]) % 26)        

    for i in encoded_list:
        final_list.append(chr(i + 97))

    # in order to convert a list to string, use .join!!  
    final_str = ''.join(final_list)
    print()
    print('The encoded text: ' + final_str)
    

"""
Code inside this function will run when the program starts.
"""
def main():
    
    user_choice = 'y'       # default value

    while user_choice != 'n':
        print('Enter text (letters only): ')
        user_text = input().lower()     # making it a lower case
        while inputchecker(user_text) == True:
            print('Input must contain only letters. Try again: ')
            user_text = input().lower()
        
        print('Enter key (letters only): ')
        user_key = input().lower()      # making it a lower case
        while inputchecker(user_key) == True:
            print('Input must contain only letters. Try again: ')
            user_key = input().lower()

        encoder(user_text, user_key)
        print('The decoded text: ' + user_text)

        print()
        print('Run again? ')
        user_choice = input()

    
if __name__ == '__main__':
    main()
