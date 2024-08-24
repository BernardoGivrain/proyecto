from prettytable import PrettyTable
import datetime
logo = '''

████████╗░█████╗░░██████╗██╗░░██╗  ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
╚══██╔══╝██╔══██╗██╔════╝██║░██╔╝  ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
░░░██║░░░██ ████║╚█████╗░█████═╝░  ██╔████╔██║██ ████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
░░░██║░░░██╔══██║░╚═══██╗██╔═██╗░  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║██████╔╝██║░╚██╗  ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝
'''

print(logo)
tabla_tarea = PrettyTable(['Id. de Tarea', 'Descripción', 'Fecha de creación', 'Fecha límite', 'Completada'])
print(tabla_tarea)

print("Proporcione la fecha límite para realizar esta tarea ")

dia_limite = int(input("Ingrese el día de la fecha límite: "))
mes_limite = int(input("Ingrese el mes de la fecha límite: "))
anio_limite =  int(input("Ingrese el año de la fecha límite: "))

fecha_creacion = datetime.datetime.now()
fecha_limite = datetime.datetime(anio_limite, mes_limite, dia_limite)

dia_creacion = fecha_creacion.date()
dia_limite = fecha_limite.date()

diferencia_dias = dia_limite - dia_creacion

print(f"Tienes {diferencia_dias.days} días para completar la tarea")





