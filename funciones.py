class InterfazFunciones:
    def __init__(self, aritmetica, trigonometrica):
        self.aritmetica = aritmetica
        self.trigonometrica = trigonometrica

    def sumar(self, cuadro_a, cuadro_b, resultado_aritmetico):
        self.aritmetica.numero_a = float(cuadro_a.get())
        self.aritmetica.numero_b = float(cuadro_b.get())
        resultado_aritmetico.set(self.aritmetica.suma())

    def restar(self, cuadro_a, cuadro_b, resultado_aritmetico):
        self.aritmetica.numero_a = float(cuadro_a.get())
        self.aritmetica.numero_b = float(cuadro_b.get())
        resultado_aritmetico.set(self.aritmetica.resta())

    def multiplicar(self, cuadro_a, cuadro_b, resultado_aritmetico):
        self.aritmetica.numero_a = float(cuadro_a.get())
        self.aritmetica.numero_b = float(cuadro_b.get())
        resultado_aritmetico.set(self.aritmetica.multiplicacion())

    def dividir(self, cuadro_a, cuadro_b, resultado_aritmetico):
        self.aritmetica.numero_a = float(cuadro_a.get())
        self.aritmetica.numero_b = float(cuadro_b.get())
        resultado = self.aritmetica.division()
        if isinstance(resultado, str):
            resultado_aritmetico.set(resultado)
        else:
            resultado_aritmetico.set(f"{resultado:.4f}")

    def calcular_seno(self, cuadro_angulo, resultado_trigonometrico):
        self.trigonometrica.angulo = float(cuadro_angulo.get())
        resultado_trigonometrico.set(self.trigonometrica.seno())

    def calcular_coseno(self, cuadro_angulo, resultado_trigonometrico):
        self.trigonometrica.angulo = float(cuadro_angulo.get())
        resultado_trigonometrico.set(self.trigonometrica.coseno())

    def calcular_tangente(self, cuadro_angulo, resultado_trigonometrico):
        self.trigonometrica.angulo = float(cuadro_angulo.get())
        resultado_trigonometrico.set(self.trigonometrica.tangente())

    def calcular_cotangente(self, cuadro_angulo, resultado_trigonometrico):
        self.trigonometrica.angulo = float(cuadro_angulo.get())
        resultado_trigonometrico.set(self.trigonometrica.cotangente())

    def calcular_secante(self, cuadro_angulo, resultado_trigonometrico):
        self.trigonometrica.angulo = float(cuadro_angulo.get())
        resultado_trigonometrico.set(self.trigonometrica.secante())

    def calcular_cosecante(self, cuadro_angulo, resultado_trigonometrico):
        self.trigonometrica.angulo = float(cuadro_angulo.get())
        resultado_trigonometrico.set(self.trigonometrica.cosecante())
