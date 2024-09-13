from tkinter import Frame, Entry, Button, Label, END, messagebox
import sqlite3

from sqlite import Database


class Login(Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.pack()
        self.place(x=0, y=0, width=960, height=540)
        self.controller = controller
        self.widgets()

    def login(self):
        with sqlite3.connect("database.db") as connect:
            cursor = connect.cursor()
            query = "SELECT * FROM users WHERE username = ? AND password = ?"
            cursor.execute(query, (self.username.get(), self.password.get()))
            if cursor.fetchall():
                self.success()
            else:
                self.error()
            cursor.close()

    def success(self):
        self.controller.showFrame(Container)

    def error(self):
        self.username.delete(0, END)
        self.password.delete(0, END)
        messagebox.showerror("Error..!", "Credenciales invalidas.")

    def showRegister(self):
        self.controller.showFrame(Register)

    def widgets(self):
        background = Frame(self, bg="CYAN")
        background.pack()
        background.place(x=0, y=0, width=960, height=540)

        self.username = Entry(background)
        self.username.place(x=460, y=250)

        self.password = Entry(background, show="*")
        self.password.place(x=460, y=290)

        loginBtn = Button(
            background,
            bg="blue",
            fg="white",
            text="Iniciar sesion",
            command=self.login,
        )
        loginBtn.place(x=460, y=330)

        loginBtn = Button(
            background,
            bg="blue",
            fg="white",
            text="Registrar usuario",
            command=self.showRegister,
        )
        loginBtn.place(x=520, y=330)


class Register(Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.pack()
        self.place(x=0, y=0, width=960, height=540)
        self.controller = controller
        self.widgets()

    def register(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if self.validate(password):
            self.insert(username, password)

    def validate(self, password):
        if len(password) < 6:
            messagebox.showwarning(
                "Alerta..!", "La contraseña debe ser mayor a 6 caracteres."
            )
            self.passwordEntry.delete(0, END)
            return False
        return True

    def insert(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (?,?)"
        parameters = (username, password)
        Database.query(query, parameters)
        self.success()

    def success(self):
        self.controller.showFrame(Container)

    def widgets(self):
        background = Frame(self, bg="CYAN")
        background.pack()
        background.place(x=0, y=0, width=960, height=540)

        self.usernameLabel = Label(background, text="Nombre de usuario")
        self.usernameLabel.place(x=460, y=210)
        self.usernameEntry = Entry(background)
        self.usernameEntry.place(x=460, y=250)

        self.passwordLabel = Label(background, text="Contraseña")
        self.passwordLabel.place(x=460, y=290)
        self.passwordEntry = Entry(background, show="*")
        self.passwordEntry.place(x=460, y=320)

        loginBtn = Button(
            background, bg="blue", fg="white", text="Registrar", command=self.register
        )
        loginBtn.place(x=520, y=360)


class Container(Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.pack()
        self.place(x=0, y=0, width=960, height=540)
        self.controller = controller
        self.widgets()
        self.frames = {}
        for i in (Sale, Buy):
            frame = i(self)
            self.frames[i] = frame
            frame.pack()
            frame.config(bg="red")
            frame.place(x=0, y=40, width=960, height=540)
        self.showFrame(Sale)

    def widgets(self):
        saleBtn = Button(self, bg="blue", fg="white", text="Ventas", command=self.sale)
        saleBtn.pack()
        saleBtn.place(x=0, y=0, width=300, height=40)

        buyBtn = Button(self, bg="blue", fg="white", text="Compras", command=self.buy)
        buyBtn.pack()
        buyBtn.place(x=310, y=0, width=300, height=40)

    def showFrame(self, container):
        frames = self.frames[container]
        frames.tkraise()

    def sale(self):
        self.showFrame(Sale)

    def buy(self):
        self.showFrame(Buy)


class Sale(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.widgets()

    def widgets(self):
        saleLabel = Label(self, text="Ventas")
        saleLabel.pack()
        saleLabel.place(x=460, y=210)


class Buy(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.widgets()

    def widgets(self):
        buyLabel = Label(self, text="Comnpras")
        buyLabel.pack()
        buyLabel.place(x=460, y=210)
