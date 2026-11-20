#counting script for large binary documents with stripping.
#euan hao


fileCipher = open("cipher(100C)NA234.txt","r")     #maybe in future version update so that it can manually open and empty unlimited amounts of cipher files.
length = 0
counter = 0
End = False


while End == False:


        entry = fileCipher.read(1)
        entry = entry.strip()
        if entry == "1" or entry == "0":
                length = length + 1
                counter = 0

        else:
                counter = counter + 1

                if counter == 15:
                        End = True
                

#endwhile
        
fileCipher.close()



print("done counting, the length is: ", length)
close = input("")
