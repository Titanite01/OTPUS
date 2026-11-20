# Made on 24/03/2023
# By Euan H.
# V2 saved as OTP Reader2
# use this link for generating new ciphers:  https://www.random.org/integers/?mode=advanced
# This encryption is runs on pure Binary with an XOR procedure.
# You don't need to dowload the pyperclip module or any other external modules, however please keep the contents of the folder together.
# THIS PROGRAM WILL NOT HANDLE CORRUPT MESSAGES.



def convertFromASCII(raw, charset):

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

def convertToASCII(raw, maxLen, code, charset):

    #charset must be consistent/pos passed in by reference

    message = ""                
    
    for index in range(len(raw)):
        whitespace = True
        rawASCII = 0 #unpadded int currently in denary, need to use binary version of it
        for counter in range(len(charset)): #this repeats for any size of charset
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
            
        #end counter for unicode value
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
    print(output, "heehehe")###remove after OK!!!!!?
    return output
       
#end function    

def deleteCipher(length, fileCipherPath):

        fileCipher = open(fileCipherPath, "r")

        rawCipher = fileCipher.readline()

        rawCipher = "".join(rawCipher.split('\t'))

        fileCipher.close()

        # Overwrite

        fileCipher = open(fileCipherPath, "w")

        fileCipher.write(rawCipher[length:])

        fileCipher.close()

        return rawCipher[:length]
    

#start mainbody-----------------------------------------------------------------------------

try:
    import pyperclip
    print("Copy to clipboard function successfully loaded!")
except:
    print("You do not have pyperclip installed, thus python will not be able to autosave to your clipboard.")
#end try
    
charset = "␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟ !'#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~␡ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"

#ASCII 8 bit printable characters without the "    
#pyperclip.copy("The text has been copied to the clipboard.")


print("Important note! You must ensure that the cipher file has not run out, in order for the program to work!")
print("You may paste the code in with spaces and formatting characters.")
print("V2.7.6 - with signed messages")
print("")

Mode = ""
while Mode != "D" and Mode != "d" and Mode != "E" and Mode != "e":
    
    Mode = str(input("Are you 'Decoding' a message or 'Encoding'? (Type D/E): "))
    
#end validation


print("")
if Mode == "D" or Mode == "d":#DECRYPTION -----------------------------------------------------

    ###note on encryption standard, 8 bits for sheet no., then 24 bits for char number in the sheet, then the message after. pre message signature is consistent.
    print("Starting Decryption...")
    print("")

    rawInput=str(input("Please input the Encrypted binary message you received: "))    #example data 1111 1111 1111 1111 1111 1111 1111 1111
    Input = strip(rawInput)
    
    #print(Input, "input")
    #print(len(Input), "len of input in binary")


    #fileLog = open("MEMORY(XC)NB.txt","r") #read from log file what sheet number is

    
    #fileCipher = open("cipher(100C)NA234.txt","r")      #IN FUTURE ADD FUNCTION TO READ AS MANY FILES AS NECESSARY 


    Cipher = ""                  
    fileCipher = open("cipher(100C)NA234.txt","r")
    while len(Cipher) != len(Input): #whilst the cipher hasn't matched the input in length

        
        counter = 0
        while counter != 8: #makes sure to strip all the code to 1s and 0s
            readCharacter = fileCipher.read(1)
            if readCharacter == "1" or readCharacter == "0":
                counter = counter + 1
                Cipher = Cipher + readCharacter
            #endif
        #endwhile
        
        #print("cipher: ", Cipher)
          
    fileCipher.close()

    
    rawMessage = applyCipher(Cipher, Input)
    (Message,charsUsed) = convertFromASCII(rawMessage, charset) #8 Bit ASCII


    print("")
    print("Here is the message: ")
    print("")
    print(Message)

    #Below, proceed to delete cipher:

    cipherData = ""
    fileCipher = open("cipher(100C)NA234.txt","r")

    # returns cipher sections required and delete them from file

    deleteCipher(len(Input),"cipher(100C)NA234.txt")

    


    #countC = 0
    #for x in fileCipher:

        #if fileCipher.read(1) == "1" or fileCipher.read(1) == "0":
            #cipherData = cipherData + fileCipher.read(1)
            #countC = countC +1
        #endif

        

        
    


    

else: #for encryption -------------------------------------------------------------------------
    print("Starting Encryption...")
    print("")

    rawCipher=str(input("Please input the Cipher for the respective data:  "))
    Cipher = strip(rawCipher)
    print("Your Cipher allows a maximum of ", int(len(Cipher)/6) ," characters.")#int truncates rather than round so safer.

    rawInput = ""
    while len(rawInput) > (int(len(Cipher)/6)) or len(rawInput) == 0:
        print("You may only use all Extended ASCII characters: ")
        print("")
        rawInput = str(input("Please input the message you would like to send: "))
    #endwhile

    print("")

    Message = convertToASCII(rawInput, (int(len(Cipher)/6)), Cipher, charset)
    #currently takes the bnab code that isn't encoded
    print("Here is your code: ")
    print("")
    print(Message)
#end else condition for encryption   



#end if for mainbody
print("")
end = str(input("Are you done with the program? (Y/n): "))#holds the command prompt open.

    
