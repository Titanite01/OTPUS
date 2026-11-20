# Made on 18/11/2026 (updated the 2023 version)
# By Euan H.
# V5 saved as OTPE-v5 
# Title:  One Time Picture Exchange Mailbox
# ASCII 7-Bit for fast speed, with hex 
### pyinstaller version for executables and all related modules
#---------------------------------------------------------------------
#####Example data
#Img file: numpy array:   ['23', '25', '54' ... ]

#Message -                 "Hello Son"    [H.e.l.l.o. .S.o.n]

#Index   -                  9 (characters used)

#oldcharset = "␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟ !'#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~␡ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
#---------------------------------------------------------------------


###    FUNCTIONS    ###-----------------------------------------------

def check_inbox():

    
    try:
               #check for the NOTICE
        path = str(current_path) + "\\NOTICE - SEND ME.txt"
        #print(path)
        newImg = open(path, "r")   #Open and read the Notice file data
        dataNewImg = []
        for line in newImg:
            dataNewImg.append(line.strip()) 

        newImg.close()
        os.remove(path) #remove the notice afterwards

        newImgPath = str(current_path) + "\\" + str(dataNewImg[1])


        for file in os.listdir(current_path):
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', 'png'):
                oldimgpath = (os.path.join(current_path, file))


        if str(newImgPath) == str(oldimgpath):
            imgpath = oldimgpath

        else:
            imgpath = newImgPath
            get_new_img(newImgPath, oldimgpath,dataNewImg[1])
            #print("New picture loaded and notice deleted.")

    except:

        oldimgpath = (current_path + "\\image1.jpg")
        for file in os.listdir(current_path):
                if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg', 'png'):
                    oldimgpath = (os.path.join(current_path, file))
        
        imgpath = (oldimgpath)
        print("No updates detected.")
        print("\n")

    return imgpath
#-



def get_new_img(newPath, oldPath, imgPath):

    os.remove(imgPath)
    os.replace(oldPath, newPath)    # (source,destination)
    
    countFilePath = str(current_path) + "\\System_Files\\OTPE2_COUNT.txt" #update index to be 0 with new img
    file = open(countFilePath, "w")
    file.write("0")
    file.close()




def get_img_data(filename):

    img = Image.open(open(filename, 'rb'))           #get image data in array

    bilevel_img = img.convert('L')
    bool_array = np.array(bilevel_img)
    binary = (bool_array > 127).astype(np.uint8)
    sizeArray = bool_array.size
    flat_array = bool_array.flatten()

    return flat_array
#-


def get_txt_from_file(filename):

     #get message
    messageFile = open(filename, "r")
    messageRaw = messageFile.read()
    messageFile.close()

    return messageRaw
#-


def validateText(input):

    output = ""
    for index in range (len(input)):

        for counter in range (len(charset)):
            if input[index] == charset[counter]:
                output = output + input[index]
                
        #output = output + "␀"   #needs better implementation

    #print(output)
    return output


def get_ascii(text):

    array = []
    for counter in range (len(text)):
        for index in range (len(charset)):
            if charset[index] == text[counter]:
                array.append(index)
    #
    return array
#-


def do_XOR(message, cipher):

    print(message, "\n\n", cipher)
    message_bin = denary_to_binary(message) 
    cipher_bin = denary_to_binary(cipher)

    print("\n\nMessage to be encrypted   ",message_bin, "\n\nCipher in binary  ",cipher_bin,"\n\n")
    #do XOR

    export_bin = ""

    for counter in range (len(message_bin)):
        if message_bin[counter] ==  cipher_bin[counter]:
            export_bin = export_bin + "0"
        else:
            export_bin = export_bin + "1"
        print(message_bin[counter],cipher_bin[counter])
    print("CODE   ",export_bin)

    return export_bin
#-



def crack_XOR(encrypted_bin, cipher):

    encrypted_bin = str(encrypted_bin)
    cipher_bin = denary_to_binary(cipher)
    decrypted_bin = ""

    for counter in range (len(encrypted_bin)):
        if encrypted_bin[counter] == cipher_bin[counter]:
            decrypted_bin = decrypted_bin + "0"
        else:
            decrypted_bin = decrypted_bin + "1"
    
    print("\n\nMessage to crack  ",encrypted_bin,"\n\n\n", "Cipher data  ", cipher_bin,"\n\n\n")
    print("DECODE    ",decrypted_bin)

    return decrypted_bin
#-




def binary_to_denary(binary):

    print(type(binary))
    digits = int(len(binary)/7)
    message = ""

    for index in range(digits):   
            
            value = 64
            denary = 0
    
            for counter in range(7):   #iterate though 7 consecutive chars 
                pointer = index * 7 + counter
                if binary[pointer] == "1":
                    denary = denary + value
    
                value = int(value/2)
            
            #print("Denary  ",denary)

            message = message + charset[denary]
        
    return message
#-


def denary_to_binary(array): #only 7 bits per character

    stack = ""
    for counter in range (len(array)):
        value = bin(array[counter])
        value = str(value[2:len(value)])
        while len(value) < 7:
            value = "0" + value
        
        stack = stack + value

    return stack
#-


def locate_Chunk(message, array, index):   #possibility to make direct comparisons also but its more complex

    length = len(str(message))
    max_length = len(array) -20

    chunk_array = []

    for counter in range (length):
        pointer = int(index) + counter
        chunk_array.append(int(array[pointer]))

    #give warning about file size
    if max_length < int(index):
        write_to_file(current_path + "\\Warning.txt", "You are running low on characters, you should consider a new source image.")
    #-
    return chunk_array
#-


def write_to_log(filename, message, status):

    file = open(filename, "a")
    file.write("\n") 
    file.write("\n") 
    file.write(str(datetime.datetime.now()))
    file.write("     ---      ")
    file.write("  ")
    file.write("\n")
    file.write("\n")
    file.write("\n ")
    status = status + " Message:       "
    file.write(status)
    file.write("   ---   ")
    file.write("\n")
    file.write(message)
    file.write("\n")
    file.write("\n")
    file.write("Original Message:      ")
    file.write(raw_message)
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.close()
#-


def write_to_file(filename, data):

    file = open(filename, "w")
    file.write(data)
    file.close()
#-


def delete_reply(filename):

    os.remove(filename)

#-



###     START MAIN      ###----------------------------------------------------------------------



import datetime
import os
import pathlib
from PIL import Image 
import numpy as np


print("V5.1.0")
print("Thank you for using Python OTPE")
print("THIS IS THE DEBUGGER")


#-------
current_path = str(pathlib.Path(__file__).parent.resolve())
mode = ""
charset = " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~\\"
#length = 93*
#parent_path = 
#-------


imgpath = check_inbox()
index = int(get_txt_from_file(current_path + "\\System_Files\\OTPE2_COUNT.txt"))
print("index:    ",index)

try:
    in_message = get_txt_from_file(current_path + "\\NEW MESSAGE.txt") #check for new messages
    mode = "decrypt"
except:
    mode = "encrypt"
print(mode)



if mode == "encrypt":


    raw_message = get_txt_from_file(current_path + "\\MAILBOX.txt")
    out_message = validateText(raw_message)
    
    letter_array = get_ascii(out_message)
    new_index = index + len(letter_array) 

    cipher_array = get_img_data(imgpath)
    cipher_chunk = locate_Chunk(out_message, cipher_array, index)


    output = do_XOR(letter_array, cipher_chunk)
    output = "1" + output #1 is a signed bit, to help with compression to HEX
    output = int(output)
    compressed_output = hex(output)
    
    write_to_file(current_path + "\\System_Files\\OTPE2_COUNT.txt", str(new_index))
    write_to_file(current_path + "\\NEW MESSAGE.txt",compressed_output)
    write_to_log(current_path +"\\System_Files\\CONVERSATION LOG2.txt", str(output),"Sent")

    print("output    ",output, "\n\n", compressed_output)

else:   #decrypt


    raw_message = get_txt_from_file(current_path + "\\NEW MESSAGE.txt")
    in_message = raw_message
    message_bin = int(in_message, 16) #decode hex
    message_bin = str(message_bin)
    message_bin = message_bin[1:len(message_bin)] #remove the signed bit 

    cipher_array = get_img_data(imgpath)   #now locate the origin index from index - length
    message_length = int(len(str(message_bin))/7)  #message len in terms of chars
    new_index = index + (message_length)
    
    dummy_message = int(1 * (10 ** message_length)) #make a dummy message length of the original characters
    cipher_chunk = locate_Chunk(dummy_message, cipher_array, index) #get cipher chunk
    message = crack_XOR(message_bin, cipher_chunk)
    message = binary_to_denary(message)

    write_to_file(current_path + "\\MAILBOX.txt", message)
    write_to_log(current_path +"\\System_Files\\CONVERSATION LOG2.txt", message, "Received")
    delete_reply(current_path + "\\NEW MESSAGE.txt")
    
    
    print("")


###  END  ###--------------------------------------------------------------------------------------

