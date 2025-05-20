import random
import string

##Message encoding

msg=input("Enter your message here...")
words=msg.split( )
en_msg=""
##res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=3))
for word in words:
    if(len(word)<3):
        code=word[::-1]
        en_msg=en_msg+" "+code
    else:
        code=''.join(random.choices(string.ascii_letters,k=3))+word[1::]+word[0]+''.join(random.choices(string.ascii_letters,k=3))
        en_msg=en_msg+" "+code

print("Encoded message:"+en_msg)

##message decoding

words=en_msg.split( )
d_msg=""
for word in words:
    if(len(word)<3):
       d_msg=d_msg+" "+word[::-1]
    else:
        d_msg=d_msg+" "+word[-4]+word[3:(len(word)-4)]

print("decoded message:"+d_msg)
