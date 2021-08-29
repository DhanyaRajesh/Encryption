def encripted(string,shift):
    ciper = ''
    for char in string: 
        if char==' ':
            ciper = ciper+char
        elif char.isupper():
            ciper = ciper+chr((ord(char)+shift-65)%26+65)
        else:
            ciper = ciper+chr((ord(char)+shift-97)%26+97)
    return ciper


def decripted(string,shift):
    ciper = ''
    for char in string: 
        if char==' ':
            ciper = ciper+char
        elif char.isupper():
            ciper = ciper+chr((ord(char)-shift-65)%26+65)
        else:
            ciper = ciper+chr((ord(char)-shift-97)%26+97)
    return ciper    
    

msg = input("Enter the message: ")
s = int(input("Enter the shift value: "))
print("The encrypted message is: ",encripted(msg,s))
encr = encripted(msg,s)
print("The Decrypted message is: ",decripted(encr,s))

