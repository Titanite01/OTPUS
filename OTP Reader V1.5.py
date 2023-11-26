# Made on 24/03/2023
# By Euan Hao
# V2 saved as OTP Reader2
# use this link for generating new ciphers:  https://www.random.org/integers/?mode=advanced
# This encryption is runs on a Binary XOR procedure.

#no external modules for accessability on all interpreters/compilers
#do not reloop the code due to reuse of variable name comflicts. Only call functions.

def convertFromASCII(raw):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!-=[];'#,./\|£$%^&*()_+{}:@~<>? "
    #ASCII 8 bit
    message = ""
    index = 0
    
    for repeat in range(round(len(raw)/8)):    #amount of packets     ##example 01101100 10110111 01010101 10011010 11110101 10101100
        exponent = 0
        denary = 0
        for counter in range(8):   #calculates the decimal of the raw binary of each 8bit packet
            #print("total + ", (int(raw[index + counter]), "times ",  int(2**exponent)))
            denary = denary + (int(raw[index + counter]) * int(2**exponent))
            exponent = exponent + 1
            
        #endfor
        #print("")   
        index = index + 6
        message = message + charset[denary]   #finds the character of index denary
        charactersUsedUp = round(len(raw)/8)  #returns the quantity of characters decoded.
    
    return message, charactersUsedUp

#endfunction

def convertToASCII(raw, maxLen, code):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!-=[];'#,./\|£$%^&*()_+{}:@~<>? " #must be consistent/pos passed in by reference,
    #however due to the relative unlikeliness of change in charset value storage is fine.

    message = ""                #raw example :    "Hi, how are you Kid?"
    
    for index in range(len(raw)):
        whitespace = True
        rawASCII = 0 #unpadded int currently in denary, need to use binary version of it
        for counter in range(94):
            if raw[index] == charset[counter]:
                ASCII = bin(rawASCII)
                #print(ASCII,rawASCII)
                ASCII = pad(str(ASCII)[2:len(ASCII)])
                #print("pure unpad binary", len(ASCII)-1)
                #print("unpadded binary",str(ASCII)[2:len(ASCII)-1])
                whitespace = False #this way to catch any non accepted characters.
                message = message + ASCII
            #endif
            rawBnab = rawBnab + 1
        #endfor
        if whitespace == True:
            message = message + bin(94)
        #endif
            
        #end counter for ASCII value
    #end repeat for every character

    #while len(message) < maxLen*6: #this was to add spaces to pad out the code.
        #message = message + "111111"
    #end while

    message = applyCipher(code, message)#cipher it
    
    return message


#end function


def strip(entry):
    
    Cipher=("")
    index = 0
    for index in range(len(entry)):
        indexVal = entry[index:index+1]
        indexVal = indexVal.strip()
        Cipher=(Cipher + indexVal)
    #endfor
    return Cipher
    
#end function


def pad(entry): # pad for Bnab, we pad onto the end due to the way it is read here.

    entry = str(entry)
    while len(entry) < 6:#not len != 6 due to possible infinite loop
        entry = "0" + entry    #now reverse digit order
    #endwhile
    reverse = ""
    for counter in range(len(entry)):
        reverse = reverse + str(entry[(5 - counter)])
    return reverse

#endfunction


def applyCipher(code, message):
    
    output = ""
    for index in range(len(message)):
        indexVal1 = (code[index:index + 1])
        indexVal2 = (message[index:index + 1])
        
        if indexVal2 == "1" and indexVal1 == "0":   #XOR gate for inputs val1 and val2
            output = output + "1"
        elif indexVal2 == "0" and indexVal1 == "1":
            output = output + "1"
        elif indexVal2 == "0" and indexVal1 == "0":
            output = output + "0"
        else:
            output = output + "0"
        #endif
        

    #endfor
    return output
       
#end function    



#start mainbody-----------------------------------------------------------------------------


print("Important note! You must input the correct cipher, in order for the program to work!")
print("V2.5.6 - no autoread")
print("")

Mode = ""
while Mode != "D" and Mode != "d" and Mode != "E" and Mode != "e":
    
    Mode = str(input("Are you 'Decoding' a message or 'Encoding'? (Type D/E): "))
    
#end validation

print("")
if Mode == "D" or Mode == "d":#decryption 
    print("Starting Decryption...")
    print("")

    lengthValidate = False   #this chunk checks the length
    while lengthValidate == False:
        rawInput=str(input("Please input the Encrypted binary message you received: "))
        rawCipher=str(input("Please input the Cipher for the respective data:  "))
        Cipher = strip(rawCipher)
        Input = strip(rawInput)
        if len(Cipher) != len(Input):
            print("")
            print("The Message and Cipher are of different lengths, so the code will not work.")
            print("please try again.")
        else:
            lengthValidate = True
        #endif

    rawInput=str(input("Please input the Encrypted binary message you received: "))#########################################################BUILDING THE NEW VARIABLE CIPHER EXTRACTING
    Input = strip(rawInput)
    length = (len(Input)/8)

    fileCipher = open("cipher(100C)N234.txt","r")                            #maybe in future version update so that it can manually open and empty unlimited amounts of cipher files.
    Cipher = ""
 
    while len(Cipher) != Input: #whilst the cipher hasn't matched the input in length
        for counter in range(len(Input)):
            
        

    fileCipher.close()



    
    rawMessage = applyCipher(Cipher, Input)
    Message = convertFromASCII(rawMessage) #8 Bit ASCII
    print("")
    print("Here is the message: ")
    print("")
    print(Message)
    
else: #for encryption
    print("Starting Encryption...")
    print("")

    rawCipher=str(input("Please input the Cipher for the respective data:  "))
    Cipher = strip(rawCipher)
    print("Your Cipher allows a maximum of ", int(len(Cipher)/6) ," characters.")#int truncates rather than round so safer.

    rawInput = ""
    while len(rawInput) > (int(len(Cipher)/6)) or len(rawInput) == 0:
        print("You may only use the following characters and also a spacebar: ")
        print("")
        print("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!-()*£:@")
        print("")
        rawInput = str(input("Please input the message you would like to send: "))
    #endwhile

    print("")

    Message = convertToASCII(rawInput, (int(len(Cipher)/6)), Cipher)
    #currently takes the ASCII code that isn't encoded
    print("Here is your code: ")
    print("")
    print(Message)
#end else condition for encryption   
    
#end if for mainbody
print("")
end = str(input("Are you done with the program? (Y/n): "))#holds the command prompt open.

    
