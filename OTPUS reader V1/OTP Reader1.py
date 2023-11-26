# Made on 24/03/2023
# By Euan Hao
# V1 saved as OTP Reader1
# use this link for generating new ciphers:  https://www.random.org/integers/?mode=advanced

#no external modules for accessability on all interpreters/compilers
#do not reloop the code due to reuse of variable name comflicts. Only call functions.

def convertFromBNAB(raw):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!-()*£:@ "
    #special BNAB decode charset 63 character values, index from pos (0 to 33)
    message = ""
    index = 0
    
    for repeat in range(round(len(raw)/6)):    #amount of packets     ##example 011011 101101 010001 100010 110101 101000
        exponent = 0
        denary = 0
        for counter in range(6):   #calculates the decimal of the raw binary of each 6bit packet
            #print("total + ", (int(raw[index + counter]), "times ",  int(2**exponent)))
            denary = denary + (int(raw[index + counter]) * int(2**exponent))
            exponent = exponent + 1
            
        #endfor
        #print("")   
        index = index + 6
        message = message + charset[denary]   #finds the character of index denary
    
    return message

#endfunction

def convertToBNAB(raw, maxLen, code):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!-()*£:@ " #must be consistent/pos passed in by reference,
    #however due to the relative unlikeliness of change in charset value storage is fine.

    message = ""                #raw example :    "Hi, how are you Kid?"
    
    for index in range(len(raw)):
        whitespace = True
        rawBnab = 0 #unpadded int currently in denary, need to use binary version of it
        for counter in range(63):
            if raw[index] == charset[counter]:
                Bnab = bin(rawBnab)
                #print(Bnab,rawBnab)
                Bnab = pad(str(Bnab)[2:len(Bnab)])
                #print("pure unpad binary", len(Bnab)-1)
                #print("unpadded binary",str(Bnab)[2:len(Bnab)-1])
                whitespace = False #this way to catch any non accepted characters.
                message = message + Bnab
            #endif
            rawBnab = rawBnab + 1
        #endfor
        if whitespace == True:
            message = message + "111111"
        #endif
            
        #end counter for bnab value
    #end repeat for every character

    while len(message) < maxLen*6: #this finally adds spaces to fill up the message and due to OTP is secure.
        message = message + "111111"
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
print("V3.4.4 - no autoread")
print("")

Mode = ""
while Mode != "D" and Mode != "d" and Mode != "E" and Mode != "e":
    
    Mode = str(input("Are you 'Decoding' a message or 'Encoding'? (Type D/E): "))
    
#end validation

print("")
if Mode == "D" or Mode == "d":#decryption 
    print("Starting Decryption...")
    print("")

    lengthValidate = False   #this chunk validates the length
    while lengthValidate == False:
        rawInput=str(input("Please input the Encrypted binary message you received: "))
        print("")
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
        
    rawMessage = applyCipher(Cipher, Input)
    Message = convertFromBNAB(rawMessage) #BNAB means Between Nibble AND Byte encoding software. Ie, 6bts
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
        print("You may only use up to", int(len(Cipher)/6) ," of the following characters and also a spacebar: ")
        print("")
        print("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!-()*£:@")
        print("")
        rawInput = str(input("Please input the message you would like to send: "))
    #endwhile

    print("")

    Message = convertToBNAB(rawInput, (int(len(Cipher)/6)), Cipher)
    #currently takes the bnab code that isn't encoded
    print("Here is your code: ")
    print("")
    print(Message)
#end else condition for encryption   
    
#end if for mainbody
print("")
end = str(input("Are you done with the program? (Y/n): "))#holds the command prompt open.

    
