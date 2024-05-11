# Login  verificacion de datos

from tkinter import Tk, Button, Entry, Label, ttk
from tkinter import StringVar, END, HORIZONTAL, Frame, Toplevel
import time
import connector

class Login(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.user_marcar = "Ingrese su correo"
        self.contra_marcar = "Ingrese su contraseña"
        self.datos = connector.login_datos()
        self.widgets()

    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = ""
        if self.entry2.get() != 'Ingrese su correo':
            self.entry2['show'] = "*"

    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)

        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = "*"

        if self.entry2.get() == 'Ingrese su contraseña':
            self.entry2['show'] = ""

    def salir(self):
        self.master.destroy()
        self.master.quit()

    def acceder_ventana_dos(self):
        for i in range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.02)

        self.master.withdraw()
        self.ventana_dos = Toplevel()
        self.ventana_dos.title('Segunda Ventana')
        self.ventana_dos.geometry('500x500+400+80')
        self.ventana_dos.protocol("WM_DELETE_WINDOW", self.salir)
        self.ventana_dos.config(bg='white')
        self.ventana_dos.state('zoomed')

        Label(self.ventana_dos, text='VENTANA DOS', font='Arial 40', bg='white').pack(expand=True)
        Button(self.ventana_dos, text='Salir', font='Arial 10', bg='red', command=self.salir).pack(expand=True)

    def verification_users(self):
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        users_entry = self.entry1.get()
        password_entry = self.entry2.get()

        if users_entry != self.user_marcar or self.contra_marcar != password_entry:
            users_entry = str("'" + users_entry + "'")
            password_entry = str("'" + password_entry + "'")

            dato1 = self.datos.busca_users(users_entry)
            dato2 = self.datos.busca_password(password_entry)

            self.fila1 = dato1
            self.fila2 = dato2

            if self.fila1 == self.fila2:
                if dato1 == [] and dato2 == []:
                    self.indica2['text'] = 'Contraseña incorrecta'
                    self.indica1['text'] = 'Usuario incorrecto'
                else:
                    if dato1 == []:
                        self.indica1['text'] = 'Usuario incorrecto'
                    else:
                        dato1 = dato1[0][1]

                    if dato2 == []:
                        self.indica2['text'] = 'Contraseña incorrecta'
                    else:
                        dato2 = dato2[0][2]

                    if dato1 != [] and dato2 != []:
                        self.acceder_ventana_dos()
            else:
                self.indica1['text'] = 'Usuario incorrecto'
                self.indica2['text'] = 'Contraseña incorrecta'

    def widgets(self):
        # Usuario y Entry
        Label(self.master, text='Usuario', bg='DarkOrchid1', fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        self.entry1 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey', highlightbackground="#195da2",
                            highlightcolor="green2", highlightthickness=5)
        self.entry1.insert(0, self.user_marcar)
        self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: self.entry_out(self.entry1, self.user_marcar))
        self.entry1.pack(pady=4)

        self.indica1 = Label(self.master, bg='DarkOrchid1', fg='black', font=('Arial', 8, 'bold'))
        self.indica1.pack(pady=2)

        # Contraseña y Entry
        Label(self.master, text='Contraseña', bg='DarkOrchid1', fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        self.entry2 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey', highlightbackground="#195da2",
                            highlightcolor="green2", highlightthickness=5)
        self.entry2.insert(0, self.contra_marcar)
        self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: self.entry_out(self.entry2, self.contra_marcar))
        self.entry2.pack(pady=4)
        self.indica2 = Label(self.master, bg='DarkOrchid1', fg='black', font=('Arial', 8, 'bold'))
        self.indica2.pack(pady=2)

        Button(self.master, text='Iniciar Sesión', command=self.verification_users, activebackground='blue', bg='#195da2', font=('Arial', 12, 'bold')).pack(pady=10)
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TProgressbar", foreground='blue', background='black', troughcolor='DarkOrchid1',
                         bordercolor='#F5F5F5', lightcolor='#F5F5F5', darkcolor='black')
        self.barra = ttk.Progressbar(self.master, orient=HORIZONTAL, length=200, mode='determinate', maximum=100, style="TProgressbar")
        self.barra.pack()
        Button(self.master, text='Salir', bg='DarkOrchid1', activebackground='DarkOrchid1', bd=0, fg='black', font=('Arial', 13, 'italic'), command=self.salir).pack(pady=10)

if __name__ == "__main__":
    ventana = Tk()
    ventana.config(bg='DarkOrchid1')
    ventana.geometry('350x500+500+50')
    ventana.overrideredirect(1)
    ventana.resizable(0, 0)
    app = Login(ventana)
    app.mainloop()
