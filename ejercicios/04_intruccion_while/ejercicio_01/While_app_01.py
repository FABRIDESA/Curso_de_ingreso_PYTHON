import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
---
ejercicio: 4-1
'''
'''
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        '''
        Enunciado:
        Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
        10 repeticiones con números ASCENDENTE desde el 1 al 10
        '''
        numero = 0 #inicialización de mi variable de control
        while (numero < 10): #condición para controlar cuantas veces se debe iterar
            numero = numero + 1 #le sumo 1
            alert(message=numero)
        #OTRA FORMA
        '''
        numero = 0
        while (numero < 10):
            numero = numero +1
            alert(message=str(numero))
        '''
        '''
        OTRO EJEMPLO
        test = prompt("test","test")

        while test is None:
            prompt('test','test')

        print(test)
        '''
        '''
        OTRO EJEMPLO
        test = prompt("test","test")

        while True:
            test = prompt('test','test')
            if test is not None:
                break
        print(test)
        '''
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()