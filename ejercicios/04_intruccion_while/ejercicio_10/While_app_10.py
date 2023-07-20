import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
---
ejercicio: 4-10
'''
'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
                
        '''
        Enunciado:
        Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
        quiera hasta que presione el botón Cancelar (en el prompt). 
        Luego calcular:
            La suma acumulada de los negativos
            La suma acumulada de los positivos
            Cantidad de números positivos ingresados
            Cantidad de números negativos ingresados
            Cantidad de ceros
            Diferencia entre la cantidad de los números positivos ingresados y los negativos

        Informar los resultados mediante alert()
        '''
        suma_acumulada_negativos = 0 #acumulador
        suma_acumulada_positivos = 0 #acumulador
        cantidad_numeros_positivos= 0 #contador
        cantidad_numeros_negativos = 0 #contador
        cantidad_ceros = 0 #contador
        
        while True:
            numero = prompt(title="UTN", prompt="Ingrese un número")
            if numero == None:
                break
            numero = int(numero)
            if numero > 0:
                cantidad_numeros_positivos += 1
                suma_acumulada_positivos += numero
            elif numero == 0:
                cantidad_ceros += 1
            else: 
                cantidad_numeros_negativos += 1
                suma_acumulada_negativos += numero
        diferencia = cantidad_numeros_positivos - cantidad_numeros_negativos
        alert(title= "UTN", message= "Suma acumulada de los positivos: {0}\nSuma acumulada de los negativos: {1}\nCantidad de numeros positivos: {2}\nCantidad de numeros negativos: {3}\nCantidad de ceros: {4}\nDiferencia entre cantidad de positivos y negativos: {5}".format(suma_acumulada_positivos,suma_acumulada_negativos,cantidad_numeros_positivos,cantidad_numeros_negativos,cantidad_ceros,diferencia))

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
