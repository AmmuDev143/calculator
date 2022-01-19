#importing tkinter
from tkinter import*
#creating function 
def click(event):
#creating global variable
	global scvalue
	text = event.widget.cget("text")
	print(text)
#conditions when we click on "=" button
	if text == "=":
		if scvalue.get().isdigit():
			value=int(scvalue.get())
		else:
			value=eval(entry.get())
			
			scvalue.set(value)
			entry.update()
	
#conditions for clear button
	elif text == "C":
		scvalue.set(" ")
		entry.update()
	else:
		scvalue.set(scvalue.get()+text)
		entry.update()

#taking geometry for screen size		
root=Tk()
root.geometry("400x300")

#label at bottom
Label(root,text="A GUI Calculator\n having abilities to do basic calulation !!",font="cosmicsansm 6 ",fg="gray").pack(side=BOTTOM,pady=30)

#creating string variable and setting it
scvalue=StringVar()
scvalue.set(" ")

#creating the input screen by using entry widget and packing it
entry=Entry(root,textvar=scvalue,font="lucida 20",fg="black")
entry.pack(expand=True,fill=BOTH)

#creating buttons and packing them within the frame1 also binding them 
f=Frame(root)
f.pack()

b=Button(f,text="C",fg="OrangeRed2",font="lucida 20 bold",pady=55,padx=62)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="EX",fg="OrangeRed2",command=quit,pady=82,padx=69)
b.pack(side=LEFT,padx=0,pady=0)

b=Button(f,text="/",fg="OrangeRed2",font="lucida 20 bold",pady=55,padx=72)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="%",fg="OrangeRed2",font="lucida 20 bold",pady=55,padx=60)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

#creating buttons and packing them within the frame2 also binding them 
f=Frame(root)
f.pack()

b=Button(f,text="1",fg="gray",font="lucida 20 ",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="2",fg="gray",font="lucida 20",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="3",fg="gray",font="lucida 20 ",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="+",fg="OrangeRed2",font="lucida 20",padx=65,pady=55)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

#creating buttons and packing them within the frame3 also binding them 
f=Frame(root)
f.pack()

b=Button(f,text="4",fg="gray",font="lucida 20 ",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="5",fg="gray",font="lucida 20",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="6",fg="gray",font="lucida 20 ",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="-",fg="OrangeRed2",font="lucida 20",padx=76,pady=55)
b.pack(side=LEFT)
b.bind("<Button-1>",click)


#creating buttons and packing them within the frame4 also binding them 
f=Frame(root)
f.pack()

b=Button(f,text="7",fg="gray",font="lucida 20 ",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="8",fg="gray",font="lucida 20",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="9",fg="gray",font="lucida 20 ",pady=55,padx=65)
b.pack(side=LEFT,pady=0,padx=0)
b.bind("<Button-1>",click)

b=Button(f,text="*",fg="OrangeRed2",font="lucida 20",padx=70,pady=55)
b.pack(side=LEFT)
b.bind("<Button-1>",click)


#creating buttons and packing them within the frame5 also binding them 
f=Frame(root)
f.pack()

b=Button(f,text="0",fg="gray",font="lucida 15 bold",pady=55,padx=71)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text=".",fg="gray",font="lucida 15 bold",pady=55,padx=79)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

b=Button(f,text="=",bg="OrangeRed2",fg="white",font="lucida 21 bold",pady=41,padx=160)
b.pack(side=LEFT)
b.bind("<Button-1>",click)

root.mainloop()
#end of the program.