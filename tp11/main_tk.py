from tkinter import *
from tkinter import ttk
from UserDAO import UserDAO

def main_hello():
    root = Tk()
    
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)
    
    root.mainloop()


def main():
    dao = UserDAO("./formation.db")
    users = dao.findAll()
    ws = Tk()
    ws.title('Users')
    ws.geometry('800x600')

    tv = ttk.Treeview(ws,show="headings")
    tv['columns']=('Id', 'LastName', 'FirstName')

    tv.column('Id',  anchor=CENTER,stretch=NO)
    tv.column('LastName', anchor=CENTER, width=80)
    tv.column('FirstName', anchor=CENTER, width=80)

    tv.heading('Id', text='Id', anchor=CENTER)
    tv.heading('LastName', text='LastName', anchor=CENTER)
    tv.heading('FirstName', text='FirstName', anchor=CENTER)

    for user in users:
        tv.insert(parent='', index=user.id, iid=user.id, text='', values=(user.id,user.last_name,user.first_name))
    
    tv.pack(fill=BOTH,expand=True)



    ws.mainloop()



if __name__ == '__main__':
    main()
