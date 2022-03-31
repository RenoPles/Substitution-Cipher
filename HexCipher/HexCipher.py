#######################################################################
#                                                                     #
#                              Imports                                #
#                                                                     #
#######################################################################

from sys import stdin,stdout

#######################################################################
#                                                                     #
#                             Functions                               #
#                                                                     #
#######################################################################

def encrypt(message):

    total_string = ""
    
    for i in range(0,len(message) - 1):
        
        uni_value = ord(message[i])
        uni_value += 7
        hex_value = f"{hex(uni_value)}"
        
        if (i == len(message) - 2): total_string += f"{hex_value[2:len(hex_value)]}"
        else: total_string += f"{hex_value[2:len(hex_value)]}-"
        
    # end for
            
    return total_string

# end def

def decrypt(message):

    message = message.strip("\n")
    end = False
    
    if (message == ""): end = True
        
    message = message.split("-")
    message = ["0x" + message for message in message]
    completed_string = ""

    if (end != True):
        
        for i in range(0,len(message)):

            hex_value = int(str(message[i]),16)
            dec_value = int(hex_value) - 7
            completed_string += chr(dec_value)
        

        # end for

    else:

        stdout.write("Please enter a valid string!")

    # end if
        
    return completed_string

# end def

#######################################################################
#                                                                     #
#                               Code                                  #
#                                                                     #
#######################################################################
    
encrypt_or_decrypt = ""
continue_script = False

while (continue_script == False):

    stdout.write("Encrypting or Decrypting (E/D): ")
    encrypt_or_decrypt = stdin.readline()
    encrypt_or_decrypt = encrypt_or_decrypt.upper()

    if (encrypt_or_decrypt.find("E") != -1): continue_script = True
    elif (encrypt_or_decrypt.find("D") != -1): continue_script = True

# end while
    
if (encrypt_or_decrypt.find("E") != -1):

    stdout.write("Message To Encrypt: ")
    user_input = stdin.readline()
    stdout.write(f"{encrypt(user_input)}")

elif (encrypt_or_decrypt.find("D") != -1):

    stdout.write("Message To Decrypt: ")
    user_input = stdin.readline()
    stdout.write(f"{decrypt(user_input)}")

else:

    stdout.write("Please enter a valid character! (e/d)\n")
    
# end if
