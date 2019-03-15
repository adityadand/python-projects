import upsidedown
import binascii

alphabet = 'abcdefghijklmnopqrstuvwxyz'
inp = input("enter message to encrypt ")
i = int(input("select condition "))




def select(i):
 switcher={
 0:reverse,
 1:updown,
 2:movealpha,
 3:ascii,
 4:binary
 }
 func = switcher.get(i,lambda :'invalid')
 return func()

def reverse():
 print(inp[::-1]);
 
def updown():
 print(upsidedown.transform(inp))
 
def movealpha():
 newmessage=''
 key = int(input("enter no to shift alphabets "))
 for character in inp:
  position = alphabet.find(character)
  newposition = (position+key) % 26
  newcharacter = alphabet[newposition]
  newmessage += newcharacter
 print(newmessage)
 
def ascii():
 print(''.join(str(ord(c)) for c in inp))
 
def binary():
 ' '.join(map(bin,bytearray(inp)))

select(i)


