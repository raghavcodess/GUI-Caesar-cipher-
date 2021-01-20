from tkinter import *

root=Tk()
root.geometry("500x200")
root.title("Caesar Ciphar")
e=Entry(root)
e.insert(0,"Message")

f=Entry(root)
f.insert(1,"Key")

def encrypt():
    text=e.get()
    key=f.get()
    from string import ascii_lowercase
    ar=[] 
    for i in ascii_lowercase:
        ar.append(i)
        br=[]
    for i in range(0,len(text)):
        for j in range(0,len(ar)):
            if text[i]==ar[j]:                 
                br.append(ar[j+key])
            elif text[i]==" ":
                br.append(" ")
                break
    res=""
    res=res.join(br)
    myLabel=Label(root,text=res)
    myLabel.pack()

def decrypt():
    text=e.get()
    key=f.get()
    from string import ascii_lowercase
    ar=[] 
    for i in ascii_lowercase:
        ar.append(i)
        br=[]
    for i in range(0,len(text)):
        for j in range(0,len(ar)):
            if text[i]==ar[j]:                 
                br.append(ar[j-key])
            elif text[i]==" ":
                br.append(" ")
                break
    res=""
    res=res.join(br)
    myLabel=Label(root,text=res)
    myLabel.pack()

e.pack()
f.pack()

myButton1=Button(
    root,
    text="Encrpt",
    command=encrypt)
    
myButton2=Button(
    root,
    text="Decrypt",
    command=decrypt)

myButton1.pack()
myButton2.pack()
root.mainloop()