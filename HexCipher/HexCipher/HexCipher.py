
def main():
    #       Program:    Hex Cipher
    #       Author:     Trent Weikel
    #       Date:       03/29/22
    #       Purpose:    Encrypts or decrypts the users text by using unicode and adding 7 to the hex value.

    #       Test Cases: 
    #                   Hello, World! = 4F-6C-73-73-76-33-27-5E-76-79-73-6B-28
    #                   ☺☻♥♦♣♠• = 2641-2642-266C-266D-266A-2667-2029

    #######################################################################
    #                                                                     #
    #                              Imports                                #
    #                                                                     #
    #######################################################################

    import Functions    # Imports the Functions.py file.

    #######################################################################
    #                                                                     #
    #                               Code                                  #
    #                                                                     #
    #######################################################################

    encrypt_or_decrypt = ""
    continue_script = False

    while (continue_script == False):

        encrypt_or_decrypt = input("Encrypting or Decrypting (E/D): ").upper()

        if (encrypt_or_decrypt.find("E") != -1 and len(encrypt_or_decrypt) == 1): continue_script = True
        elif (encrypt_or_decrypt.find("D") != -1 and len(encrypt_or_decrypt) == 1): continue_script = True
        else: print("\nPlease enter a valid character! (e/d)\n")
        # Checks if variable is a valid value to rerun loop if needed.

    # end while

    if (encrypt_or_decrypt.find("E") != -1):

        user_input = input("Message To Encrypt: ")      # Gets the message the user wants to encrypt.
        print(f"Encrypted Message: {Functions.encrypt(user_input)}\n")

    else:

        user_input = input("Message To Decrypt: ")      # Gets the message the user wants to decrypt.
        print(f"\nDecrypted Message: {Functions.decrypt(user_input)}\n")

    # end if
if __name__ == "__main__":
    main()
