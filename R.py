import tkinter as tk
import sys
import os

root = tk.Tk()
cont1 = tk.Frame(root)
cont1.grid()

# PREDEFINED FUNCTIONS FOR USE IN APP
def retrieveOpass(self):
        opass = self.w0ent1.get()
        print(opass)
        #print("trouble getting entry")

def changePassword(self):
        root0 = tk.Tk()
        cont0 = tk.Frame(root0)
        cont0.grid()
        v=tk.StringVar()
        w0lab1 = tk.Label(cont0,text=" ") #title
        w0lab1.grid(row=1)
        w0lab2 = tk.Label(cont0,text="Old password:")
        w0lab2.grid(row=2,column=0)
        w0ent1 = tk.Entry(cont0,textvariable = v)
        w0ent1.grid(row=2,column=1)
        v.set("a default value")
        w0lab3 = tk.Label(cont0,text="New password:")
        w0lab3.grid(row=3,column=0)
        w0ent2 = tk.Entry(cont0)
        w0ent2.grid(row=3,column=1)
        w0ent2.focus_set()
        npass = w0ent2.get()
        w0but1 = tk.Button(cont0,text="Enter",command=lambda: retrieveOpass(self))
        w0but1.grid(row=4)

        
def retrieveFilename(self):
        # recall wentry1 = tk.Entry(cont1) where cont1 = tk.Frame(root) 
        filename = wentry1.get()
        return filename

def retrieveOutFilename(self):
        # recall w3ent1 = tk.Entry(cont3) = tk.Entry(tk.Frame(root3))
        filename1 = w3ent1.get()
        return filename1

def retrievePassword(self):
        password = wentry2.get()
        return password

def outputFile(self,mystr):
        filetitle = w3ent1.get()
        out_file = open(str(filetitle),'a+')
        out_file.seek(0,0)
        out_file.write(mystr)
        out_file.close()

def displayError(self,mystr):
        root4 = tk.Tk()
        cont4 = tk.Frame(root4)
        cont4.grid()
        w4lab1 = tk.Label(cont4,text=mystr)
        w4lab1.grid()

def badPass(self):
        specialLabel = tk.Label(cont1,text="Wrong Password: Try again")
        specialLabel.grid(row=6)


def goodPass(self):
        specialLabel = tk.Label(cont1,text="Password confirmed")
        specialLabel.grid(row=6)

def displayOriginalText(self,mystr,Off):
        if( Off == False):
                root2 = tk.Tk()
                cont2 = tk.Frame(root2)
                cont2.grid()
                w2lab1 = tk.Label(cont2,text="Preview Text:")
                w2lab1.grid(row=1)
                mystrModified = mystr[:50] +"..."
                w2lab2 = tk.Label(cont2, text=mystrModified)
                w2lab2.grid(row=2)
                newText = encryptAlgorithm(mystr)
                w2but2 = tk.Button(cont2, text="Encrypt/Decrypt",command=lambda: displayFinalText(self,newText))
                w2but2.grid(row=4)

def displayFinalText(self,mystr):
        root3 = tk.Tk()
        cont3 = tk.Frame(root3)
        cont3.grid()
        w3lab1 = tk.Label(cont3,text="Preview New Text:")
        w3lab1.grid(row=1)
        mystrModified = mystr[:50]+"..."
        w3lab2 = tk.Label(cont3, text=mystrModified)
        w3lab2.grid(row=2)
        w3lab3 = tk.Label(cont3, text="Enter output filename:")
        w3lab3.grid(row=3,column=0)
        w3ent1 = tk.Entry(cont3)
        w3ent1.grid(row=3,column=1)
        w3ent1.focus_set()
        w3but1 = tk.Button(cont3,text="Save",command=lambda: outputFile(self,mystr)) #ERROR HERE not customisable
        w3but1.grid(row=3,column=2)
        w3but2 = tk.Button(cont3,text="Exit All",command=lambda: root.quit())
        w3but2.grid(row=4)

def encryptAlgorithm(mystr):

        char_arr = list(mystr)
        #create a dictionary for this part replacing 1 letter with another
        alphabet = ['a','b','c','d','e','f','g','h','i',
                    'j','k','l','m','n','o','p','q','r','s',
                    't','u','v','w','x','y','z']

        #Original Dictionary
        mydict = {}
        x=0
        for let in alphabet:
            mydict[x]=let
            x=x+1

        #Modified Dictionary
        mydict2 = {}
        x=25
        for let in alphabet:
            mydict2[x] = let
            x=x-1

        # Replace letters with corresponding number value from dictionary
        for x in range(len(char_arr)):
                for y in range(26):
                    if(char_arr[x] == mydict[y]):
                            char_arr[x] = y

        #To encrypt replace numbers with corresponding value from modified dictionary
        for x in range(len(char_arr)):
                for y in range(26):
                    if(char_arr[x] == y):
                            char_arr[x] = mydict2[y]

        # PRINTING RESULT
        newText = ''.join(char_arr)

        return newText


def encryptFile(self): #called in first window cont1
        pword = retrievePassword(self)
        Off = False
        if(pword != "123"):
                Off = True #invented variable
                badPass(self)
        else:
                goodPass(self)

        fname = retrieveFilename(self)
        # READING AND DISPLAYING ORIGINAL FILE
        try:
                test_file = open(fname,'r+')
                text = str(test_file.read())
                test_file.close()
        except IOError:
                errorString = "There was an error opening the file!"
                displayError(self,errorString)

        displayOriginalText(self,text,Off)

# DESIGN APPLICATION START

# Window 1
# Features:
# Label: Title: Encryption tool
# Entry: filename
# Button: Ok --> assigns filename variable and opens new window

wlabel1 = tk.Label(cont1, text="Encryption tool")
wlabel1.grid(row=1,column=1)

wlabel2 = tk.Label(cont1, text="Enter filename:")
wlabel2.grid(row=3,column=0)

wentry1 = tk.Entry(cont1)
wentry1.grid(row=3,column=1)
#filename = wentry1.get()

wlabel3 = tk.Label(cont1, text="Enter Password:")
wlabel3.grid(row=4,column=0)

wentry2 = tk.Entry(cont1)
wentry2.grid(row=4,column=1)

wbut2 = tk.Button(cont1,text="Enter")
wbut2.bind("<Button-1>",encryptFile)
wbut2.grid(row=6,column=1)

wbut3 = tk.Button(cont1,text="Change Password")
wbut3.bind("<Button-1>",changePassword)
wbut3.grid(row=7,column=1)
root.mainloop()
