import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
NOMBRE: FABRICIO
APELLIDO: DE SA TORRES
---
ejercicio: 4-6
'''
'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
                
        '''
        Enunciado:
        Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
        Calcular la suma acumulada y el promedio de los números ingresados. 
        Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio
        '''
        #ESTRUCTURAS COMPLEJAS
        '''
        contador_numero = 0
        acumulador_numeros = 0

        while contador_numero < 5 and acumulador_numeros < 20: # voy a ingresar 5 numeros
            numero = int(prompt('numero','ingrese un numero'))
            contador_numero += 1
            #contador_numero -= 1
            #contador_numero *= 1 # OPERADORES DE ACUMULACIÓN, primero multiplica, luego asigna
            #contador_numero /= 1
            acumulador_numeros += numero # acumulador_numeros = acumulador_numeros + numero
        
        print("Acumulador: {0}\nContador: {1}".format(acumulador_numeros,contador_numero))
        '''
        #promedio_de_edades = acumulador_edades / cantidad_alumnos
        
        contador_numeros = 0 #inicializar la variable control
        acumulador_numeros = 0
        
        while contador_numeros < 5: #condición que se evalúa
            numero = prompt('EJ 4-6','Ingresar número')
            while not numero.isdigit() or numero == None or len(numero) > 6:
                numero = prompt('Error','Ingresar número válido')
            numero = int(numero)
            contador_numeros += 1 #cambiar la condición
            acumulador_numeros += numero
            
        promedio = acumulador_numeros / contador_numeros
        
        self.txt_suma_acumulada.delete(0,100)
        self.txt_suma_acumulada.insert(0,acumulador_numeros)
        
        self.txt_promedio.delete(0,100)
        self.txt_promedio.insert(0,promedio)

        print('Acumulador: {0}\nContador: {1}\nPromedio: {2}'.format(acumulador_numeros,contador_numeros,promedio))
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
