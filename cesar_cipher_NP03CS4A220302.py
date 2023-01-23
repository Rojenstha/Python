print("Welcome to the Caesar Cipher\nThis program encrypts and decrypts text with the Caesar Cipher.")
while True:
    while True:
        mod=input("Do you want to encrypt or decrypt?(1.encrypt 2.decrypt):  ")
        if(mod=='1' or mod=='2'):
            break
        else:
            print('Invalid mode.')
    txt=input("Enter the text: ")
    while True:
        try:
            s=int(input("Enter the shift number: "))
            break
        except ValueError:
            print('Invalid shift number.')
    def encrypt(txt,s):
        ecp=""
        for i in range(len(txt)):
            char=txt[i]
            if(char.upper()):
                ecp+=chr((ord(char)+s-65)%26+65)
            else:
                ecp+=chr((ord(char)+s-97)%26+97)
        return ecp
    def decrypt(txt,s):
        dcp=""
        for i in range(len(txt)):
            char=txt[i]
            if(char.upper()):
                dcp+=chr((ord(char)-s-65)%26+65)
            elif(char.lower()):
                dcp+=chr((ord(char)-s-97)%26+97)
            else:
                dcp+=' '
        return dcp
    if(mod=='1'):
        print("Encrypt: "+encrypt(txt,s).upper())
    elif(mod=='2'):
        print("Decrypt: "+decrypt(txt,s).upper())
    end=input("Do you want to continue?(yes or no):-  ")
    if(end=='no'):
        print("Thank you for uaing this program!")
        break
