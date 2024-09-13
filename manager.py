from tkinter import Tk, Frame, TOP, BOTH, Menu, messagebox
from sqlite import Database

from windows import Login, Register, Container

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("App ejecutable")
        self.geometry("960x540")
        self.menu()
        
        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.configure(bg='green')
        
        self.frames = {}
        for i in (Login, Register, Container):
            frame = i(container, self)
            self.frames[i] = frame
        self.showFrame(Login)
        
    def showFrame(self, container):
        frames = self.frames[container]
        frames.tkraise()
            
    def menu(self):
        menu = Menu()
        items=Menu(menu, tearoff=0)
        items.add_command(label='Crear/Conectar Base de datos.', command=self.createDatabase)
        menu.add_cascade(label='Inicio', menu=items)
        self.config(menu=menu)
        
    def createDatabase(self):
        db=Database()
        try: 
            db.create()
        except:
            messagebox.showerror('Error..!', 'Error al crear la base de datos.')
            raise