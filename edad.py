# Codigo de ejemplo para Git
# Autor: Jefry Navas <jnavass@est.ups.edu.ec>
# Fecha: 22-06-2020
# Versión: 0.0.1
#
# Calcula tu edad al año actual
#

anio_actual = 2020
mes_actual = 6
nombre = input("Cuál es tu nombre: ")
anio_nacimiento = int(input("En que año naciste: "))
mes_nacimiento = int(input("En que mes naciste [1-12]: "))
edad = anio_actual - anio_nacimiento

if mes_nacimiento > mes_actual:
 edad -= 1

print("\nHola ",nombre," tu edad en este año será: ",edad);

