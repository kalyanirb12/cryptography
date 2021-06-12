from tkinter import *
import smtplib

import random

#Main Screen Init
master       = Tk()
master.title = 'Custom Email App'

encrypted=""
value=random.randint(1,100)
series="abcdefghijklmnopqrstuvwxyz0123456789!@#$%&"
series+=series.upper()
series+=" "

#Functions



def send():
    try: 
        
        username = temp_username.get()
        password = temp_password.get()
        to       = temp_receiver.get()
        subject  = temp_subject.get()
        
        body = temp_body.get()
        
        
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            notif.config(text="All fields required", fg="red")
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject, enc(body))
            server   = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username,to,finalMessage)
            notif.config(text="Email has been sent successfully", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")

def enc(temp_body):
    #msg=temp_body

    value=random.randint(1,100)
    encrypted=""
    series="abcdefghijklmnopqrstuvwxyz0123456789!@#$%&"
    series+=series.upper()
    series+=" "
    for letter in temp_body:
        position=series.find(letter)
        newp=(position+value)%69
        if letter==" ":
            encrypted+=" "
        else:
            encrypted+=series[newp]
    dec(encrypted, value, series)
    
    return encrypted
    

def dec(encrypted, value, series):
	decrypted=""
	for letter in encrypted:
		position2=series.find(letter)
		newp2= (position2-value)%69
		if letter==" ":
			decrypted+=" "
		else:
			decrypted+=series[newp2]
	print(decrypted)
#dec(encrypted, value, series)






def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete(0,'end')

#Labels
Label(master, text="Custom Email App", font=('Calibri',15)).grid(row=0, sticky=N)
Label(master, text="Please use the form below to send an email", font=('Calibri',11)).grid(row=1, sticky=W, padx=5 ,pady=10)

Label(master, text="Email", font=('Calibri', 11)).grid(row=2,sticky=W, padx=5)
Label(master, text="Password", font=('Calibri', 11)).grid(row=3,sticky=W, padx=5)
Label(master, text="To", font=('Calibri', 11)).grid(row=4,sticky=W, padx=5)
Label(master, text="Subject", font=('Calibri', 11)).grid(row=5,sticky=W, padx=5)
Label(master, text="Body", font=('Calibri', 11)).grid(row=6,sticky=W, padx=5)
notif = Label(master, text="", font=('Calibri', 11),fg="red")
notif.grid(row=7,sticky=S)

#Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject  = StringVar()
temp_body     = StringVar()

#Entries
usernameEntry = Entry(master, textvariable = temp_username)
usernameEntry.grid(row=2,column=0)
passwordEntry = Entry(master, show="*", textvariable = temp_password)
passwordEntry.grid(row=3,column=0)
receiverEntry  = Entry(master, textvariable = temp_receiver)
receiverEntry.grid(row=4,column=0)
subjectEntry  = Entry(master, textvariable = temp_subject)
subjectEntry.grid(row=5,column=0)
bodyEntry     = Entry(master, textvariable = temp_body)
bodyEntry.grid(row=6,column=0)

#Buttons
Button(master, text = "Send", command = send).grid(row=7,   sticky=W,  pady=15, padx=5)
Button(master, text = "Reset", command = reset).grid(row=7,  sticky=W,  padx=45, pady=40)


#Mainloop
master.mainloop()
