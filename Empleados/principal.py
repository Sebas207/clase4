'''
from empleado import Empleado

e1 = Empleado()
e1.setNombre("Jonathan")
e1.apellido = "Campos Lozano"
e1.cargo = "Profesor"
e1.salario = "20000"

print(e1)

e2 = Empleado()
e2.setNombre("Johan")
e2.apellido = "Peña Montaño"
e2.cargo = "Gerente"
e2.salario = "5000000"

print(e2)

from indicadores import Indicadores

i = Indicadores()
print('trm =', i.trm())
print('salario minimo =', i.salariominimo())

'''

from nomina import Nomina

listaNomina = []

while True: 
    print("1. Calcular Nomina")
    print("10. salir")
    respuesta = input("ingrese la opcion")

    if  respuesta == "1":
        renglon = []
        n = Nomina()
        n.setSalario(float(input("ingrese el salario: ")))
        n.setDiasLiquidados(int(input(("ingrese los dias liquidados:"))))

        renglon.append(n.getSalario())
        renglon.append(n.getDiasLiquidados())
        renglon.append(n.salarioDevengado())
        renglon.append(n.auxilioTransporte())
        renglon.append(n.totalDevengado())
        listaNomina.append(renglon)


    elif respuesta == "10":
        print("saliendo")
        break
for i in listaNomina:
    print(i)