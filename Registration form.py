from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0, column=3)

#Field Name
Name=Label(root, text="Name")
Gender=Label(root, text="Gender")
Email=Label(root, text="Email")
Phone=Label(root, text="Phone")
City=Label(root, text="City")
State=Label(root, text="State")

#Packing Fields
Name.grid(row=1, column=2)
Gender.grid(row=2, column=2)
Email.grid(row=3, column=2)
Phone.grid(row=4, column=2)
City.grid(row=5, column=2)
State.grid(row=6, column=2)

#Variable For storing data
Namevalue = StringVar
Gendervalue = StringVar
Emailvalue = StringVar
Phonevalue = StringVar
Cityvalue = StringVar
Statevalue = StringVar
checkvalue =IntVar

#Creating Entry Field
Nameentry = Entry(root, textvariable=Namevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Emailentry = Entry(root, textvariable=Emailvalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
Cityentry = Entry(root, textvariable=Cityvalue)
Stateentry = Entry(root, textvariable=Statevalue)

#Packing Entry field
Nameentry.grid(row=1, column=3)
Genderentry.grid(row=2, column=3)
Emailentry.grid(row=3, column=3)
Phoneentry.grid(row=4, column=3)
Cityentry.grid(row=5, column=3)
Stateentry.grid(row=6, column=3)

#Creating checkbox
checkbtn =Checkbutton(text="Remember me?", variable=checkvalue)
checkbtn.grid(row=7, column=3)

#Submit button
Button(text="Submit", command=getvals).grid(row=8,column=3)

root.mainloop()