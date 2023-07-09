import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: FABRICIO    
apellido: DE SA TORRES
---
Ejercicio: entrada_salida_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Importe")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe = customtkinter.CTkEntry(master=self)
        self.txt_importe.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Descuento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_descuento = customtkinter.CTkEntry(master=self)
        self.txt_descuento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        '''
        Enunciado:
        Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txt_importe y txt_descuento), 
        transformarlos en números y mostrar el importe actualizado con el descuento utilizando el Dialog Alert.
        '''
        txt_importe_float = float(self.txt_importe.get())
        txt_descuento_float = float(self.txt_descuento.get())
        descuento_importe = txt_importe_float * txt_descuento_float / 100
        importe_actualizado = txt_importe_float - descuento_importe
        alert(title='Importe actualizado', message= importe_actualizado)

        '''
        CLASE DE APOYO SÁBADOS
        '''
        '''
        importe = self.txt_importe.get()
        importe = float(importe)
        descuento = self.txt_descuento.get()
        descuento = int(descuento)
        importe_con_descuento = importe - (importe * descuento / 100)
        # si me pide cual es el descuento hago
        #importe_descuento = (importe * descuento / 100)
        alert(title = "UTN", message = importe_con_descuento)
        '''
        


        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()