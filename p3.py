class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def es_saldo_negativo(self):
        return self.saldo < 0

    def mostrar_datos(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"
class CuentasBancarias:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def saldo_deudor_total(self):
        saldo_total = 0.0
        for cuenta in self.cuentas:
            if cuenta.es_saldo_negativo():
                saldo_total += cuenta.saldo
        return saldo_total

    def mostrar_cuentas_negativas(self):
        cuentas_negativas = []
        for cuenta in self.cuentas:
            if cuenta.es_saldo_negativo():
                cuentas_negativas.append(cuenta)
        return cuentas_negativas
    
num_cuentas = int(input("Ingrese el número de cuentas bancarias a crear: "))
cuentas_bancarias = CuentasBancarias()

for i in range(num_cuentas):
    titular = input(f"Ingrese el nombre del titular de la cuenta {i + 1}: ")
    saldo = float(input(f"Ingrese el saldo de la cuenta {i + 1}: "))
    cuenta = CuentaBancaria(titular, saldo)
    cuentas_bancarias.agregar_cuenta(cuenta)

print("Saldo deudor total:", cuentas_bancarias.saldo_deudor_total())

print("Cuentas con saldo negativo:")
for cuenta in cuentas_bancarias.mostrar_cuentas_negativas():
    print(cuenta.mostrar_datos())
