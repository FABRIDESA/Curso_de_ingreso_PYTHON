import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: FABRICIO    
apellido: DE SA TORRES
---
Ejercicio: entrada_salida_03
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener el contenido de la caja de texto y luego 
mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)

        """
        self.label2 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=1, column=1)

        
        self.label3 = customtkinter.CTkLabel(master=self, text="Sector")
        self.label3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_sector = customtkinter.CTkEntry(master=self)
        self.txt_sector.grid(row=2, column=1)
        """
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        """
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=3, pady=20, columnspan=2, sticky="nsew")
        """


    def btn_mostrar_on_click(self):
        """
        Enunciado:
        Al presionar el botón  'Mostrar', se deberá obtener el contenido de la caja de texto y luego 
        mostrarlo utilizando el Dialog Alert
        """
        nombre = self.txt_nombre.get()
        alert(title='Alert', message=nombre)

        #FORMA MÁS AVANZADA
        """
        nombre = self.txt_nombre.get()
        apellido = self.txt_apellido.get()
        sector = self.txt_sector.get()
        saludo = "Hola {0} {1}, trabajas en {2}".format(nombre,apellido,sector)
        alert(title='Saludo', message=saludo)
        """
                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()