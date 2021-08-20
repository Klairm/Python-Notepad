from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.colorchooser import *
import tkinter as tk
import tkinter.filedialog
import os

class Notepad():
	def __init__(self):
	
		def textBackground_color():
			color = askcolor()
			text.configure(bg=color[1])

		

		def background_color():
			color = askcolor()
			window.configure(bg=color[1])
			
			
		def text_input():
			input = text.get("1.0",'end-1c')
			save_file(input)
		
		def save_file(input):
			name =tkinter.filedialog.asksaveasfilename(filetypes = (("txt files","*.txt"),("all files","*.*"),("odt files","*.odt")))
			#return((os.path.basename(name)))
			try:
				file= open(name,"w")
				file.write(input)
				file.close()
			except TypeError:
				pass

			except FileNotFoundError:
				pass
		
		def read_file():
			name = tkinter.filedialog.askopenfilename(filetypes=(("txt files","*.txt"),("all files","*.*"),("odt files","*.odt")))
			file_name =os.path.basename(name)
			l1 = Label(bottom_frame,text=f"Current file: {file_name}",bd=0)
			l1.pack()
			l2 = Label(bottom_frame,text=f"Current directory: {name}",bd=0)
			l2.pack()
			#l1 = Label(top_frame,textvariable=print(read_file()),relief=RAISED)
			try:
				file = open(name,"r")
				content = file.read()
				file.close()
				text.delete('1.0',END)
				
				text.insert(END,content)
			#except TypeError:
				#messagebox.showinfo("TypeError","An error ocurred.")
			except FileNotFoundError:
				pass

		#def title_file():
		#	print(read_file())
		window =Tk()
		# Menu 
		menubar = Menu(window)
		
		filemenu=Menu(menubar,tearoff=0)
		filemenu.add_command(label="Save",command=lambda:text_input())
		filemenu.add_command(label="Open",command=lambda:read_file())
		filemenu.add_command(label="Exit",command=window.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		
		optionsmenu=Menu(menubar,tearoff=0)
		optionsmenu.add_command(label="Background color",command=lambda:background_color())
		optionsmenu.add_command(label="Text Background color",command=lambda:textBackground_color())
		menubar.add_cascade(label="Settings",menu=optionsmenu)

		# Frames for organize the widgets
		top_frame = Frame(window)
		top_frame.pack()
		bottom_frame= Frame(window)
		bottom_frame.pack(side = BOTTOM)
		
		# Window configs
		#window.geometry("500x500")
		window.configure(bg="gray27")
		window.title("Notepad")
		
		# Text and scroll widgets
		text = Text(top_frame,height=60)
		text.pack(side=LEFT)
		scroll = tk.Scrollbar(top_frame,orient="vertical",command=text.yview)
		scroll.pack(side=RIGHT,expand=True,fill="y")
		text.configure(yscrollcommand=scroll.set)
		
		window.attributes('-zoomed', True)
		window.config(menu=menubar)
		window.mainloop()

Notepad()