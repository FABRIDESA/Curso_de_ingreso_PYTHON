import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
---
ejercicio: 4-4
'''
'''
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
                
        '''
        Enunciado:
        Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
        Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
        volverlo a solicitar hasta que la condición se cumpla
        '''
        numero = prompt(title='EJ 4-4', prompt='Ingrese un número entre 0 y 9')
        while numero == None or numero.isdigit() == False or not(int(numero) >= 0 and int(numero) <= 9):#recordar el int para operaciones numéricas
            alert(title='Error', message='Escriba un número entre 0 y 9')
            numero = int(prompt(title='EJ 4-4', prompt='Ingrese un número entre 0 y 9'))
        alert(title='EJ 4-4', message='El número ingresado es válido')

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()