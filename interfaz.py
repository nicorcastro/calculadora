import tkinter as tk
from tkinter import *
from interfazFunciones import InterfazFunciones
from calculadoraBase import Aritmetica, Trigonometrica

class InterfazCalculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry('500x500')
        self.ventana.title('Calculadora')

        self.aritmetica = Aritmetica()
        self.trigonometrica = Trigonometrica()

        marco_principal = Frame(self.ventana)
        marco_principal.pack(expand=True, fill='both', padx=10, pady=10)

        # Crear instancia de InterfazFunciones
        self.interfaz_funciones = InterfazFunciones(self.aritmetica, self.trigonometrica)

        # Crear cuadros de entrada
        cuadro_a = Entry(marco_principal)
        cuadro_b = Entry(marco_principal)
        cuadro_angulo = Entry(marco_principal)

        # Crear etiquetas
        etiqueta_a = Label(marco_principal, text="Número A:")
        etiqueta_b = Label(marco_principal, text="Número B:")
        etiqueta_angulo = Label(marco_principal, text="Ángulo:")

        # Crear botones para operaciones aritméticas
        boton_sumar = Button(marco_principal, text="Sumar", command=lambda: self.interfaz_funciones.sumar(cuadro_a, cuadro_b, resultado_aritmetico))
        boton_restar = Button(marco_principal, text="Restar", command=lambda: self.interfaz_funciones.restar(cuadro_a, cuadro_b, resultado_aritmetico))
        boton_multiplicar = Button(marco_principal, text="Multiplicar", command=lambda: self.interfaz_funciones.multiplicar(cuadro_a, cuadro_b, resultado_aritmetico))
        boton_dividir = Button(marco_principal, text="Dividir", command=lambda: self.interfaz_funciones.dividir(cuadro_a, cuadro_b, resultado_aritmetico))

        # Crear botones para funciones trigonométricas
        boton_seno = Button(marco_principal, text="Seno", command=lambda: self.interfaz_funciones.calcular_seno(cuadro_angulo, resultado_trigonometrico))
        boton_coseno = Button(marco_principal, text="Coseno", command=lambda: self.interfaz_funciones.calcular_coseno(cuadro_angulo, resultado_trigonometrico))
        boton_tangente = Button(marco_principal, text="Tangente", command=lambda: self.interfaz_funciones.calcular_tangente(cuadro_angulo, resultado_trigonometrico))
        boton_cotangente = Button(marco_principal, text="Cotangente", command=lambda: self.interfaz_funciones.calcular_cotangente(cuadro_angulo, resultado_trigonometrico))
        boton_secante = Button(marco_principal, text="Secante", command=lambda: self.interfaz_funciones.calcular_secante(cuadro_angulo, resultado_trigonometrico))
        boton_cosecante = Button(marco_principal, text="Cosecante", command=lambda: self.interfaz_funciones.calcular_cosecante(cuadro_angulo, resultado_trigonometrico))

        # Crear etiquetas para mostrar resultados
        resultado_aritmetico = StringVar()
        resultado_trigonometrico = StringVar()
        etiqueta_resultado_aritmetico = Label(marco_principal, textvariable=resultado_aritmetico)
        etiqueta_resultado_trigonometrico = Label(marco_principal, textvariable=resultado_trigonometrico)

        # Organizar widgets en la interfaz
        etiqueta_a.grid(row=0, column=0)
        cuadro_a.grid(row=0, column=1)
        etiqueta_b.grid(row=1, column=0)
        cuadro_b.grid(row=1, column=1)
        etiqueta_angulo.grid(row=2, column=0)
        cuadro_angulo.grid(row=2, column=1)

        boton_sumar.grid(row=3, column=0)
        boton_restar.grid(row=3, column=1)
        boton_multiplicar.grid(row=3, column=2)
        boton_dividir.grid(row=3, column=3)

        boton_seno.grid(row=4, column=0)
        boton_coseno.grid(row=4, column=1)
        boton_tangente.grid(row=4, column=2)
        boton_cotangente.grid(row=5, column=0)
        boton_secante.grid(row=5, column=1)
        boton_cosecante.grid(row=5, column=2)

        etiqueta_resultado_aritmetico.grid(row=6, column=0, columnspan=4)
        etiqueta_resultado_trigonometrico.grid(row=7, column=0, columnspan=4)

        # Ejecutar la aplicación
        self.ventana.mainloop()
