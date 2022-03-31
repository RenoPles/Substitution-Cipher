#       Program:    Hex Cipher Functions
#       Author:     Trent Weikel
#       Date:       03/29/22

#######################################################################
#                                                                     #
#                             Functions                               #
#                                                                     #
#######################################################################

def encrypt(message):

    total_string = ""
    
    for i in range(0,len(message)):
        
        uni_value = ord(message[i])                         # Gets the decimal unicode value of a letter.
        uni_value += 7                                      # Adds 7 to the decimal value.
        hex_value = f"{hex(uni_value)}"                     # Converts the decimal number to a hex value.
        
        if (i == len(message) - 1): total_string += f"{hex_value[2:len(hex_value)]}"
        else: total_string += f"{hex_value[2:len(hex_value)]}-"

    # end for
            
    return total_string.upper()

# end def

def decrypt(message):

    message = message.strip("\n")
    end = False
    
    if (message == ""): end = True
        
    message = message.split("-")
    message = ["0x" + message for message in message]       # Adds the string "0x" to the beginning of each value in the list.
    completed_string = ""

    if (end != True):
        
        for i in range(0,len(message)):

            hex_value = int(str(message[i]),16)             # Converts the string to a hex value. 
            dec_value = int(hex_value) - 7                  # Subtracts 7 from the hex value as a decimal number.
            completed_string += chr(dec_value)              # Adds the character to the return string
        

        # end for

    else:

        completed_string = "Please enter a valid string!\n"

    # end if
    
    return completed_string                                 # Returns the completed and decrypted string.

# end def