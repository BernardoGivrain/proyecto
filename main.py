from prettytable import PrettyTable
from tarea import Tarea
from datetime import datetime
from openpyxl import Workbook, load_workbook
from logo import logo

print(logo)


wb = load_workbook('C:/Users/Givrain/OneDrive/Escritorio/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')
ws = wb.active

tarea = Tarea(1,'', '')

tabla_tarea = PrettyTable(['Id. de Tarea', 'Título', 'Fecha de creación', 'Fecha límite', 'Completada'])

def diferencia_dias(fecha_limite, fecha_creacion):

    dia_creacion = fecha_creacion.date()
    dia_limite = fecha_limite.date()
    diferencia_dias = dia_limite - dia_creacion
    print(f"Tienes {diferencia_dias.days} días para completar la tarea")

def agregar_tarea():
    fecha_creacion = datetime.now()

    print("Proporcione la fecha límite para realizar esta tarea. ")

    dia_limite = int(input("Ingrese el día de la fecha límite: "))
    mes_limite = int(input("Ingrese el mes de la fecha límite: "))
    anio_limite =  int(input("Ingrese el año de la fecha límite: "))
    fecha_limite = datetime(anio_limite, mes_limite, dia_limite)

    diferencia_dias(fecha_limite, fecha_creacion)

    tarea.titulo = input('Inserte el titulo de la tarea: ')
    tarea.fecha_creacion = fecha_creacion
    tarea.fecha_limite = fecha_limite
    ws.append((tarea.id, tarea.titulo, tarea.fecha_creacion, tarea.fecha_limite, tarea.completado))
    wb.save('C:/Users/Givrain/OneDrive/Escritorio/Primer Semestre - tec/Pensamiento/proyecto/tareas.xlsx')

    
    
   


print(logo)
print(tabla_tarea)
print('')

respuesta_usuario = input('¿Qué desea hacer? a: agregar tarea b: eliminar c: editar s: salir ')

while respuesta_usuario != 's':

    if respuesta_usuario == 'a':
        agregar_tarea()

    respuesta_usuario = input('¿Qué desea hacer? a: agregar tarea b: eliminar c: editar s: salir')
    
print('Gracias por usar el programa!')






