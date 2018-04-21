# Rename a large number of files and move them to another file
# Create by Yujiang Fu NEU
# email: marsmarcin@sina.com
import os,shutil
from tkinter import *
import random
import re
window = Tk()
window.title('Rename Files')
window['background'] = 'gray'
window.geometry('520x550+300+300')

Label(window, text='Source File', relief=RIDGE, width=15).grid(row=0, column=0)
Label(window, text='Target File', relief=RIDGE, width=15).grid(row=1, column=0)


entryVar1 = StringVar()
entry1 = Entry(window, textvariable=entryVar1, width=40)
entry1.grid(row=0, column=1)
entryVar1.set('F://get_img//XCQ_Error//') #default Source File


entryVar2 = StringVar()
entry2 = Entry(window, textvariable=entryVar2, width=40)
entry2.grid(row=1, column=1)
entryVar2.set('F://get_img//01//') #default Target File


text_result = Text(window, width=40, height=25)
text_result.grid(row=4, column=1)

def file_name(file_dir):
    dstfile = str(entryVar2.get())
    for root, dirs, files in os.walk(file_dir):
      for file in files:
       str_list = list(file)
       str_list.insert(4, '_')     #insert'_'between the 3th and 4th character
       str_2 = "".join(str_list)
       mycopyfile(file_dir+file,dstfile+str_2)

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #Separate file names and paths
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #Create path
        shutil.copyfile(srcfile,dstfile)      #Copy files



def hitMe():
    srcfilename = str(entryVar1.get())
    srclist = file_name(srcfilename)
    m_result = 'The Mission is over!'
    text_result.insert(1.0, m_result + '\n')

button1 = Button(window, text='Start', width=14, command=hitMe)
button1.grid(row=3, column=0)



mainloop()