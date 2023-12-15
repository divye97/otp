#import twilio to send messages
from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox
import time
root = Tk()
root.title("OTP Verification")
root.geometry("300x200")
root.configure(bg = "#00FFFF")
def send_otp():
    global n 
    n= random.randint(1000, 9999)
    n=str(n)
    print(n) 
    #create twilio account from twilio.com u get two parameters Account SID and Auth Token   
    client = Client("AC32bf73189a6d964462a3592c4d8c5030","e837dc5c6079064e1f8c9a20dd8c4ef1")
    client.messages.create(to = ["+917877766268"],from_= "+12162382363",body = "hello how are you your one time otp is "+n+".") 
def verify():
    otp = entry1.get()
    if otp == n:
        print("verified")
    else:
        print("you entered wrong otp")
entry1 = Entry(root,width=40)
entry1.place(x=30,y=80)
b1 = Button(root,text="Submit",command = verify)
b1.place(x=170,y=110)
b2 = Button(root,text="send otp",command=send_otp)
b2.place(x=70,y=110)
root.mainloop()