# Made on 18/11/2026 (updated the 2023 version)
# By Euan Hao
# V4 saved as OTPE v4 reworked
# Title:  One Time Picture Exchange
# New cipher technique using obscurity based encryption, through the use of image files and an image index, built for use by non computer savvy.
# This encryption is runs on standard Binary XOR procedure.

### pyinstaller version for executables and all related modules
### featuring desynchronised message indexing. Maybe it increases security.




def convertFromASCII(raw):

    message = ""
    list = []
    length = int(len(raw)/8)
    print(length)
    print("do ascii calcs")
    for repeat in range(length):    #repeat 57 x
        
        value = 128
        denary = 0

        for counter in range(8):   #iterate though 8 consecutive chars 
            pointer = repeat * 8 + counter
            if raw[pointer] == "1":
                denary = denary + value

            value = int(value/2)
        
        print("Denary  ",denary)
        list.append(denary)  
        #endfor
        #print("")   
 #returns the quantity of characters decoded.
    print(list)
    for index in range (length):
            message = message + charset[list[index]]

    print("Result  ",message)
    return message

#endfunction

def convertToASCII(raw):

    #charset must be consistent/pos passed in by reference
    #print("RAW TO ASCII TXT", raw)
    message = ""                
    #print("quoted length:    ")

  
    
    for index in range(len(raw)):#no. of characters
        for counter in range(len(charset)): #this repeats for any size of charset
            if raw[index] == charset[counter]:
                ASCII = bin(counter)
                ASCII = pad(str(ASCII)[2:len(ASCII)])
                #print("ascii value:  ", charset[counter], str(ASCII), len(ASCII))
                message = message + ASCII
        #endfor
            
        #end counter for unicode value
    #end repeat for every character

    
    #print(message, len(message))
    return message


#end function


def strip(entry):
    
    output=("")

    for index in range(len(entry)):
        indexVal = entry[index:index+1]
        indexVal = indexVal.strip()
        output=(output + indexVal)
    #endfor
    return output
    
#end function


def pad(entry): 

    print("I am padder ",entry)
    entry = str(entry)
    while len(entry) < 8:#not len != 6 due to possible infinite loop
        entry = "0" + entry    #now reverse digit order
    #endwhile
    reverse = ""
    for counter in range(len(entry)):
        reverse = reverse + str(entry[(5 - counter)])
    
    #print("REVERSE", reverse)
    print("I have padded ",reverse)
    return reverse

#endfunction



def decodeChunk(cipherList, index, length):     #[29, 35, 61 ... ] index=0, chunklen = 57


    print("ASCCI",cipherList, index, length/8)
    #print(cipherList[0:56])
    chunk_len = int(length/8)   #from 456, to 57 length
    print(chunk_len)
    print(type(cipherList))
    index = int(index)
    chunkData = [0]*(chunk_len)

    print(chunkData, type(index))
    
    
    for counter in range (chunk_len):
        pointer = counter + index
        chunkData[counter] = int(cipherList[pointer])
        counter = counter + 1


    print("what is thisLLL",chunkData, len(chunkData), type(chunkData), charset)
    
    for counter in range (chunk_len):
            
            if chunkData[counter] < 10:
                chunkVal = "0" + str(chunkData[counter]) #ensures no numbers overflow 01-99
                chunkData[counter] = chunkVal
                #print(chunkVal, chunkData[counter])
            elif chunkData[counter] > 99:
                chunkVal = str(chunkData[counter])
                chunkVal = chunkVal[0:2]
                chunkData[counter] = chunkVal
                #print(chunkData[counter])
            else:
                chunkData[counter] = str(chunkData[counter])
        
    chunkExport = ""

    for index in range (len(chunkData)):
        chunkExport = chunkExport + charset[int(chunkData[index])]

    new_index = index + length
    print("CHUNK EXP", chunkExp)
    chunkExport = convertToASCII(chunkExport)

    print("chunkdata    ", chunkExport)
    code = convertToASCII(chunkExport)
    print(code, len(code))


    return code




def getChunk(cipherList, message, index):

    message_len = len(strip(message))
    
    chunk = cipherList[index:(index + message_len)]
    quote_len = round(len(chunk)/8 )

    chunkData = [0]*(quote_len)


    for counter in range (quote_len):
        
        if chunk[counter] < 10:
            chunkVal = "0" + str(chunk[counter]) #ensures no numbers overflow 01-99
            chunkData[counter] = chunkVal
            #print(chunkVal, chunkData[counter])
        elif chunk[counter] > 99:
            chunkVal = str(chunk[counter])
            chunkVal = chunkVal[0:2]
            chunkData[counter] = chunkVal
            #print(chunkData[counter])
        else:
            chunkData[counter] = str(chunk[counter])
    
    chunkExport = ""

    for index in range (len(chunkData)):
        chunkExport = chunkExport + charset[chunk[index]]

    new_index = index + message_len

    chunkExport = convertToASCII(chunkExport)

    #print(chunkData,chunkExport, len(chunkExport))
    #print("message:    ",message, len(message))
    
    return chunkExport, new_index  #chunkData is a str array due to formatting preservation




def applyCipher(Cipher, message, index, length, mode):     #cipher in binary already (needs chunk), message converted to padded binary and index is a binary counter
    
    print(mode, type(mode))
    if mode == True:  #encrypting 
        (chunk, new_index) = getChunk(Cipher, message, index) 
        print("getchunk", chunk)      #removed leaked bits
    else:
        (chunk) = decodeChunk(Cipher, index, length)
        new_index = index
        print("decodechunk")
        print("\n\n\n\n\n\n")
        #chunk = str(chunk)

    

    #print(len(message))
    output = ""
    for counter in range(len(message)):   #make sure all operations are conducted in STRINGS
        
        indexVal1 = (chunk[counter])
        indexVal2 = (message[counter])

        if indexVal2 == "1" and indexVal1 == "0":   #XOR gate for inputs a, b
            output = output + "1"
        elif indexVal2 == "0" and indexVal1 == "1":
            output = output + "1"
        elif indexVal2 == "0" and indexVal1 == "0":
            output = output + "0"
        else:
            output = output + "0"
        #endif

    #endfor
    

    return (output, new_index, mode)
       
#end function    



def validateRawText(input):

    output = ""
    for index in range (len(input)):

        for counter in range (len(charset)):
            if input[index] == charset[counter]:
                output = output + input[index]
                
        #output = output + "␀"   #needs better implementation

    #print(output)
    return output



def writeToLog(logMessage, local_address, new): #1 new file/0 append
    
    print("")
    print("Written to log:   ", this_path, local_address)
    path = str(this_path) + "\\" + local_address 

    if new == True: #create new file
        file = open(path, "w")
        file.write(logMessage)
        file.write("\n")
        file.write("\n")
        file.close()
    else:           #append to log
        file = open(path, "a")
        file.write("  ") 
        file.write("\n") 
        file.write(str(datetime.datetime.now()))
        file.write("   ---   ")
        file.write("  ")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write("Sent Message:     ")
        file.write("   ---   ")
        file.write(logMessage)
        file.write("\n")
        file.write("\n")
        file.write("Original Message:    ")
        file.write(messageRaw)
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.close()




def doDecrypt(Cipher, index, length, raw):

    print("hello2")
    (message, new_index, mode) = applyCipher(Cipher, raw, index, length, False)

    #print("DECRYPTION COPLETE \n\n\n\n\n\n ",message)

    print("decrypting   ",message)
    return message




def doEncrypt(Cipher, index, length, message):


    print("Starting Encryption...")    
    print("Only ASCII characters accepted.") 
    print("")
    
    #quotedlength = round(length / 8) + 1   #how many needed to match the binary message, at 1 denary digit to 8 binary digits
    
    validatedMessage = validateRawText(message)
    #print("Validated message:", validatedMessage, message)

    if index + 1 == length:
        
        writeToLog("No more encryption data, load a new picture", "System_Files\\CONVERSATION LOG2.txt", False)

    else:

        if index > (length - 20):

            writeToLog("Warning, you are running out of characters.", "System_Files\\CONVERSATION LOG2.txt", False)


        ASCIImessage = convertToASCII(validatedMessage)
        print("ASCII MESSAGE:   ",ASCIImessage)
        (ASCIImessage, new_index, mode) = applyCipher(Cipher, ASCIImessage, index, length, True)                 #new custom cipher algorithm
        
        print("Here is your code: ")
        print("")
        print(ASCIImessage, "    ", new_index, len(ASCIImessage))

        writeToLog(ASCIImessage, "NEW MESSAGE.txt", True)
        
        writeToLog(ASCIImessage, "System_Files\\CONVERSATION LOG2.txt", False)
        #print(ASCIImessage)

        truncated_index = len(ASCIImessage)

    return truncated_index
    
    #end else condition for encryption   



def getNewImg(new, old, img_name):

    #new = str(this_path) + "\\" + str(filePaths[0])
    #old = str(parent_path) + "\\" + str(filePaths[0])
    os.remove(old)
    newImgSource = str(current_path) + "\\photo album\\" + str(img_name)
    print(new)
    print(newImgSource)
    os.replace(newImgSource, new)    # (source,destination)
    

    countFilePath = str(current_path) + "\\System_Files\\OTPE2_COUNT.txt"
    file = open(countFilePath, "w")
    file.write("0")
    file.close()

    




#start mainbody-----------------------------------------------------------------------------






    
#ASCII 8 bit printable characters without the "    

import datetime
import os
import pathlib
from PIL import Image 
import numpy as np

charset = "␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟ !'#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~␡ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
print("V4.1.0")
print("Thank you for using Python OTPE")


#replyData = readtxtFile("OTPE02Reply.txt")
#cipherData = readimgFile("image1.jpg")

#Test for the name of file
#reads the image cipher file        returns the boolean array

### Check if image has been changed


#### IMG FILE INTEGRITY VALIDATION >>>>>>>>> 

try:
    current_path = pathlib.Path(__file__).parent.resolve()      #check for the NOTICE
    path = str(current_path) + "\\NOTICE - SEND ME.txt"
    #print(path)
    newImg = open(path, "r")   #Open and read the Notice file data
    dataNewImg = []
    for line in newImg:
        dataNewImg.append(strip(line))

    newImg.close()
    os.remove(path) #remove the notice afterwards

    newImgPath = str(current_path) + "\\" + str(dataNewImg[1])


    for f in os.listdir(current_path):
        if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', 'png'):
            oldimgpath = (os.path.join(current_path, f))

    #print(newImgPath)
    #print(oldimgpath)

    if str(newImgPath) == str(oldimgpath):
        imgpath = oldimgpath

    else:
        imgpath = newImgPath
        getNewImg(newImgPath, oldimgpath,dataNewImg[1])
        #print("New picture loaded and notice deleted.")

except:

    for f in os.listdir(current_path):
            if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg', 'png'):
                oldimgpath = (os.path.join(current_path, f))
    imgpath = oldimgpath
    print("No updates detected.")
    print("\n")


#imgpath always will be parsed:>




### MAIN CODELINE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




#try:                                                        #look for a new file to decrypt (deletes after)

print("Checking Inbox....    ")
this_path = pathlib.Path(__file__).parent.resolve() 
path = str(this_path) + "\\" + "NEW MESSAGE.txt"    #test to see if new message is here
messageFile = open(path, "r")
rawInput = strip(messageFile.read())
messageFile.close()
#os.remove(path)         #close and remove the file
    
print("Starting Decryption...   ")
countFilePath = str(current_path) + "\\System_Files\\OTPE2_COUNT.txt"
file = open(countFilePath, "r")
index = file.read() 


print(rawInput)
ASCII_length = len(rawInput)
print(len(rawInput), index)


print(imgpath)
img = Image.open(open(imgpath, 'rb'))           #get image data in array

bilevel_img = img.convert('L')
bool_array = np.array(bilevel_img)
binary = (bool_array > 127).astype(np.uint8)
sizeArray = bool_array.size
flat_array = bool_array.flatten()

print(flat_array)
print("hello1")
text = doDecrypt(flat_array, index, ASCII_length, rawInput)
message = convertFromASCII(text)
print(message)




  

except:                                                     #encryption open file image file

    print("exception in code")
    quit()

    print("Starting Encryption:    ")
    print(imgpath)
    img = Image.open(open(imgpath, 'rb'))           #get image data in array

    bilevel_img = img.convert('L')
    bool_array = np.array(bilevel_img)
    binary = (bool_array > 127).astype(np.uint8)
    sizeArray = bool_array.size


    flat_array = bool_array.flatten()

    
    this_path = pathlib.Path(__file__).parent.resolve()      #get count
    path = str(this_path) + "\\System_Files\\" + "OTPE2_COUNT.txt"
    #print(path)
    countFile = open(path, "r")
    count = int(countFile.read())
    countFile.close()
    
    this_path = pathlib.Path(__file__).parent.resolve()      #get message
    path = str(this_path) + "\\" + "TYPE YOUR MESSAGE HERE.txt"
    #print(path)
    messageFile = open(path, "r")
    messageRaw = messageFile.read()
    messageFile.close()


    print ("do encrypt in:", flat_array, count, sizeArray, messageRaw)
    new_index = doEncrypt(flat_array, count, sizeArray, messageRaw)
    print("TRIGGERED")


    countFilePath = str(current_path) + "\\System_Files\\OTPE2_COUNT.txt"
    file = open(countFilePath, "w")
    file.write(str(new_index))
    file.close()                    #write new index to the file, 2nd party will have to manually calculate


    





    



#end if for mainbody should execute without delay instantly
print("")
#end = str(input("Are you done with the program? (Y/n): "))#holds the command prompt open.
exit()






