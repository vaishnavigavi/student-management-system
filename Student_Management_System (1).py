from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
from tkinter import ttk
import bs4

def add_btn():
	root.withdraw()
	add_window.deiconify()
def view_btn():
	root.withdraw()
	view_window.deiconify()
	info = ""
	scrolled_text.delete(1.0, END)
	try:
		con = connect("kit.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)	
		data = cursor.fetchall()
		if data == []:
			showinfo("Message", "No record available")
			if con is not None:
				con.close()
			view_window.withdraw()
			root.deiconify()
		else:
			for d in data:
				info = info + "R_no = " + str(d[0]) + ", Name = " + str(d[1]) + ", Marks = " + str(d[2]) + "\n\n"
			scrolled_text.insert(INSERT, info)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
def update_btn():
	root.withdraw()
	update_window.deiconify()

def delete_btn():
	root.withdraw()
	delete_window.deiconify()

def back_add():
	add_window.withdraw()
	root.deiconify()

def back_view():
	view_window.withdraw()
	root.deiconify()

def back_update():
	update_window.withdraw()
	root.deiconify()

def back_delete():
	delete_window.withdraw()
	root.deiconify()
#-----------------------------ADD----------------------------------------------------------------------
def add():
	if (add_window_ent_rno.get() == "" and add_window_ent_name.get() == "" and add_window_ent_marks.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (add_window_ent_rno.get() == ""):
		showerror('OOPS!',"Rollno. cannot be blank")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_name.get() == ""):
		showerror('OOPS!',"Name cannot be blank")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_marks.get() == ""):
		showerror('OOPS!',"Marks cannot be blank")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_rno.get().isalpha() == True):
		showerror('OOPS!',"Roll number can have integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (int(add_window_ent_rno.get()) <= 0) :
		showerror('OOPS!',"Roll number cannot be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (len(add_window_ent_name.get()) < 2):
		showerror('OOPS!',"Name should have atleast two alphabet")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif ((((add_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror('OOPS!',"Name can't consist of digits")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif (add_window_ent_marks.get().isdigit() == False):
		showerror('OOPS!',"Marks can be integers only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif int(add_window_ent_marks.get()) < 0:
		showerror('OOPS!',"Marks can't be negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	elif int(add_window_ent_marks.get()) > 100:
		showerror('OOPS!',"Marks can't be greater than 100")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
	else:
		con = None
		try:
			rno = int(add_window_ent_rno.get())
			name = add_window_ent_name.get()
			marks = int(add_window_ent_marks.get())
			con = connect("kit.db")
			cursor = con.cursor()
			sql = "insert into student values('%d', '%s', '%d')"
			cursor.execute(sql % (rno, name, marks))
			con.commit()
			showinfo("Success", "Record inserted")
			add_window_ent_rno.delete(0, END)
			add_window_ent_name.delete(0, END)
			add_window_ent_marks.delete(0, END)		
		except Exception as e:
			showerror("Issue", e)
			add_window_ent_rno.delete(0, END)
			add_window_ent_name.delete(0, END)
			add_window_ent_marks.delete(0, END)	
		finally:
			if con is not None:
				con.close()
#---------------------------------Update------------------------------------------------------------------------

def update():
	if (update_window_ent_rno.get() == "" and update_window_ent_name.get() == "" and update_window_ent_marks.get() == ""):
		showerror("OOPS!", "Please fill all the details")
	elif (update_window_ent_rno.get() == ""):
		showerror('OOPS!',"Rollno. cannot be blank")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (update_window_ent_name.get() == ""):
		showerror('OOPS!',"Name cannot be blank")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (update_window_ent_marks.get() == ""):
		showerror('OOPS!',"Marks cannot be blank")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (update_window_ent_rno.get().isalpha() == True):
		showerror('OOPS!',"Roll number can have integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (int(update_window_ent_rno.get()) <= 0) :
		showerror('OOPS!',"Roll number can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (len(update_window_ent_name.get()) < 2):
		showerror('OOPS!',"Name should have atleast two alphabet")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif ((((update_window_ent_name.get()).replace(" ","")).isalpha()) == False):
		showerror('OOPS!',"Name can't consist of digits")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif (update_window_ent_marks.get().isdigit() == False):
		showerror('OOPS!',"Marks can be integers only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_marks.get()) < 0:
		showerror('OOPS!',"Marks can't be negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	elif int(update_window_ent_marks.get()) > 100:
		showerror('OOPS!',"Marks can't be greater than 100")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
	else:
		con = None
		try:
			rno = int(update_window_ent_rno.get())
			name = update_window_ent_name.get()
			marks = int(update_window_ent_marks.get())
			con = connect("kit.db")
			cursor = con.cursor()
			sql = "update student set name = '%s', marks = '%d' where rno = '%d'"
			cursor.execute(sql % (name, marks, rno))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("Success", "Details updated successfully")
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_marks.delete(0, END)
			else:
				showwarning('OOPS!',"Record does not exist")
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_marks.delete(0, END)
		except Exception as e:
			showerror("Issue", e)
		finally:
			if con is not None:
					con.close()
#------------------------------------DELETE---------------------------------------------------------------------------
def delete():
	con = None
	if (delete_window_ent_rno.get() == ""):
		showerror('OOPS!',"Please enter roll number")
	elif ((delete_window_ent_rno.get()).isalpha() == True):
		showerror('OOPS!',"Roll number can consist of integers only")
		delete_window_ent_rno.delete(0, END)
	elif (int(delete_window_ent_rno.get()) <= 0):
		showerror('OOPS!',"Roll number can't be negative")
		delete_window_ent_rno.delete(0, END)
	else:
		try:
			con = connect("kit.db")
			cursor = con.cursor()
			rno = int(delete_window_ent_rno.get())
			sql = "delete from student where rno = '%d' "
			cursor.execute(sql % (rno))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("Success", "Student deleted successfully :)")
				delete_window_ent_rno.delete(0, END)
			else:
				showerror("Failure", "Student does not exist")
				delete_window_ent_rno.delete(0, END)
		except Exception as e:
			showerror("Issue", e)
			delete_window_ent_rno.delete(0, END)
		finally:
			if con is not None:
				con.close()
#--------------------------------CHARTS----------------------------------------------------------------------------------
def charts():
	list_marks = []
	list_names = []	
	con=None
	try:
		con=connect('kit.db')
		cursor=con.cursor()
		sql="select marks from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		# print(data)
		for d in data:	
			list_marks.append(int(str(d[0])))
			#print(list_marks)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()

	con=None
	try:
		con=connect('kit.db')
		cursor=con.cursor()
		sql="select name from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		#print(data)
		for d in data:	
			list_names.append(str(d[0]))
		#print(list_names)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()


	plt.bar(list_names, list_marks, width = 0.6, color = ['red', 'green', 'cyan', 'orange'])
	plt.title("Batch Information!")
	plt.xlabel("Students")
	plt.ylabel("Marks")

	plt.show()
#-----------------------------LOCATION_LABEL--------------------------------------
try:
	wa="https://ipinfo.io/"
	res=requests.get(wa)
	#print(res)
	data=res.json()
	city=data['city']
except Exception as e:
	showerror("Issue",e)
#-----------------------------Temperature_Label------------------------------------
try:
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=kalyan"
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	wa = a1 + a2 + a3
	res = requests.get(wa)
	#print(res)
	data = res.json()
	temp = data['main']['temp']
	#print(temp)
except Exception as e:
	print("Issue",e)
#----------------------------------QOTD--------------------------------------------
try:
	wa="https://www.brainyquote.com/quote_of_the_day"
	res=requests.get(wa)
	data = bs4.BeautifulSoup(res.text, 'html.parser')
	#print(data)
	info = data.find('img', {'class' : 'p-qotd'})
	#print(info)
	qotd = info['alt']
	#print(qotd)	
except Exception as e:
	print("Issue",e)
#----------------------------------SMS Window-------------------------------------------
root=Tk()
root.geometry('500x530+400+100')
root.title('Student.Management.System -  Singhaniya')
root.resizable(height=False , width=False)
root.configure(bg='honeydew2')
f=('Calibri',20,'bold ')
f1=('Arial',20)


btn_add=Button(root,text='Add',width=12,font=f,relief='solid',borderwidth=1,command=add_btn)
btn_view=Button(root,text='View',width=12,font=f,relief='solid',borderwidth=1,command=view_btn)
btn_update=Button(root,text='Update',width=12,font=f,relief='solid',borderwidth=1,command=update_btn)
btn_delete=Button(root,text='Delete',width=12,font=f,relief='solid',borderwidth=1,command=delete_btn)
btn_charts=Button(root,text='Charts',width=12,font=f,relief='solid',borderwidth=1,command=charts)
lbl_location=Label(root,text='Location:'+city,pady=5,width=31,font=f1,bg='honeydew2',relief='solid',borderwidth=1,anchor="w")
lbl_temp=Label(root,text='Temp:'+str(temp)+"\u00B0"+"C",padx=15,pady=1,font=f1,bg='honeydew2')
lbl_qotd=Label(root,text='QOTD:'+qotd,width=31,height=3,font=f1,bg='honeydew2',relief='solid',borderwidth=1,anchor="w",wraplength = 500)

btn_add.pack(pady=10)
btn_view.pack(pady=0)
btn_update.pack(pady=10)
btn_delete.pack(pady=0)
btn_charts.pack(pady=10)
lbl_location.place(x=0,y=375)
lbl_temp.place(x=265,y=380)
lbl_qotd.place(x=0,y=423)
#----------------------------------------ADD WINDOW----------------------------------------------------------------------
add_window = Toplevel(root)
add_window.title("Add St.")
add_window.geometry("500x600+400+25")
add_window.configure(bg='lavender')
f=('Calibri',20,'bold ')


add_window_lbl_rno = Label(add_window, text = "Enter roll number", font=f,bg='lavender')

add_window_ent_rno = Entry(add_window, bd = 5, font=f,relief='solid',borderwidth=1)

add_window_lbl_name = Label(add_window, text = "Enter name", font=f,bg='lavender')

add_window_ent_name = Entry(add_window, bd = 5, font=f,relief='solid',borderwidth=1)

add_window_lbl_marks = Label(add_window, text = "Enter marks", font=f,bg='lavender')

add_window_ent_marks = Entry(add_window, bd = 5, font=f,relief='solid',borderwidth=1)

add_window_btn_save = Button(add_window, text = 'Save',font = ('Arial', 19, 'bold'), width = 10, command = add)

add_window_btn_back = Button(add_window, text = 'Back',font = ('Arial', 19, 'bold'), width = 10,command = back_add)


add_window_lbl_rno.pack(pady = 10)
add_window_ent_rno.pack(pady = 10)
add_window_lbl_name.pack(pady = 10)
add_window_ent_name.pack(pady = 10)
add_window_lbl_marks.pack(pady = 10)
add_window_ent_marks.pack(pady = 10)
add_window_btn_save.pack(pady = 5)
add_window_btn_back.pack(pady = 5)

add_window.withdraw()
#---------------------------------------VIEW WINDOW-------------------------------------------------------------------
view_window = Toplevel(root)
view_window.resizable(height=False , width=False)
view_window.title("View student")
view_window.geometry("500x600+400+25")
view_window.configure(bg='yellow')
f=('Calibri',20,'bold ')

scrolled_text = ScrolledText(view_window, width = 40, height = 15, font = ("Arial", 16, "bold"))
view_window_btn_back = Button(view_window, text = 'Back', borderwidth = 9, font=f, width = 10,command = back_view)

scrolled_text.pack(pady = 10)
view_window_btn_back.pack(pady = 10)

view_window.withdraw()
#-------------------------------------------UPDATE WINDOW----------------------------------------------------------------------------------------
update_window = Toplevel(root)
update_window.resizable(height=False , width=False)
update_window.title('Update St.')
update_window.geometry('500x500+400+100')
update_window.configure(bg='peach puff')

update_window_lbl_rno = Label(update_window, text = "Enter roll number", font=f,bg='peach puff')

update_window_ent_rno = Entry(update_window, bd = 5, font=f,relief='solid',borderwidth=1)

update_window_lbl_name = Label(update_window, text = "Enter name", font=f,bg='peach puff')

update_window_ent_name = Entry(update_window, bd = 5, font=f,relief='solid',borderwidth=1)

update_window_lbl_marks = Label(update_window, text = "Enter marks", font=f,bg='peach puff')

update_window_ent_marks = Entry(update_window, bd = 5, font=f,relief='solid',borderwidth=1)

update_window_btn_save = Button(update_window, text = 'Save',font=("Arial",19,'bold'), width = 10,command = update)

update_window_btn_back = Button(update_window, text = 'Back',font=("Arial",19,'bold'), width = 10,command = back_update)


update_window_lbl_rno.pack(pady = 10)
update_window_ent_rno.pack(pady = 10)
update_window_lbl_name.pack(pady = 10)
update_window_ent_name.pack(pady = 10)
update_window_lbl_marks.pack(pady = 10)
update_window_ent_marks.pack(pady = 10)
update_window_btn_save.pack(pady = 5)
update_window_btn_back.pack(pady = 5)


update_window.withdraw()
#---------------------------------DELETE WINDOW-------------------------------------------------------------------------------------
delete_window = Toplevel(root)
delete_window.resizable(height=False , width=False)
delete_window.title('Delete St.')
delete_window.geometry('500x500+400+100')
delete_window.configure(bg='LightSteelBlue1')
f=('Calibri',20,'bold ')

delete_window_lbl_rno = Label(delete_window, text = "Enter roll number", font=f,bg='LightSteelBlue1')
delete_window_ent_rno = Entry(delete_window, bd = 5, font =f,relief='solid',borderwidth=1)
delete_window_btn_save = Button(delete_window, text='Save',font = ('Arial', 19, 'bold'), width = 10,command = delete)
delete_window_btn_back = Button(delete_window, text='Back',font = ('Arial', 19, 'bold'), width = 10,command = back_delete)


delete_window_lbl_rno.pack(pady = 10)
delete_window_ent_rno.pack(pady = 10)
delete_window_btn_save.pack(pady = 5)
delete_window_btn_back.pack(pady =5)

delete_window.withdraw()

#-----------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()















