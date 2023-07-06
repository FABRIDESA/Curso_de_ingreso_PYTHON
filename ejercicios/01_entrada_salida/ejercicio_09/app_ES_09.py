import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: FABRICIO    
apellido: DE SA TORRES
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        '''
        Enunciado:
        Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
        transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
        '''
        #numero = int(self.txt_sueldo.get())
        #alert("lalal", numero)
        
        #Obteniendo valores contenidos en cajas de texto/Los transformo en números con float()/
        txt_sueldo_float= float(self.txt_sueldo.get())
        txt_incremento_float= float(self.txt_incremento.get())
        incremento = 1 + (txt_incremento_float/100)
        sueldo_actualizado = txt_sueldo_float * incremento #PARA SUBIR EL SUELDO
        alert(title='Sueldo actualizado', message= sueldo_actualizado)
        
        '''
        PARA REDUCIR EL SUELDO SERÍA...
        txt_sueldo_float= float(self.txt_sueldo.get())
        txt_decremento_float= float(self.txt_incremento.get())
        decremento_sueldo = txt_sueldo_float * (txt_decremento_float/100)
        sueldo_actualizado = txt_sueldo_float - decremento_sueldo
        alert(title='Sueldo actualizado', message= sueldo_actualizado)
        '''
        #decremento= txt_sueldo_float - (1 + (txt_incremento_float/100))
        
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()