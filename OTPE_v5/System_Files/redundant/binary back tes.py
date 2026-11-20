charset = "␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟ !'#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~␡ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"




z = " H   E   L   L   O"
x = [72, 154,216, 216, 219]

y = bin(x[0])
y = bin(x[1])
y = bin(x[2])

print(y)
print(charset[72],charset[101], charset[108], charset[108],charset[111])

# -0 -53, -108


#Hello Christina, expect more Tina x Ceres stories soon!ЉЊ

def pad(entry): # pad for Bnab, we pad onto the end due to the way it is read here.
    print("I AM PADDER",entry)
    entry = str(entry)
    while len(entry) < 8:#not len != 6 due to possible infinite loop
        entry = "0" + entry    #now reverse digit order
    #endwhile

    print("I have padded", entry)
    return entry

#endfunction

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
        print("List index   ",charset[list[index]])
    
    print(message)
    return message

#endfunction


#end function
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
                print("ASCII BINARY", ASCII, "ASCII NO,", counter)
        #endfor
            
        #end counter for unicode value
    #end repeat for every character

    
    #print(message, len(message))
    return message

print("KJHSAKJDHASK\n\n\n\n\n")

test = "Hello Christina"




test = convertToASCII(test)
print("ASCIII", test)

test2 = convertFromASCII(test)
print("CONVERTED BACK",test2)





#---


  

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
