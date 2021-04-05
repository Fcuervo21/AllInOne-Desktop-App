from tkinter import*
from tkinter import messagebox
import json
from random import choice, randint, shuffle
import pyperclip
import math
import time

class Pantalla(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(width = 500, height = 700, bg = "#e6cb7a")

        self.btn_salir = Button(self, text = "Salir", font = ("Bahnschrift", 20, "bold"))
        self.btn_salir.config(command = lambda:self.cerrar_aplicacion(master))
        self.btn_salir.place(relx = 0.80, rely = 0.9)

        # Montamos el contenedor (pantalla)
        self.pack()

    # Metodo de la super clase para cerrar
    def cerrar_aplicacion(self, padre):
        padre.destroy()



class pantalla_inicio(Pantalla):
    def __init__(self, master):
        super().__init__(master)

        # Titulo de la pantalla
        self.label_titulo_inicio = Label(self, text = "All In One Desk",font = ("Arial", 30), bg = "#e6cb7a")
        self.label_titulo_inicio.place(relx = 0.2, rely = 0.1)

        # Boton de ingreso
        self.boton_pass_manager = Button(self, text="Password Manager", bg="gold", command = lambda:self.cambio_a_manager(master))
        self.boton_pass_manager.config(font = ("arial",16))
        self.boton_pass_manager.place(relx = 0.1, rely = 0.5, relwidth = 0.4)

        # Boton de registro
        self.boton_pomodoro = Button(self, text="Pomodoro Timer", bg="gold", command = lambda:self.cambio_a_pomodoro(master))
        self.boton_pomodoro.config(font = ("arial",16))
        self.boton_pomodoro.place(relx = 0.5, rely = 0.5, relwidth = 0.4)

    # Funcion para cambiar a la pantalla de inicio de sesion
    def cambio_a_manager(self, padre):
        self.destroy()
        manager = pantalla_manager(padre)

    # Funcion para cambiar a la pantalla de inicio de registro
    def cambio_a_pomodoro(self, padre):
        self.destroy()
        registro = pantalla_pomodoro(padre)



class pantalla_manager(Pantalla):
    def __init__(self, master):
        super().__init__(master)

        # Titulo de la pantalla
        self.titulo_password = Label(self, text = "Password Manager", font = ("Corbel",23, "bold"), fg = "#2c3e50", bg = "#e6cb7a")
        self.titulo_password.place(relx = 0.25, rely = 0.2)

        # Etiqueta Website-------------------
        self.label_website = Label(self, text = "Website", font = ("Corbel", 16, "bold"), fg = "#2980b9", bg = "#e6cb7a")
        self.label_website.place(relx = 0.42, rely = 0.3)

        self.website_entry = Entry(self, font = ("Corbel", 15), bg = "white", justify = "center")
        self.website_entry.place(relx = 0.25, rely = 0.35, relwidth = 0.5)

        self.boton_busqueda = Button(self, text = "Search", bg = "#45b39d", fg = "white", font = ("Corbel",10, "bold"), command = self.find_password)
        self.boton_busqueda.place(relwidth = 0.2, relx = 0.77, rely = 0.35)
        #-------------------------------------

        #Etiqueta email-----------------------
        self.label_email = Label(self, text = "Email", font = ("Corbel", 16, "bold"), fg = "#2980b9", bg = "#e6cb7a")
        self.label_email.place(relx = 0.44, rely = 0.4)

        self.email_entry = Entry(self, font = ("Corbel", 12), bg = "white", justify = "center")
        self.email_entry.place(relx = 0.25, rely = 0.45, relwidth = 0.5)
        self.email_entry.insert(0, "@gmail.com")
        #--------------------------------------

        #Etiqueta password---------------------
        self.label_password = Label(self, text = "Password", font = ("Corbel", 16, "bold"), fg = "#2980b9", bg = "#e6cb7a")
        self.label_password.place(relx = 0.41, rely = 0.5)

        self.password_entry = Entry(self, font = ("Corbel", 15), bg = "white", justify = "center")
        self.password_entry.place(relx = 0.25, rely = 0.55, relwidth = 0.5)

        self.generate_password = Button(self, text = "Generate Password", bg = "#45b39d", fg = "white", font = ("Corbel",10, "bold"), command = self.generar_contrasena)
        self.generate_password.place(relwidth = 0.22, relx = 0.77, rely = 0.55)
        #--------------------------------------

        #Boton Add-----------------------------
        self.anadir_password = Button(self, text = "Add", bg = "#45b39d", fg = "white", font = ("Corbel",17, "bold"), command= self.save_password)
        self.anadir_password.place(relwidth = 0.5, relx = 0.25, rely = 0.7)
        #--------------------------------------

        #Boton regresar a menu-----------------
        self.btn_menu = Button(self, text = "Menu principal", font = ("arial",12, "bold"), command = lambda: self.ir_a_menu(master))
        self.btn_menu.place(relx = 0.1, rely = 0.1)
        #-------------------------------------

    # Metodo para ir a la pantalla principal
    def ir_a_menu(self, padre):
        self.destroy()
        p_inicio = pantalla_inicio(padre)

    def generar_contrasena(self):
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numeros  = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letras = [choice(letras) for i in range(randint(8 , 10))]
        password_symbol = [choice(simbolos) for i in range(randint(2, 4))]
        password_number = [choice(numeros) for i in range(randint(2, 4))]
        final_password = password_letras + password_symbol + password_number

        shuffle(final_password)
        password = "".join(final_password)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)
    
    def save_password(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_data = {
            website:{
                "email": email,
                "password":password
                }
            }

        if len(website) == 0 or len(password) ==0:
            messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
        else:
            try:
                with open('data.json', 'r') as data_file:
                    #Redading olda data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #updating old data
                data.update(new_data)

                with open('data.json', 'w') as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                    self.website_entry.delete(0, END)
                    self.password_entry.delete(0, END)
    
    def find_password(self):
        website = self.website_entry.get()
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists")


class pantalla_pomodoro(Pantalla):
    def __init__(self,master):
        super().__init__(master)


        # Titulo pomodoro
        self.mensaje = Label(self, text = "Pomodoro Timer", font = ("Corbel",25, "bold"), fg = "#2c3e50", bg = "#e6cb7a")
        self.mensaje.place(relx = 0.28, rely = 0.15)
        # Canvas tomate
        self.canvas_tomato = Canvas(self, bg="#e6cb7a",  highlightthickness=0)
        self.imagen = PhotoImage(file = "tomato.png")
        self.canvas_tomato.create_image(100, 130, image=self.imagen)
        self.timer_text = self.canvas_tomato.create_text(100, 140, text="00:00", font = ("Courier", 25, "bold"))
        self.canvas_tomato.place( relx = 0.3, rely = 0.3)

        #Label Timer
        self.timer_label = Label(self, text="Timer", font = ("Courier", 35, "bold"), fg="#4da16f", bg="#e6cb7a", highlightthickness=1)
        self.timer_label.place(relx = 0.37, rely = 0.23)

        #Label check marks
        self.check_marks = Label(self, fg="#4da16f", bg="#e6cb7a")
        self.check_marks.place(relx = 0.3, rely = 0.85)

        # Boton Inicio tiempo
        self.btn_registro = Button(self, text="Start", font = ("Corbel", 14), highlightthickness=1, command = self.start_timer)
        self.btn_registro.place(relx = 0.2, rely = 0.7)
        # Boton Reiniciar tiempo
        self.btn_registro = Button(self, text="Restart", font = ("Corbel", 14), highlightthickness=1, command = self.reset_timer)
        self.btn_registro.place(relx = 0.7, rely = 0.7)

        # Boton para ir a pantalla de principal
        self.btn_menu = Button(self, text = "Menu principal", font = ("arial",12), command = lambda: self.ir_a_menu(master))
        self.btn_menu.place(relx = 0.1, rely = 0.1)


    # Metodo para ir a la pantalla principal
    def ir_a_menu(self, padre):
        self.destroy()
        p_inicio = pantalla_inicio(padre)

    def reset_timer(self):
        root.after_cancel(timer)
        self.canvas_tomato.itemconfig(self.timer_text, text="00:00")
        self.timer_label.config(text="Timer")
        self.check_marks.config(text="")
        global reps
        reps = 0

    # Metodo start timer
    def start_timer(self):
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        self.count_down(work_sec)
        if reps % 8 == 0:
            self.count_down(long_break_sec)
            self.timer_label.config(text="Break", fg="#e7305b")
        elif reps % 2 == 0:
            self.count_down(short_break_sec)
            self.timer_label.config(text="Break", fg="#e2979c")
        else:
            self.count_down(work_sec)
            self.timer_label.config(text="Work", fg="#e2979c")
    
    #Metodo cuenta atras
    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec  =count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        self.canvas_tomato.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            global timer
            timer = root.after(1000, self.count_down, count-1)
        else:
            self.start_timer()
            marks = ""
            for _ in range(math.floor(reps/2)):
                marks += "✅"
                self.check_marks.config(text=marks)





# Creamos la raiz o base de la apliacion
root = Tk()
root.title("Primera Aplicacion")
root.geometry("500x600")

reps = 0
timer = None
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Instancia de la clase pantalla para crear la pantalla de inicio de mi aplicacion
aplicacion = pantalla_inicio(root)
aplicacion.mainloop()