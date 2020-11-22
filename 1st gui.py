from pygame import *
import os
from tkinter import *
from PIL import ImageTk,Image
def s1():
    mixer.init()
    mixer.music.load("lol.ogg")
    mixer.music.play()



def s2():
    mixer.init()
    mixer.music.load("pirates_of_the_caribbean_-_soundtrack.ogg")
    mixer.music.play()



def s3():
    mixer.init()
    mixer.music.load("Lalla_Lalla_Lori_(Welcome_To_Karachi).ogg")
    mixer.music.play()



def s4():
    mixer.init()
    mixer.music.load("Zaroori_Tha_(Rahat_Fateh_Ali_Khan).ogg")
    mixer.music.play()



def s5():
    mixer.init()
    mixer.music.load("lol4.ogg")
    mixer.music.play()



def s6():
    mixer.init()
    mixer.music.load("lol5.ogg")
    mixer.music.play()



def s7():
    mixer.init()
    mixer.music.load("lol6.ogg")
    mixer.music.play()



def s8():
    mixer.init()
    mixer.music.load("lol7.ogg")
    mixer.music.play()


def s9():
    mixer.init()
    mixer.music.load("lol8.ogg")
    mixer.music.play()



def s10():
    mixer.init()
    mixer.music.load("lol9.ogg")
    mixer.music.play()

def st():
    mixer.init()
    mixer.music.stop()

root=Tk()
root.title("MEGA_MUSIC")
root.geometry("900x450")
root.minsize(100,200)
f1=Frame(bd=3,relief=RAISED,bg="grey",width=250)
f1.pack(side=LEFT,fill=Y)
la1=Label(f1,text="Welcome_To_Mega_music",bd=2,relief=SUNKEN,padx=23,bg="black",fg="red",font="chiller 19 italic")
la1.pack(fill=X)
la2=Label(f1,text="Feel The Beat",bd=2,relief=GROOVE,padx=23,bg="BLACK",font="inkfree 19 italic",fg="YELLOW",)
la2.pack(fill=X)
f2=Frame(bg="gray",relief="raised",height=10)
f2.pack(side=TOP,fill=X)

lab4=Label(f2,text="MEGA_MUSIC",bg="black",fg="blue",font="chiller 20 bold",)
lab4.pack(expand=YES,fill=X)
b1=Button(root,bd=6,relief="sunken",text="A UNIQUE LOVE",font="arial 10  bold italic",command=s1,bg="brown")
b1.pack(fill=X)
b2=Button(root,bd=6,relief="sunken",text="pirates_of_the_caribbean",font="arial 10  bold italic",
          cursor="pirate",command=s2,bg="brown")
b2.pack(fill=X)
b3=Button(root,bd=6,relief="sunken",text="Lalla_Lalla_Lori_(Welcome_To_Karachi) ",font="arial 10  bold italic",command=s3,bg="brown")
b3.pack(fill=X)
b4=Button(root,bd=6,relief="sunken",text="Zaroori_Tha_(Rahat_Fateh_Ali_Khan)",font="arial 10  bold italic",command=s4,bg="brown")
b4.pack(fill=X)
b5=Button(root,bd=6,relief="sunken",text="DIL K PASS",font="arial 10  bold italic",command=s5,bg="brown")
b5.pack(fill=X)
b6=Button(root,bd=6,relief="sunken",text="SHIVA THE GRAET",font="arial 10  bold italic",command=s6,bg="brown")
b6.pack(fill=X)
b7=Button(root,bd=6,relief="sunken",text="OLD song",font="arial 10  bold italic",command=s7,bg="brown")
b7.pack(fill=X)
b8=Button(root,bd=6,relief="sunken",text="HASI (hamari adhuri kahani)",font="arial 10  bold italic",command=s8,bg="brown")
b8.pack(fill=X)
b9=Button(root,bd=6,relief="sunken",text="Badri ki Dhulahaniya",font="arial 10  bold italic",command=s9,bg="brown")
b9.pack(fill=X)
b10=Button(root,bd=6,relief="sunken",text="BUlliya",font="impact 10 italic",command=s10,bg="brown")
b10.pack(fill=X)
b11=Button(root,bd=6,relief="sunken",text="PAUSE THE SONGS",font="impact 10 italic",bg="brown",command=st)
b11.pack(fill=X)
root.mainloop()


