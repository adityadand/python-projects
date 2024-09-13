import requests , sys, webbrowser, bs4
from bs4 import BeautifulSoup
import string
import random


webext = ['.in','.com,','.org']


#note i dont take responsibility of this tool if something happens to your system or your messed up

def drivegenerator(size=26, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def megagenerator1(size=8, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def megagenerator2(size=22, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def pastebingen(size=8, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))
 
def mediafiregen(size=15, chars=string.digits+string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def dropboxgen1(size=15, chars=string.digits+string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def dropboxgen2(size=25, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def warandomcontact(size=10, chars=string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def telegramrandom(size=6, chars=string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def githubrandom(size=3, chars=string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def twitterrandom(size=4, chars=string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def instarandom(size=5, chars=string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def facebookrandom(size=2, chars=string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

def spotifyrandom(size=4, chars=string.ascii_lowercase):
   return ''.join(random.choice(chars) for _ in range(size)) 

def randomwebsite(size=4, chars=string.ascii_lowercase):
   return ''.join(random.choice(chars) for _ in range(size)) 

def randomyoutubeusr(size=2, chars=string.ascii_lowercase):
   return ''.join(random.choice(chars) for _ in range(size))

def imgur(size=5, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def imgurgallery(size=7, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def imguralbum(size=5, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def youtubevidrandom(size=11, chars=string.digits+string.ascii_lowercase+string.ascii_uppercase):
  return ''.join(random.choice(chars) for _ in range(size))

def pininterestrandom(size=17, chars=string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def zoomclass(size=8, chars=string.digits):
  return ''.join(random.choice(chars) for _ in range(size))


def back():
    print("do you want to go back and try other options")
    inp = input()
    if(inp[0] == "y"):
        printdef()
        chooseoption()
    else:
        exit();
        


def chooseoption():
    print("do you want to run single time or multiple times")
    inp = input()
    if(inp[0] == "m"):
        multichooseit()
    else:
        chooseit()

def printdef():
 #i do not gurantee that this tool will work
 print("what do you want to random generate link of")
 print("1. google drive")
 print("2. mega")
 print("3. pastebin")
 print("4. reddit")
 print("5. random website ")
 print("6. generate random youtube channel link")
 print("7. mediafire")
 print("8. dropbox")
 print("9. contact a random person on whatsapp")
 print("10. generate random telegram link")
 print("11. generate random github user link")
 print("12. generate random twitter user link")
 print("13. generate random instagram user link")
 print("14. generate random facebook page or user link")
 print("15. random spotify playlist / profile search")
 print("16. imgur")
 print("17. youtube video")
 print("18. pininterest")
 print("19. imgur albums")
 print("20. imgur gallery")
 print("21. random wikipedia pages")
 print("22. zoom class codes")

def chooseit():
 print("choose any option")
 cho = int(input())
 if(cho == 1): 
     webbrowser.open("https://drive.google.com/drive/folders/0B"+drivegenerator())
     back()
 if(cho == 2):
     webbrowser.open("https://mega.nz/#F!"+megagenerator1()+"!"+megagenerator2())
     back()
 if(cho == 3):
     webbrowser.open("https://pastebin.com/"+pastebingen())
     back()
 if(cho == 4):
     webbrowser.open("https://www.reddit.com/r/random")
     back()
 if(cho == 5):
     webbrowser.open("www."+randomwebsite()+webext[random.randint(0, 2)])
     back()
 if(cho == 6):
     webbrowser.open("https://www.youtube.com/"+randomyoutubeusr())
     back()
 if(cho == 7):
     webbrowser.open("https://www.mediafire.com/file/"+mediafiregen()+"/")
     back()
 if(cho == 8):
     webbrowser.open("https://www.​dropbox.​com/sh/"+dropboxgen1()+"/"+dropboxgen2()+"?dl=0")
     back()
 if(cho == 9):
     webbrowser.open("https://wa.me/"+warandomcontact())
     back()
 if(cho == 10):
     webbrowser.open("https://t.me/"+telegramrandom())
     back()
 if(cho == 11):
     webbrowser.open("https://www.github.com/"+githubrandom())
     back()
 if(cho == 12):
     webbrowser.open("https://www.twitter.com/"+twitterrandom())
     back()
 if(cho == 13):
     webbrowser.open("https://www.instagram.com/"+instarandom())
     back()
 if(cho == 14):
     webbrowser.open("https://www.facebook.com/"+facebookrandom())
     back()
 if(cho == 15):
     webbrowser.open("https://open.spotify.com/search/results/"+spotifyrandom())
     back()
 if(cho == 16):
     webbrowser.open("http://i.imgur.com/"+imgur()+".jpg")
     back()
 if(cho == 17):
     webbrowser.open("https://www.youtube.com/watch?v="+youtubevidrandom())
     back()
 if(cho == 18):
     webbrowser.open("https://in.pinterest.com/pin/"+str(random.randint(1,7))+pininterestrandom())
     back()
 if(cho == 19):
     webbrowser.open("http://imgur.com/a"+imguralbum())
     back()
 if(cho == 20):
     webbrowser.open("http://imgur.com/gallery"+imgurgallery())
     back()
 if(cho == 21):
     webbrowser.open("https://en.wikipedia.org/wiki/Special:Random")
     back()
 if(cho == 22):
     webbrowser.open("https://us02web.zoom.us/j/"+zoomclass())
     back()

     

def multichooseit():
 print("choose any option")
 cho = int(input())
 print("choose no of times to run it")
 tme = int(input())
 if(cho == 1): 
    for x in range(tme):
       webbrowser.open("https://drive.google.com/drive/folders/0B"+drivegenerator())
    back()
 if(cho == 2):
    for x in range(tme):
      webbrowser.open("https://mega.nz/#F!"+megagenerator1()+"!"+megagenerator2())
    back()
 if(cho == 3):
    for x in range(tme):
     webbrowser.open("https://pastebin.com/"+pastebingen())
    back()
 if(cho == 4):
    for x in range(tme):
     webbrowser.open("https://www.reddit.com/r/random")
    back()
 if(cho == 5):
    for x in range(tme):
     webbrowser.open("www."+randomwebsite()+webext[random.randint(0, 2)])
    back()
 if(cho == 6):
    for x in range(tme):
     webbrowser.open("https://www.youtube.com/"+randomyoutubeusr())
    back()
 if(cho == 7):
    for x in range(tme):
     webbrowser.open("https://www.mediafire.com/file/"+mediafiregen()+"/")
    back()
 if(cho == 8):
    for x in range(tme):
     webbrowser.open("https://www.​dropbox.​com/sh/"+dropboxgen1()+"/"+dropboxgen2()+"?dl=0")
    back()
 if(cho == 9):
    for x in range(tme):
     webbrowser.open("https://wa.me/"+warandomcontact())
    back()
 if(cho == 10):
    for x in range(tme):
     webbrowser.open("https://t.me/"+telegramrandom())
    back()
 if(cho == 11):
    for x in range(tme):
     webbrowser.open("https://www.github.com/"+githubrandom())
    back()
 if(cho == 12):
    for x in range(tme):
     webbrowser.open("https://www.twitter.com/"+twitterrandom())
    back()
 if(cho == 13):
    for x in range(tme):
     webbrowser.open("https://www.instagram.com/"+instarandom())
    back()
 if(cho == 14):
    for x in range(tme):
     webbrowser.open("https://www.facebook.com/"+facebookrandom())
    back()
 if(cho == 15):
    for x in range(tme):
     webbrowser.open("https://open.spotify.com/search/results/"+spotifyrandom())
    back()
 if(cho == 16):
    for x in range(tme):
     webbrowser.open("http://i.imgur.com/"+imgur()+".jpg")
    back()
 if(cho == 17):
    for x in range(tme):
     webbrowser.open("https://www.youtube.com/watch?v="+youtubevidrandom())
    back()
 if(cho == 18):
    for x in range(tme):
     webbrowser.open("https://in.pinterest.com/pin/"+str(random.randint(1,7))+pininterestrandom())
    back()
 if(cho == 19):
    for x in range(tme):
     webbrowser.open("http://imgur.com/a/"+imguralbum())
    back()
 if(cho == 20):
    for x in range(tme):
     webbrowser.open("http://imgur.com/gallery/"+imgurgallery())
    back()
 if(cho == 21):
    for x in range(tme):
     webbrowser.open("https://en.wikipedia.org/wiki/Special:Random")
    back()
 if(cho == 22):
    for x in range(tme):
     webbrowser.open("https://us02web.zoom.us/j/5"+zoomclass())
    back()


 

def start():
 printdef()
 chooseoption()
 chooseit()

start()