#test

#rawInput=str(input("Please input the Encrypted binary message you received: "))#########################################################BUILDING THE NEW VARIABLE CIPHER EXTRACTING
#Input = strip(rawInput)
#length = (len(Input)/8)
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

Input = "111111111111111111111111" #multiple of 8

fileCipher = open("test.txt","r")                            #maybe in future version update so that it can manually open and empty unlimited amounts of cipher files.
Cipher = ""
 
while len(Cipher) != 80: #whilst the cipher hasn't matched the input in length

    chars = ""
    while len(chars) < 8:
        chars = chars + strip(fileCipher.read(1))
    Cipher = Cipher + chars
    print(Cipher)
    print(fileCipher)
          
fileCipher.close()


close = input("")
