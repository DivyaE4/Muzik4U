# Import the required libraries
from tkinter import *
from tkinter import ttk
import qrcode
import random

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("1000x450")
win['background']='#856ff8'
heading=Label(win,text='Miuzik4U',font=("Arial Black ",50,"bold"),bg='#856ff8').pack(padx=10,pady=20)

def Tamil_list(lines):
    Tamil_list=[]
    for i in lines:
        line=i.split()
        if line[2]=="TAMIL":
            Tamil_list.append(line[0])
    return Tamil_list
 
def Hindi_list(lines):
    Hindi_list=[]
    for i in lines:
        line=i.split()
        if line[2]=="HINDI":
            Hindi_list.append(line[0])
    return Hindi_list
 
def Telugu_list(lines):
    Telugu_list=[]
    for i in lines:
        line=i.split()
        if line[2]=="TELUGU":
            Telugu_list.append(line[0])
    return Telugu_list
 
def Kannada_list(lines):
    Kannada_list=[]
    for i in lines:
        line=i.split()
        if line[2]=="KANNADA":
             Kannada_list.append(line[0])
    return  Kannada_list

def SongFile(language,genre):
    if genre=="GENRE":
        file=''
    if genre=="MELODY":
        file="D://comp project music details/MELODY.txt"
    elif genre=="ENERGETIC":
        file="D://comp project music details/ENERGETIC.txt"
    elif genre=="EMOTIONAL":
        file="D://comp project music details/EMOTIONAL.txt"
    elif genre=="CLASSICAL":
        file="D://comp project music details/CLASSICAL.txt"
    with open(file,"r") as f:
        lines=f.readlines() 
        f.close()
        #url name language 
        if language=="TAMIL":
            langlist=Tamil_list(lines)
        elif language=="HINDI":
            langlist=Hindi_list(lines)
        elif language=="TELUGU":
            langlist=Telugu_list(lines)
        elif language=="KANNADA":
            langlist=Kannada_list(lines)
        a=random.randint(0,len(langlist)-2)
        return langlist[a] #random url with language specification
 
def QrCode(Url):
    url = qrcode.make(Url)
    url.show()
 
#play here embedding video
#def embeddingVideo(url):
    
 
#add songs
def AddSongs(song):
    with open("ADDSONGS.txt","a") as f:
        f.append(song+'\n')
# Create a function to clear the combobox
def clear_cb():
    cb.set('')
    gr.set('')
   
# Define Days Tuple
lang= ("TAMIL","TELUGU","KANNADA","HINDI")
genr=("MELODY","EMOTIONAL","ENERGETIC","CLASSICAL")

# Function to print the index of selected option in Combobox
def proceed(language,genre):
    url=SongFile(language,genre)
    if genre!="GENRE":
        QrCode(url)
   
def callback(*arg):
    language=cb.get()
    genre=gr.get()
    print(language,genre)
    proceed(language,genre)
   

# Create a combobox widget
var= StringVar()
cb= ttk.Combobox(win,width=10,textvariable= var)
cb['values']= lang
cb['state']= 'readonly'
cb.set('LANGUAGE')
cb.pack(fill='x',padx= 5, pady=5)
gen= StringVar()
gr= ttk.Combobox(win,width=10,textvariable= gen)
gr['values']= genr
gr['state']='readonly'
gr.set('GENRE')
gr.pack(fill='x',padx= 15, pady=5)

# Set the tracing for the given variable
var.trace('w', callback)
gen.trace('w',callback)
    
    
# Create a button to clear the selected combobox text value
button= Button(win, text= "Clear", command= clear_cb)
button.pack()


win.mainloop()