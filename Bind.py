from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ast

root = Tk()
root.title("Signin page")
root.geometry('925x500+200+100')
root.config(bg ='#fff')
root.resizable(False,False)

def sign_in():
    username  = user.get()
    Password = code.get()

    file =open("datasheet.txt","r")
    d = file.read()
    r= ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())

    if username in r.keys() and Password == r[username]:
        screen = Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg ='white')
        
        Label(screen,text='Hello EveryOne', bg = '#fff', font= ('Calibari(Body)',50,'bold')).pack(expand=True)
        
        screen.mainloop()
        
    else:
        messagebox.showerror("Invalid","invalid username or password")
        
def sign_up():

    window = Toplevel(root)
    window.title("SignUp page")
    window.geometry('925x500+200+100')
    window.config(bg ='#fff')
    window.resizable(False,False)

    def signup():
        username = user.get()
        password = code.get()
        conferm_password = conferm_code.get()

        if password == conferm_password:
            try:
                file= open("datasheet.txt","r+")
                d= file.read()
                r = ast.literal_eval(d)
                
                dict2 = {username:password}
                r.update(dict2)
                file.truncate(0) 
                file.close()

                file = open('datasheet.txt','w')
                w= file.write(str(r))
                messagebox.showinfo('SignUp',"Sign Up Sucessfully")

            except:
                file= open("datasheet.txt","w")
                pp = str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid',"Both password should match")
    def sign():
        window.destroy()

    Image = PhotoImage(file='signout.png')
    Label(window,image=Image,bg = "white").place(x=50,y=80)
    frame = Frame(window,width=350,height=350,bg = 'white').place(x=480, y=70)

    heading = Label(window, text="Sign Up", fg ='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=600,y =75)


    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(window, width=37, fg = 'black',border = 0,bg = 'white',font=('Microsoft YaHei UI Light',11))
    user.place(x=550,y =150)
    user.insert(0, 'User name')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(window, width=298, height=2, bg = 'black').place(x=550,y =175)

    # __________________________________________________

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    code = Entry(window, width=37, fg = 'black',border = 0,bg = 'white',font=('Microsoft YaHei UI Light',11))
    code.place(x=550,y =210)
    code.insert(0, 'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    Frame(window, width=298,height=2,bg = 'black').place(x=550,y =235)

    # __________________________________________

    def on_enter(e):
        conferm_code.delete(0, 'end')

    def on_leave(e):
        name = conferm_code.get()
        if name == '':
            conferm_code.insert(0, 'Conform Password')

    conferm_code = Entry(window, width=37, fg = 'black',border = 0, bg = 'white', font=('Microsoft YaHei UI Light',11))
    conferm_code.place(x=550,y =270)
    conferm_code.insert(0, 'Conform Password')
    conferm_code.bind('<FocusIn>',on_enter)
    conferm_code.bind('<FocusOut>',on_leave)

    Frame(window, width=298,height=2,bg = 'black').place(x=550,y =295)

    Button(window, width=39, pady=7,text='Sign Up', bg = '#57a1f8', fg ='white', border=0, command = signup).place(x=564,y=334)
    label = Label(window,bg='white',fg = 'black', text = "I have an account?", font=('Microsoft YaHei UI Light',9))
    label.place(x=620,y=390)

    # ______________________________________________

    sign_in = Button(window, width=6,text='Sign in', bg = 'white', cursor='hand2',border=0, fg = '#57a1f8', command=sign)
    sign_in.place(x=730,y=390)

    window.mainloop()

Image = PhotoImage(file='login.png')
Label(root,image=Image,bg = "white").place(x=50,y=50)

frame1 = Frame(root,width=350,height=350,bg = 'white').place(x=480, y=70)

heading = Label(frame1, text="Sign in", fg ='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=600,y =75)

# ________________________________________

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame1, width=37, fg = 'black',border = 0,bg = 'white',font=('Microsoft YaHei UI Light',11))
user.place(x=550,y =150)
user.insert(0, 'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame1, width=298, height=2, bg = 'black').place(x=550,y =175)

# #________________________________________

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame1, width=37, fg = 'black',border = 0,bg = 'white',font=('Microsoft YaHei UI Light',11))
code.place(x=550,y =210)
code.insert(0, 'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame1, width=298,height=2,bg = 'black').place(x=550,y =235)

#________________________________________

Button(frame1, width=39, pady=7,text='Sign in', bg = '#57a1f8', fg ='white',border=0,command=sign_in).place(x=564,y=264)
label = Label(frame1, bg='white',fg = 'black', text = "Don't have an account?", font=('Microsoft YaHei UI Light',9))
label.place(x=600,y=328)

#________________________________________

sign_up = Button(frame1, width=6,text='Sign Up', bg = 'white', cursor='hand2',border=0, fg = '#57a1f8',command= sign_up)
sign_up.place(x=738,y=328)
root.mainloop()




